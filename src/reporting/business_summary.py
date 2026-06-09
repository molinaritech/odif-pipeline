from pathlib import Path
from src.db.business_queries import get_revenue_by_product

import pandas as pd
import sqlite3


def save_business_summary_report(
        summary_df: pd.DataFrame,
        output_path: Path,
)-> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)

    summary_df.to_csv(output_path, index=False)


def generate_revenue_by_product_report(
        connection: sqlite3.Connection,
) -> pd.DataFrame:
    return get_revenue_by_product(connection)