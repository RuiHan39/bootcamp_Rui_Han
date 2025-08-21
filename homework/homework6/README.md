
## Cleaning Strategy

1. **Fill gaps** – numeric NaNs → column median.  
2. **Drop rows** – any remaining NaNs removed.  
3. **Normalize** – Min-Max to [0, 1].

Raw untouched in `data/raw/`; cleaned files saved in `data/processed/`.