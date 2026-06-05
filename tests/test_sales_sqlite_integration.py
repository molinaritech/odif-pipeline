from src.db.connection import get_connection
from src.db.load_dataframe import load_dataframe_to_table

import pandas as pd
import sqlite3

TABLE_NAME = "processed_sales"


def create_processed_sales_test_table(
        tmp_path,
) -> sqlite3.Connection:
    db_path = tmp_path / "test_odif.db"

    processed_sales_df = pd.DataFrame(
        {
            "product": ["Notebook", "Sticker", "Mug", "Pen"],
            "quantity": [25, 40, 15, 30],
            "revenue": [125.00, 80.00, 150.00, 45.00],
            "unit_price": [5.00, 2.00, 10.00, 1.50],
        }
    )

    connection = get_connection(db_path)

    load_dataframe_to_table(
        processed_sales_df,
        TABLE_NAME,
        connection,
    )

    return connection


def test_processed_sales_data_loads_to_sqlite_table(tmp_path) -> None:
    db_path = tmp_path / "test_odif.db"

    connection = create_processed_sales_test_table(tmp_path)

    row_count = connection.execute(
        f"SELECT COUNT(*) FROM {TABLE_NAME}"
    ).fetchone()[0]

    total_revenue = connection.execute(
        f"SELECT SUM(revenue) FROM {TABLE_NAME}"
    ).fetchone()[0]

    connection.close()

    assert row_count == 4
    assert total_revenue == 400.00


def test_highest_revenue_product_query(tmp_path) -> None:
    db_path = tmp_path / "test_odif.db"

    connection = create_processed_sales_test_table(tmp_path)

    result = connection.execute(
        f"""
        SELECT product, revenue
        FROM {TABLE_NAME}
        ORDER BY revenue DESC
        LIMIT 1
        """
    ).fetchone()

    connection.close()

    assert result[0] == "Mug"
    assert result[1] == 150.00


def test_total_revenue_query(tmp_path) -> None:
    db_path = tmp_path / "test_odif.db"

    connection = create_processed_sales_test_table(tmp_path)

    result = connection.execute(
        f"""
        SELECT SUM(revenue) AS total_revenue
        FROM {TABLE_NAME}
        """
    )