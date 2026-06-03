from pathlib import Path

import pandas as pd

from src.transform.sales_transform import transform_sales_data
from src.validation.sales_validation import validate_sales_data
from src.data.sales_data import (
    load_sales_data,
    save_processed_sales_data,
)


def test_load_sample_csv(sample_sales_csv_path: Path) -> None:

    sales_df = load_sales_data(sample_sales_csv_path)

    assert list(sales_df.columns) == ["product","quantity","revenue"]
    assert len(sales_df) == 4
    assert sales_df["quantity"].sum() == 110
    assert sales_df["revenue"].sum() == 400.00

def test_transform_and_validate_sample_csv(sample_sales_csv_path: Path) -> None:

    raw_sales_df = pd.read_csv(sample_sales_csv_path)
    transformed_sales_df = transform_sales_data(raw_sales_df)
    validation_errors = validate_sales_data(transformed_sales_df)

    assert validation_errors == []
    assert "unit_price" in transformed_sales_df.columns
    assert transformed_sales_df["unit_price"].tolist() == [5.0, 2.0, 10.0, 1.5]

def test_save_and_reload_processed_sample_csv(
        sample_sales_csv_path: Path,
        tmp_path: Path,
) -> None:
    processed_csv_path = tmp_path / "sales_data_processed.csv"

    raw_sales_df = load_sales_data(sample_sales_csv_path)

    transformed_sales_df = transform_sales_data(raw_sales_df)
    
    validation_errors = validate_sales_data(
        transformed_sales_df
    )

    save_processed_sales_data(
        transformed_sales_df,
        processed_csv_path,
    )

    reloaded_sales_df = load_sales_data(
        processed_csv_path,
    )

    assert validation_errors == []
    
    assert processed_csv_path.exists()

    assert list(reloaded_sales_df.columns) == [
        "product",
        "quantity",
        "revenue",
        "unit_price",
    ]

    assert len(reloaded_sales_df) == 4
    
    assert reloaded_sales_df["revenue"].sum() == 400.0

    assert reloaded_sales_df["unit_price"].sum() == 18.5