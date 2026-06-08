import sqlite3
import pandas as pd

from src.db.query import query_to_dataframe


def get_revenue_by_product(
        connection: sqlite3.Connection,
) -> pd.DataFrame:
    return query_to_dataframe(
        """
        SELECT
            product,
            SUM(revenue) AS total_revenue
        FROM processed_sales
        GROUP BY product
        ORDER BY total_revenue DESC
        """,
        connection,
    )


def get_total_revenue(
        connection: sqlite3.Connection,
) -> pd.DataFrame:
    return query_to_dataframe(
        """
        SELECT
            SUM(revenue) AS total_revenue
        FROM processed_sales
        """,
        connection,
    )