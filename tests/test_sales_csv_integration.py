from pathlib import Path

import pandas as pd

from src.transform.sales_transform import transform_sales_data
from src.validation.sales_validation import validate_sales_data


def test_load_sample_csv() -> None:
    sample_csv_path = Path("data/sample/sales_data_sample.csv")

    sales_df = pd.read_csv(sample_csv_path)

    assert list(sales_df.columns) == ["product","quantity","revenue"]
    assert len(sales_df) == 4
    assert sales_df["quantity"].sum() == 110
    assert sales_df["revenue"].sum() == 400.00

def test_transform_and_validate_sample_csv() -> None:
    sample_csv_path = Path("data/sample/sales_data_sample.csv")

    raw_sales_df = pd.read_csv(sample_csv_path)
    transformed_sales_df = transform_sales_data(raw_sales_df)
    validation_errors = validate_sales_data(transformed_sales_df)

    assert validation_errors == []
    assert "unit_price" in transformed_sales_df.columns
    assert transformed_sales_df["unit_price"].tolist() == [5.0, 2.0, 10.0, 1.5]