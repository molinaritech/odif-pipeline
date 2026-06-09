from pathlib import Path
from src.db.business_queries import (
    get_revenue_by_product,
    get_top_product_by_revenue,
    get_total_quantity_sold,
    get_total_revenue,
)


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


def generate_business_summary(
        connection: sqlite3.Connection,
) -> pd.DataFrame:
    total_revenue_df = get_total_revenue(connection)
    total_quantity_sold_df = get_total_quantity_sold(connection)
    top_product_df = get_top_product_by_revenue(connection)
    
    summary_data = {
        "total_revenue": [total_revenue_df.iloc[0]["total_revenue"]],
        "total_quantity_sold": [total_quantity_sold_df.iloc[0]["total_quantity"]],
        "top_product": [top_product_df.iloc[0]["product"]],
    }

    return pd.DataFrame(summary_data)
