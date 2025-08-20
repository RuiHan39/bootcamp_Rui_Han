import pandas as pd

def get_summary_stats(df: pd.DataFrame) -> pd.DataFrame:
    desc = df.describe().T
    desc["count_null"] = df.isna().sum()
    return desc
