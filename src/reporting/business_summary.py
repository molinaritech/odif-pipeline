from pathlib import Path

import pandas as pd


def save_business_summary_report(
        summary_df: pd.DataFrame,
        output_path: Path,
)-> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)

    summary_df.to_csv(output_path, index=False)

