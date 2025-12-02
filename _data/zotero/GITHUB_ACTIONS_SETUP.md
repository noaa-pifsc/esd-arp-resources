# GitHub Actions Setup Guide

## How to Set Up Automatic Publication Updates

Follow these steps to enable automatic Zotero publication fetching via GitHub Actions:

### Step 1: Get Your Zotero Credentials

1. Visit https://www.zotero.org/settings/keys
2. Click "Create new private key"
3. Provide a description (e.g., "GitHub Actions")
4. Under permissions, enable "Read-only library access"
5. Copy your **API Key** (looks like: `REDACTED_ZOTERO_API_KEY`)

6. Find your **Group ID**:
   - Go to your Zotero group page
   - Look at the URL: `https://www.zotero.org/groups/YOUR_GROUP_ID`
   - Example: `REDACTED_GROUP_ID`

7. Find your **Collection Key**:
   - In your Zotero group, click on the collection you want
   - Look at the URL or collection settings
   - Example: `VD8Z582Z`

### Step 2: Add Repository Secrets

1. In GitHub, go to your repository
2. Click **Settings** → **Secrets and variables** → **Actions**
3. Click **New repository secret**
4. Create three secrets:

   | Secret Name | Value |
   |---|---|
   | `ZOTERO_API_KEY` | Your API key from Step 1 |
   | `ZOTERO_GROUP_ID` | Your group ID (e.g., `REDACTED_GROUP_ID`) |
   | `ZOTERO_COLLECTION_KEY` | Your collection key (e.g., `VD8Z582Z`) |

**Screenshot example:**
```
Settings → Secrets and variables → Actions

Name: ZOTERO_API_KEY
Secret: REDACTED_ZOTERO_API_KEY
[Add secret]

Name: ZOTERO_GROUP_ID
Secret: REDACTED_GROUP_ID
[Add secret]

Name: ZOTERO_COLLECTION_KEY
Secret: VD8Z582Z
[Add secret]
```

### Step 3: Add the Workflow File

1. Create the directory `.github/workflows/` in your repo (if it doesn't exist):
   ```bash
   mkdir -p .github/workflows
   ```

2. Copy the file `update-publications.yml` into `.github/workflows/`

3. Optionally, edit the schedule in `update-publications.yml`:
   ```yaml
   schedule:
     - cron: '0 2 * * *'  # Daily at 2 AM UTC
   ```

### Step 4: Prepare Your Repository Structure

1. Create the `_data` folder (if it doesn't exist):
   ```bash
   mkdir -p _data
   ```

2. Make sure you have a `_layouts/publications.html` file

### Step 5: Add the Python Script

1. Copy `fetch_zotero_publications.py` to the root of your repository

### Step 6: Commit and Push

```bash
git add .github/workflows/update-publications.yml
git add fetch_zotero_publications.py
git add _data/
git commit -m "Add Zotero publication automation"
git push origin main
```

### Step 7: Test the Workflow

1. Go to your repository
2. Click **Actions** tab
3. Click **Update Zotero Publications** workflow (on the left)
4. Click **Run workflow** → **Run workflow** button
5. Wait for the run to complete
6. Check that `_data/filtered_pifsc_publications.yml` was created

### Step 8: Verify GitHub Pages

1. Check that `_data/filtered_pifsc_publications.yml` was committed
2. Your Jekyll site should automatically rebuild and render the publications
3. Visit your GitHub Pages URL to verify the publications appear

## How It Works

```
┌─────────────────────────────────────────────────────────┐
│         GitHub Actions Workflow (Daily at 2 AM)         │
└────────────────────────┬────────────────────────────────┘
                         │
                         ▼
         ┌───────────────────────────────┐
         │  fetch_zotero_publications.py │
         └───────────────┬───────────────┘
                         │
      ┌──────────────────┼──────────────────┐
      │                  │                  │
      ▼                  ▼                  ▼
 Fetch from         Clean &            Assign
 Zotero API         Standardize        Regions
      │                  │                  │
      └──────────────────┼──────────────────┘
                         │
                         ▼
         ┌───────────────────────────────┐
         │  Generate YAML File           │
         │  (_data/...publications.yml)  │
         └───────────────┬───────────────┘
                         │
                         ▼
         ┌───────────────────────────────┐
         │  Commit to GitHub             │
         │  (if changes detected)        │
         └───────────────┬───────────────┘
                         │
                         ▼
         ┌───────────────────────────────┐
         │  GitHub Pages Rebuild         │
         │  (Jekyll renders YAML)        │
         └───────────────────────────────┘
```

## Monitoring

To check if your workflow is running:

1. Go to **Actions** tab in your repository
2. Look for **Update Zotero Publications** workflow runs
3. Click on any run to see details:
   - ✅ = Success
   - ❌ = Failed
   - ⏱️ = In progress

## Troubleshooting

### Workflow not triggering on schedule?

- Workflows are disabled if there's no activity on the repo for 60 days
- Solution: Make any commit to re-enable scheduled workflows

### "API key not provided" error?

- Verify all three secrets are added to your repository
- Check spelling: `ZOTERO_API_KEY`, `ZOTERO_GROUP_ID`, `ZOTERO_COLLECTION_KEY`

### "No items fetched" error?

- Verify your collection is public (or you have API access)
- Confirm Group ID and Collection Key are correct
- Test the API key manually: https://api.zotero.org/users/YOUR_USER_ID (requires API key in header)

### YAML file not appearing in _data folder?

- Check the workflow logs for errors
- Ensure `_data` folder exists in your repo
- Verify git permissions allow pushing

### Publications not rendering on site?

- Check that Jekyll template includes: `site.data.filtered_pifsc_publications`
- Verify YAML file syntax is valid (check logs)
- GitHub Pages may take a few minutes to rebuild

## Scheduling Options

Edit the `cron` line in `.github/workflows/update-publications.yml`:

```yaml
schedule:
  - cron: '0 2 * * *'  # Cron format: minute hour day month weekday (UTC)
```

**Common schedules:**
- `'0 2 * * *'` → Daily at 2:00 AM UTC
- `'0 */6 * * *'` → Every 6 hours
- `'0 0 * * 0'` → Weekly (Sundays at midnight UTC)
- `'0 0 1 * *'` → Monthly (1st of each month at midnight UTC)

[Learn more about cron syntax](https://crontab.guru)

## Manual Trigger

You can manually run the workflow anytime:

1. Go to **Actions** → **Update Zotero Publications**
2. Click **Run workflow** dropdown
3. Click the **Run workflow** button

## Questions?

Refer to the main `ZOTERO_README.md` for more details and customization options.

