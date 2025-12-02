#!/usr/bin/env python3
"""
Zotero Publications Fetcher for GitHub Pages
Fetches publications from Zotero API, cleans data, and exports YAML for Jekyll

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
# Helper Functions
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
    
    # Hawaiian Archipelago keywords
    if any(area in title_lower for area in ['hawai', 'hawaii', 'kahekili', 'maui', 'ahu', 
                                              'northwestern', 'papahānaumokuākea', 'kauai', 'oahu', 'big island']):
        return 'Hawaiian Archipelago'
    
    # American Samoa keywords
    elif any(area in title_lower for area in ['samoa', 'aua', 'swains', 'american samoa']):
        return 'American Samoa'
    
    # Mariana Archipelago keywords
    elif any(area in title_lower for area in ['guam', 'mariana', 'saipan', 'tinian', 'rota']):
        return 'Mariana Archipelago'
    
    # Pacific Remote Island Areas (PRIA)
    elif any(area in title_lower for area in ['wake', 'baker', 'howland', 'jarvis', 'palmyra', 
                                               'kingman', 'johnston', 'jarvisisland']):
        return 'Pacific Remote Island Areas'
    
    # Pacific-wide (catch-all for broad Pacific studies)
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
    
    Args:
        base_url: Zotero API endpoint URL
        headers: Request headers with API key
        batch_size: Items per request (max 100)
    
    Returns:
        List of all items from the collection
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
            
            if not items:  # No more items
                print("✓ All items fetched")
                break
            
            all_items.extend(items)
            start += batch_size
            retry_count = 0  # Reset retry counter on success
            
            # Respect rate limits
            if 'Backoff' in response.headers:
                backoff_seconds = int(response.headers['Backoff'])
                print(f"⏳ Rate limited. Waiting {backoff_seconds} seconds...")
                time.sleep(backoff_seconds)
            else:
                time.sleep(0.5)  # Be nice to the API
                
        except requests.exceptions.RequestException as e:
            retry_count += 1
            if retry_count >= max_retries:
                print(f"❌ Error fetching data (max retries exceeded): {e}")
                break
            print(f"⚠️ Error fetching data: {e}. Retrying ({retry_count}/{max_retries})...")
            time.sleep(2 ** retry_count)  # Exponential backoff
    
    return all_items


# =============================================================================
# Processing Functions
# =============================================================================

def process_publications(all_items: List[Dict]) -> List[Dict]:
    """
    Process and filter publications from API response.
    
    Args:
        all_items: Raw items from Zotero API
    
    Returns:
        Cleaned and filtered publications list
    """
    filtered_publications = []
    duplicate_checker = set()
    errors = 0
    
    for entry in all_items:
        try:
            data = entry.get("data", {})
            
            # Extract fields
            title = data.get("title", "").strip()
            if not title:
                continue  # Skip entries without title
            
            # Check for duplicates (by title)
            if title in duplicate_checker:
                continue
            duplicate_checker.add(title)
            
            # Build publication record
            pub = {
                "title": title,
                "creators": clean_creators(data.get("creators", [])),
                "year": extract_year(data.get("date", "")),
                "doi": data.get("DOI", "").strip() or None,
                "issn": data.get("ISSN", "").strip() or None,
                "url": data.get("url", "").strip() or None,
                "region": assign_region(title),
                # Additional useful fields
                "item_type": data.get("itemType", ""),
                "publication_title": data.get("publicationTitle", "").strip() or None,
            }
            
            filtered_publications.append(pub)
        
        except Exception as e:
            print(f"⚠️ Error processing entry: {e}")
            errors += 1
            continue
    
    # Sort by year (descending)
    filtered_publications.sort(key=lambda x: x["year"] or 0, reverse=True)
    
    print(f"\n📊 Processing Results:")
    print(f"  ✓ Successfully processed: {len(filtered_publications)}")
    print(f"  ✗ Errors encountered: {errors}")
    print(f"  🔄 Duplicates removed: {len(all_items) - len(filtered_publications) - errors}")
    
    # Print region distribution
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
    Export publications in multiple formats.
    
    Args:
        filtered_publications: List of cleaned publications
        output_dir: Directory to save output files
    
    Returns:
        Dictionary with file paths
    """
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    files = {}
    
    # Export to CSV
    csv_file = output_dir / "filtered_pifsc_publications.csv"
    with open(csv_file, "w", newline="", encoding="utf-8") as f:
        if filtered_publications:
            writer = csv.DictWriter(f, fieldnames=filtered_publications[0].keys())
            writer.writeheader()
            writer.writerows(filtered_publications)
    files['csv'] = str(csv_file)
    print(f"✓ CSV export: {csv_file}")
    
    # Export to JSON
    json_file = output_dir / "filtered_pifsc_publications.json"
    with open(json_file, "w", encoding="utf-8") as f:
        json.dump(filtered_publications, f, indent=2, ensure_ascii=False)
    files['json'] = str(json_file)
    print(f"✓ JSON export: {json_file}")
    
    # Export to YAML (for Jekyll)
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
    
    # Validate required arguments
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
    
    # Setup
    print("🚀 Zotero Publications Fetcher")
    print("=" * 60)
    
    base_url = f"https://api.zotero.org/groups/{parsed_args.group_id}/collections/{parsed_args.collection_key}/items"
    headers = {
        "Zotero-API-Key": parsed_args.api_key,
        "Accept": "application/json",
    }
    
    print(f"📋 Configuration:")
    print(f"  Group ID: {parsed_args.group_id}")
    print(f"  Collection Key: {parsed_args.collection_key}")
    print(f"  Output Directory: {parsed_args.output_dir}")
    print()
    
    # Fetch
    print("🔄 Step 1: Fetching Publications")
    print("-" * 60)
    # If no collection key, fetch all items from group; otherwise fetch from specific collection
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
    
    # Process
    print("🔄 Step 2: Processing Publications")
    print("-" * 60)
    filtered_publications = process_publications(all_items)
    print()
    
    if not filtered_publications:
        print("⚠️ No publications to export")
        return 1
    
    # Export
    print("🔄 Step 3: Exporting Publications")
    print("-" * 60)
    files = export_publications(filtered_publications, parsed_args.output_dir)
    print()
    
    # Summary
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
