import pandas as pd
import sqlite3

from src.db.connection import get_connection
from src.db.load_dataframe import load_dataframe_to_table
from src.db.query import query_to_dataframe
from pathlib import Path
from src.db.business_queries import (
    get_revenue_by_product,
    get_total_revenue,
    get_product_revenue_ranking,
    get_top_product_by_revenue,
    get_total_quantity_sold,
    get_quantity_by_product,
    get_product_revenue_share,
)

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


def test_query_to_dataframe_returns_sql_results(
        tmp_path: Path
) -> None:
    connection = create_processed_sales_test_table(tmp_path)

    result_df = query_to_dataframe(
        """
        SELECT
            product,
            revenue
        FROM processed_sales
        ORDER BY revenue DESC
        """,
        connection,
    )

    assert len(result_df) == 4
    assert result_df.iloc[0]["product"] == "Mug"
    assert result_df.iloc[0]["revenue"] == 150.00

    connection.close()


def test_get_revenue_by_product_returns_expected_results(
        tmp_path: Path
) -> None:
    connection = create_processed_sales_test_table(tmp_path)

    result_df = get_revenue_by_product(connection)

    assert len(result_df) == 4
    
    assert result_df.iloc[0]["product"] == "Mug"
    assert result_df.iloc[0]["total_revenue"] == 150.00

    connection.close()


def test_get_total_revenue_returns_expected_result(
        tmp_path: Path
) -> None:
    connection = create_processed_sales_test_table(tmp_path)

    result_df = get_total_revenue(connection)

    assert len(result_df) == 1
    assert result_df.iloc[0]["total_revenue"] == 400.00

    connection.close()


def test_get_product_revenue_ranking_returns_expected_results(
        tmp_path: Path
) -> None:
    connection = create_processed_sales_test_table(tmp_path)

    result_df = get_product_revenue_ranking(connection)

    assert len(result_df) == 4

    assert result_df.iloc[0]["product"] == "Mug"
    assert result_df.iloc[0]["revenue"] == 150.00
    assert result_df.iloc[0]["revenue_rank"] == 1

    connection.close()


def test_get_top_product_by_revenue_returns_expected_result(
        tmp_path: Path
) -> None:
    connection = create_processed_sales_test_table(tmp_path)

    result_df = get_top_product_by_revenue(connection)

    assert len(result_df) == 1

    assert result_df.iloc[0]["product"] == "Mug"
    assert result_df.iloc[0]["revenue"] == 150.00

    connection.close()


def test_get_total_quantity_sold_returns_expected_result(
        tmp_path: Path
) -> None:
    connection = create_processed_sales_test_table(tmp_path)

    result_df = get_total_quantity_sold(connection)

    assert len(result_df) == 1
    assert result_df.iloc[0]["total_quantity"] == 110

    connection.close()


def test_get_quantity_by_product_returns_expected_results(
        tmp_path: Path
) -> None:
    connection = create_processed_sales_test_table(tmp_path)

    result_df = get_quantity_by_product(connection)

    assert len(result_df) == 4

    assert result_df.iloc[0]["product"] == "Sticker"
    assert result_df.iloc[0]["total_quantity"] == 40

    connection.close()


def test_get_product_revenue_share_returns_expected_results(
        tmp_path: Path
) -> None:
    connection = create_processed_sales_test_table(tmp_path)

    result_df = get_product_revenue_share(connection)

    assert len(result_df) == 4

    assert result_df.iloc[0]["product"] == "Mug"
    assert result_df.iloc[0]["revenue"] == 150.00
    assert result_df.iloc[0]["revenue_share_pct"] == 37.50

    connection.close()