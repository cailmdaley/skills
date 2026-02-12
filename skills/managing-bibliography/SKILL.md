---
name: managing-bibliography
description: >
  Read arXiv paper source and add BibTeX entries via ADS API.
  Use for research that requires reading full paper text and managing citations.
  Triggers on: "read paper", "cite", "add to bibliography", "bibtex", "ADS",
  "arXiv", "find paper", "add citation", or any request to read scientific papers
  or manage references.
---

# Managing Bibliography

Read scientific papers and manage citations. Two capabilities:

1. **Read papers** — Download arXiv LaTeX source to read full text, verify claims, understand methodology
2. **Cite papers** — Fetch BibTeX from NASA ADS and add to bibliography

## Reading Papers

Download arXiv LaTeX source to read full paper text:

```bash
# Download source (replace ID as needed)
curl -L -o /tmp/2503.19441.tar.gz "https://arxiv.org/src/2503.19441"

# Extract
mkdir -p /tmp/2503.19441 && cd /tmp/2503.19441 && tar -xzf /tmp/2503.19441.tar.gz

# Find the main tex file
ls *.tex
```

Available after extraction:
- Full paper text (not just abstract), equations, methodology details
- Exact author phrasing for verification
- Their bibliography (.bib or .bbl files) for cross-referencing

---

## ADS API Setup

Before using citation features, verify `$ADS_API_TOKEN` is set:

```bash
echo $ADS_API_TOKEN
```

If missing, direct the user to create one at https://ui.adsabs.harvard.edu/user/settings/token and export it. Do not proceed with ADS API calls until the token is available.

---

## Citing Papers

When adding a paper to the bibliography:

1. **Web search** for the paper using description + "arxiv"
   - Look for arXiv ID in format `YYMM.NNNNN`
   - If multiple results, show options and ask user to select

2. **Query ADS API** to get bibcode using arXiv ID
   ```bash
   curl -H "Authorization: Bearer $ADS_API_TOKEN" \
     'https://api.adsabs.harvard.edu/v1/search/query?q=arXiv:YYMM.NNNNN&fl=bibcode'
   ```

3. **Fetch BibTeX entry** with abstract from ADS
   ```bash
   curl -H "Authorization: Bearer $ADS_API_TOKEN" \
     'https://api.adsabs.harvard.edu/v1/export/bibtexabs/{bibcode}'
   ```

4. **Parse BibTeX** to extract author names and year:
   - Parse `author = {...}` field for last names
   - Parse `year = YYYY` field for publication year
   - Generate citation key based on author count:
     - 1 author: `firstauthor{YY}` (e.g., `asgari17`)
     - 2 authors: `firstauthor.secondauthor{YY}` (e.g., `schneider.kilbinger12`)
     - 3+ authors: `firstauthor.etal{YY}` (e.g., `wright.etal25`)
   - Use only last names, lowercase, final 2 digits of year

5. **Replace citation key** in BibTeX entry
   - Update the entry key on the first line (before the opening brace)
   - Keep all other fields unchanged

6. **Append to bibliography** file
   - Add the modified entry to the project's `.bib` file
   - Check for duplicate keys first and warn if found

7. **Report success**
   - Show the user the complete entry that was added
   - Confirm file location

## Citation Key Generation

**Examples from BibTeX parsing**:
- `author = {{Wright}, Angus H. and {Stölzner}, Benjamin and ...}` + `year = 2025` → `wright.etal25`
- `author = {{Schneider}, Peter and {Kilbinger}, Martin}` + `year = 2012` → `schneider.kilbinger12`
- `author = {{Asgari}, Marika}` + `year = 2017` → `asgari17`

## Notes

- Always use the `bibtexabs` endpoint (not `bibtex`) to include abstracts
- ADS author format: `author = {{LastName}, FirstName and {LastName}, FirstName ...}`
