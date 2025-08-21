## Data Storage

### Folder structure

project-root/
├── data/
│   ├── raw/          # Original, immutable downloads
│   └── processed/    # Cleaned, enriched, or derived artifacts


- `raw/` keeps the exact bytes returned by the API / scraped HTML.  
- `processed/` holds downstream-ready files (parquet for speed & type safety, or CSV for portability).

### Formats & rationale
| File type | Location | Why |
|-----------|----------|-----|
| `.csv`    | `raw/`   | Human-readable, git-diff friendly, lowest-common-denominator. |
| `.parquet`| `processed/` | Columnar, compressed, preserves dtypes & dates → fast I/O for large frames. |

###  How code reads/writes
All paths are **environment-driven**; fallbacks work out-of-the-box.