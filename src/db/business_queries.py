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


def get_product_revenue_ranking(
        connection: sqlite3.Connection,
) -> pd.DataFrame:
    return query_to_dataframe(
        """
        SELECT
            product,
            revenue,
            RANK() OVER (
                ORDER BY revenue DESC
            ) AS revenue_rank
        FROM processed_sales
        ORDER BY revenue_rank
        """,
        connection,
    )


def get_top_product_by_revenue(
        connection: sqlite3.Connection,
) -> pd.DataFrame:
    return query_to_dataframe(
        """
        SELECT
            product,
            revenue
        FROM processed_sales
        ORDER BY revenue DESC
        LIMIT 1
        """,
        connection,
    )


def get_total_quantity_sold(
        connection: sqlite3.Connection,
) -> pd.DataFrame:
    return query_to_dataframe(
        """
        SELECT
            SUM(quantity) AS total_quantity
        FROM processed_sales
        """,
        connection,
    )


def get_quantity_by_product(
        connection: sqlite3.Connection,
) -> pd.DataFrame:
    return query_to_dataframe(
        """
        SELECT
            product,
            SUM(quantity) AS total_quantity
        FROM processed_sales
        GROUP BY product
        ORDER BY total_quantity DESC
        """,
        connection,
    )


def get_product_revenue_share(
        connection: sqlite3.Connection,
) -> pd.DataFrame:
    return query_to_dataframe(
        """
        SELECT
            product,
            revenue,
            ROUND(
                (revenue* 100.0) /
                (SUM(revenue) OVER ()),
                2
            ) AS revenue_share_pct
        FROM processed_sales
        ORDER BY revenue_share_pct DESC
        """,
        connection,
    )