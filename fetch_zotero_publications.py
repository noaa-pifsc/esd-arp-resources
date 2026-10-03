#!/usr/bin/env python3
"""
Zotero Publications Fetcher for GitHub Pages
Fetches publications from Zotero API, cleans data, scrapes web pages for missing DOIs, 
and exports YAML for Jekyll.

Usage:
    python fetch_zotero_publications.py
    
Environment Variables (recommended for security):
    ZOTERO_API_KEY - Your Zotero API key
    ZOTERO_GROUP_ID - Your Zotero group ID
    ZOTERO_COLLECTION_KEY - Your collection key
    OUTPUT_DIR - Directory to save output files (default: current directory)

For GitHub Actions, set these as repository secrets.
"""

import os
import json
import csv
import re
import sys
import time
import argparse
from pathlib import Path
from typing import List, Dict, Optional

try:
    import requests
except ImportError:
    print("ERROR: requests library not installed. Run: pip install requests")
    sys.exit(1)

try:
    import yaml
except ImportError:
    print("ERROR: pyyaml library not installed. Run: pip install pyyaml")
    sys.exit(1)


# =============================================================================
# Configuration
# =============================================================================

def get_config():
    """Load configuration from environment variables."""
    return {
        "GROUP_ID": os.getenv("ZOTERO_GROUP_ID"),
        "COLLECTION_KEY": os.getenv("ZOTERO_COLLECTION_KEY"),
        "API_KEY": os.getenv("ZOTERO_API_KEY"),
        "OUTPUT_DIR": os.getenv("OUTPUT_DIR", os.getcwd()),
        "BATCH_SIZE": 100,
    }


# =============================================================================
# Helper & Extraction Functions
# =============================================================================

def extract_doi_from_text(text: str) -> Optional[str]:
    """Extract a DOI string from a URL, HTML, or raw text if present."""
    if not text:
        return None
    # Regular expression matching standard DOI patterns (10.xxxx/...)
    match = re.search(r'10\.\d{4,9}/[-._;()/:A-Za-z0-9]+', text)
    if match:
        # Strip trailing slashes, quotes, or periods often attached by accident
        return match.group(0).rstrip('./"\'')
    return None


def extract_doi_from_webpage(url: str) -> Optional[str]:
    """
    Scrape a webpage (e.g., NOAA Repository) to extract a DOI from HTML metadata or body text.
    """
    if not url or not url.startswith("http"):
        return None
        
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code != 200:
            return None
            
        html_content = response.text
        
        # 1. Search common HTML meta tags used by repositories (e.g., DC.Identifier, citation_doi)
        meta_doi_patterns = [
            r'<meta\s+name=["\'](?:citation_doi|DC\.Identifier|DC\.identifier|doi)["\']\s+content=["\']([^"\']+)["\']',
            r'<meta\s+content=["\']([^"\']+)["\']\s+name=["\'](?:citation_doi|DC\.Identifier|DC\.identifier|doi)["\']'
        ]
        
        for pattern in meta_doi_patterns:
            match = re.search(pattern, html_content, re.IGNORECASE)
            if match:
                extracted = extract_doi_from_text(match.group(1))
                if extracted:
                    return extracted

        # 2. Fallback: Search full page text for a standard DOI pattern (10.xxxx/...)
        return extract_doi_from_text(html_content)

    except requests.exceptions.RequestException:
        return None


def extract_authors_from_crossref(crossref_data: Dict) -> Optional[str]:
    """Extract author names from CrossRef metadata."""
    if not crossref_data:
        return None
    
    authors = crossref_data.get("author", [])
    if not authors:
        return None
    
    author_names = []
    for author in authors:
        given = author.get("given", "").strip()
        family = author.get("family", "").strip()
        if family:
            name = f"{given} {family}".strip() if given else family
            author_names.append(name)
    
    return "; ".join(author_names) if author_names else None


def normalize_doi(doi_string: str) -> str:
    """
    Extract clean DOI from various formats.
    
    Args:
        doi_string: DOI string which may include URL prefix
    
    Returns:
        Clean DOI (e.g., "10.1234/example")
    """
    if not doi_string:
        return ""
    
    doi_string = doi_string.strip()
    # Remove common DOI URL prefixes
    for prefix in ["https://doi.org/", "http://doi.org/", "http://dx.doi.org/", "doi.org/"]:
        if doi_string.lower().startswith(prefix):
            return doi_string[len(prefix):]
    
    return doi_string


def create_doi_url(doi: str) -> str:
    """
    Create a proper DOI URL from a clean DOI.
    
    Args:
        doi: Clean DOI string (e.g., "10.1234/example")
    
    Returns:
        Full DOI URL (e.g., "https://doi.org/10.1234/example")
    """
    if not doi:
        return ""
    
    clean_doi = normalize_doi(doi)
    return f"https://doi.org/{clean_doi}" if clean_doi else ""


# =============================================================================
# CrossRef API Functions
# =============================================================================

def fetch_crossref_metadata(doi: str, retries: int = 3) -> Optional[Dict]:
    """
    Fetch publication metadata from CrossRef API using DOI.
    """
    if not doi:
        return None
    
    doi_clean = doi.replace("https://doi.org/", "").replace("http://dx.doi.org/", "").strip()
    crossref_url = f"https://api.crossref.org/works/{doi_clean}"
    headers = {
        "User-Agent": "NOAA-PIFSC-ESD (mailto:pifsc.publications@noaa.gov)"
    }
    
    for attempt in range(retries):
        try:
            response = requests.get(crossref_url, headers=headers, timeout=10)
            if response.status_code == 200:
                data = response.json()
                if data.get("status") == "ok" and data.get("message"):
                    return data.get("message")
                return None
            elif response.status_code == 404:
                return None
            else:
                if attempt < retries - 1:
                    time.sleep(2 ** attempt)
        except requests.exceptions.RequestException as e:
            if attempt == retries - 1:
                print(f"⚠️ CrossRef lookup failed for DOI {doi_clean}: {e}")
            else:
                time.sleep(2 ** attempt)
    
    return None


def enrich_publication(pub: Dict) -> Dict:
    """
    Enrich publication metadata by fetching missing fields from CrossRef.
    """
    if pub.get("doi"):
        clean_doi = normalize_doi(pub["doi"])
        pub["doi"] = clean_doi if clean_doi else None

    if pub.get("doi") and pub.get("url"):
        extracted_from_url = extract_doi_from_text(pub["url"])
        if extracted_from_url and normalize_doi(extracted_from_url) == pub["doi"]:
            pub["url"] = create_doi_url(pub["doi"])
    
    if not pub.get("doi"):
        return pub
    
    needs_enrichment = (
        not pub.get("creators") or pub["creators"] == "N/A" or
        not pub.get("publication_title") or pub["publication_title"] == "N/A" or
        not pub.get("year") or pub["year"] == "N/A" or
        not pub.get("url") or pub["url"] == "N/A"
    )
    
    if not needs_enrichment:
        return pub
    
    print(f"  🔍 Enriching: {pub.get('title', 'Unknown')[:60]}...", end=" ")
    
    crossref_data = fetch_crossref_metadata(pub["doi"])
    
    if not crossref_data:
        if not pub.get("url") or pub["url"] == "N/A":
            pub["url"] = create_doi_url(pub["doi"])
        print("(DOI link added)")
        return pub
    
    if not pub.get("creators") or pub["creators"] == "N/A":
        authors = extract_authors_from_crossref(crossref_data)
        if authors:
            pub["creators"] = authors
            print("✓ ", end="")
        else:
            print("(no authors)", end=" ")
    
    if not pub.get("publication_title") or pub["publication_title"] == "N/A":
        container_title = crossref_data.get("container-title")
        if container_title and isinstance(container_title, list) and container_title:
            pub["publication_title"] = container_title[0]
            print("✓ ", end="")
        elif isinstance(container_title, str):
            pub["publication_title"] = container_title
            print("✓ ", end="")
    
    if not pub.get("year") or pub["year"] == "N/A":
        issued = crossref_data.get("issued", {})
        if isinstance(issued, dict):
            date_parts = issued.get("date-parts")
            if date_parts and isinstance(date_parts, list) and date_parts[0]:
                pub["year"] = date_parts[0][0]
                print("✓ ", end="")
    
    if not pub.get("url") or pub["url"] == "N/A":
        url_from_crossref = crossref_data.get("URL")
        if url_from_crossref:
            pub["url"] = url_from_crossref
            print("✓ ", end="")
        else:
            pub["url"] = create_doi_url(pub["doi"])
            print("✓", end="")
    
    print()
    time.sleep(0.5)
    return pub


# =============================================================================
# Data Processing Helpers
# =============================================================================

def extract_year(date_str: Optional[str]) -> Optional[int]:
    """Extract 4-digit year from date string."""
    if not date_str:
        return None
    match = re.search(r"\b\d{4}\b", str(date_str))
    return int(match.group(0)) if match else None


def assign_region(title: str) -> str:
    """Assign region based on publication title keywords."""
    if not title:
        return 'Unknown'
    
    title_lower = title.lower()
    
    if any(area in title_lower for area in ['hawai', 'hawaii', 'kahekili', 'maui', 'ahu', 
                                              'northwestern', 'papahānaumokuākea', 'kauai', 'oahu', 'big island']):
        return 'Hawaiian Archipelago'
    elif any(area in title_lower for area in ['samoa', 'aua', 'swains', 'american samoa']):
        return 'American Samoa'
    elif any(area in title_lower for area in ['guam', 'mariana', 'saipan', 'tinian', 'rota']):
        return 'Mariana Archipelago'
    elif any(area in title_lower for area in ['wake', 'baker', 'howland', 'jarvis', 'palmyra', 
                                               'kingman', 'johnston', 'jarvisisland']):
        return 'Pacific Remote Island Areas'
    elif 'pacific' in title_lower:
        return 'Pacific-wide'
    else:
        return 'Unknown'


def clean_creators(creators: List[Dict]) -> str:
    """Format creator names from API response."""
    if not creators:
        return ""
    names = []
    for creator in creators:
        first = creator.get('firstName', '').strip()
        last = creator.get('lastName', '').strip()
        if first or last:
            names.append(f"{first} {last}".strip())
    return "; ".join(names)


# =============================================================================
# API Functions
# =============================================================================

def fetch_all_items(base_url: str, headers: Dict, batch_size: int = 100) -> List[Dict]:
    """
    Fetch all items from Zotero API with pagination support.
    """
    all_items = []
    start = 0
    max_retries = 3
    retry_count = 0
    
    while True:
        params = {"format": "json", "limit": batch_size, "start": start}
        print(f"📥 Fetching items {start} to {start + batch_size}...")
        
        try:
            response = requests.get(base_url, headers=headers, params=params, timeout=15)
            response.raise_for_status()
            items = response.json()
            
            if not items:
                print("✓ All items fetched")
                break
            
            all_items.extend(items)
            start += batch_size
            retry_count = 0
            
            if 'Backoff' in response.headers:
                backoff_seconds = int(response.headers['Backoff'])
                print(f"⏳ Rate limited. Waiting {backoff_seconds} seconds...")
                time.sleep(backoff_seconds)
            else:
                time.sleep(0.5)
                
        except requests.exceptions.RequestException as e:
            retry_count += 1
            if retry_count >= max_retries:
                print(f"❌ Error fetching data (max retries exceeded): {e}")
                break
            print(f"⚠️ Error fetching data: {e}. Retrying ({retry_count}/{max_retries})...")
            time.sleep(2 ** retry_count)
    
    return all_items


# =============================================================================
# Processing Functions
# =============================================================================

def process_publications(all_items: List[Dict]) -> List[Dict]:
    """
    Process, filter, and extract DOIs from Zotero API responses.
    """
    filtered_publications = []
    duplicate_checker = set()
    errors = 0
    
    for entry in all_items:
        try:
            data = entry.get("data", {})
            item_type = data.get("itemType", "")
            
            if item_type in ['attachment', 'note', 'annotation']:
                continue
            
            title = data.get("title", "").strip()
            if not title:
                continue
            
            if title in duplicate_checker:
                continue
            duplicate_checker.add(title)
            
            raw_doi = data.get("DOI", "").strip()
            raw_url = data.get("url", "").strip()
            
            # --- DOI Fallback Logic ---
            # Step 1: Extract DOI if present directly in the URL string
            if not raw_doi and raw_url:
                raw_doi = extract_doi_from_text(raw_url) or ""
            
            # Step 2: Scrape the webpage HTML at raw_url (e.g., repository.library.noaa.gov)
            if not raw_doi and raw_url:
                scraped_doi = extract_doi_from_webpage(raw_url)
                if scraped_doi:
                    raw_doi = scraped_doi
            
            pub = {
                "title": title,
                "creators": clean_creators(data.get("creators", [])),
                "year": extract_year(data.get("date", "")),
                "doi": normalize_doi(raw_doi) or None,
                "issn": data.get("ISSN", "").strip() or None,
                "url": raw_url or None,
                "region": assign_region(title),
                "item_type": data.get("itemType", ""),
                "publication_title": data.get("publicationTitle", "").strip() or None,
            }
            
            filtered_publications.append(pub)
        
        except Exception as e:
            print(f"⚠️ Error processing entry: {e}")
            errors += 1
            continue
    
    print(f"\n  ✓ Successfully processed: {len(filtered_publications)}")
    print(f"  ✗ Errors encountered: {errors}")
    print(f"  🔄 Duplicates removed: {len(all_items) - len(filtered_publications) - errors}")
    
    # Enrich publications with missing data from CrossRef
    print(f"\n📚 Step 2b: Enriching with CrossRef metadata")
    print("-" * 60)
    print(f"Checking for missing publication metadata...")
    missing_count = sum(1 for pub in filtered_publications 
                        if not pub.get("creators") or not pub.get("publication_title") or not pub.get("year"))
    print(f"Found {missing_count} publications with missing data\n")
    
    filtered_publications = [enrich_publication(pub) for pub in filtered_publications]
    print(f"✓ Enrichment complete")
    
    filtered_publications.sort(key=lambda x: x["year"] or 0, reverse=True)
    
    print(f"\n📍 Region Distribution:")
    regions = {}
    for pub in filtered_publications:
        region = pub["region"]
        regions[region] = regions.get(region, 0) + 1
    for region, count in sorted(regions.items()):
        print(f"  {region}: {count}")
    
    return filtered_publications


# =============================================================================
# Export Functions
# =============================================================================

def export_publications(filtered_publications: List[Dict], output_dir: str) -> Dict[str, str]:
    """
    Export publications in multiple formats (CSV, JSON, YAML).
    """
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    files = {}
    
    csv_file = output_dir / "filtered_pifsc_publications.csv"
    with open(csv_file, "w", newline="", encoding="utf-8") as f:
        if filtered_publications:
            writer = csv.DictWriter(f, fieldnames=filtered_publications[0].keys())
            writer.writeheader()
            writer.writerows(filtered_publications)
    files['csv'] = str(csv_file)
    print(f"✓ CSV export: {csv_file}")
    
    json_file = output_dir / "filtered_pifsc_publications.json"
    with open(json_file, "w", encoding="utf-8") as f:
        json.dump(filtered_publications, f, indent=2, ensure_ascii=False)
    files['json'] = str(json_file)
    print(f"✓ JSON export: {json_file}")
    
    yaml_file = output_dir / "filtered_pifsc_publications.yml"
    with open(yaml_file, "w", encoding="utf-8") as f:
        yaml.dump(filtered_publications, f, default_flow_style=False, allow_unicode=True, sort_keys=False)
    files['yaml'] = str(yaml_file)
    print(f"✓ YAML export: {yaml_file}")
    
    return files


# =============================================================================
# Main Function
# =============================================================================

def main(args=None):
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Fetch publications from Zotero and export as YAML for GitHub Pages"
    )
    parser.add_argument(
        "--output-dir",
        default=os.getenv("OUTPUT_DIR", os.getcwd()),
        help="Output directory for exported files (default: current directory)"
    )
    parser.add_argument(
        "--api-key",
        default=os.getenv("ZOTERO_API_KEY"),
        help="Zotero API key (or set ZOTERO_API_KEY env var)"
    )
    parser.add_argument(
        "--group-id",
        default=os.getenv("ZOTERO_GROUP_ID"),
        help="Zotero group ID"
    )
    parser.add_argument(
        "--collection-key",
        default=os.getenv("ZOTERO_COLLECTION_KEY"),
        help="Zotero collection key"
    )
    
    parsed_args = parser.parse_args(args)
    
    if not parsed_args.api_key:
        print("❌ ERROR: Zotero API key not provided.")
        print("   Set ZOTERO_API_KEY environment variable or use --api-key argument")
        sys.exit(1)
    
    if not parsed_args.group_id:
        print("❌ ERROR: Zotero group ID not provided.")
        print("   Set ZOTERO_GROUP_ID environment variable or use --group-id argument")
        sys.exit(1)
    
    if not parsed_args.collection_key:
        print("❌ ERROR: Zotero collection key not provided.")
        print("   Set ZOTERO_COLLECTION_KEY environment variable or use --collection-key argument")
        sys.exit(1)
    
    print("🚀 Zotero Publications Fetcher")
    print("=" * 60)
    
    headers = {
        "Zotero-API-Key": parsed_args.api_key,
        "Accept": "application/json",
    }
    
    print(f"📋 Configuration:")
    print(f"  Group ID: {parsed_args.group_id}")
    print(f"  Collection Key: {parsed_args.collection_key}")
    print(f"  Output Directory: {parsed_args.output_dir}")
    print()
    
    print("🔄 Step 1: Fetching Publications")
    print("-" * 60)
    if parsed_args.collection_key and parsed_args.collection_key != "VD8Z582Z":
        base_url = f"https://api.zotero.org/groups/{parsed_args.group_id}/collections/{parsed_args.collection_key}/items"
        print("Fetching from collection...")
    else:
        base_url = f"https://api.zotero.org/groups/{parsed_args.group_id}/items"
        print("Fetching all items from group...")
    all_items = fetch_all_items(base_url, headers)
    print(f"✓ Fetched {len(all_items)} total items\n")
    
    if not all_items:
        print("⚠️ No items retrieved from Zotero")
        return 1
    
    print("🔄 Step 2: Processing Publications")
    print("-" * 60)
    filtered_publications = process_publications(all_items)
    print()
    
    if not filtered_publications:
        print("⚠️ No publications to export")
        return 1
    
    print("🔄 Step 3: Exporting Publications")
    print("-" * 60)
    files = export_publications(filtered_publications, parsed_args.output_dir)
    print()
    
    print("=" * 60)
    print("✓ SUCCESS")
    print(f"\n📊 Summary:")
    print(f"  Total publications: {len(filtered_publications)}")
    years = [pub['year'] for pub in filtered_publications if pub['year']]
    if years:
        print(f"  Years covered: {min(years)} - {max(years)}")
    print(f"\n📁 Output Files:")
    for fmt, filepath in files.items():
        print(f"  [{fmt.upper()}] {filepath}")
    
    print(f"\n✅ YAML file ready for GitHub Pages: {files['yaml']}")
    print(f"   Copy to: _data/filtered_pifsc_publications.yml in your repo")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())