import pandas as pd
import pytest

from pathlib import Path

@pytest.fixture
def valid_sales_df() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "product": ["Widget A"],
            "quantity": [10],
            "revenue": [100.0],
        }
    )

@pytest.fixture
def sample_sales_csv_path() -> Path:
    return Path("data/sample/sales_data_sample.csv")


@pytest.fixture
def processed_sales_df() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "product": ["Notebook", "Sticker", "Mug", "Pen"],
            "quantity": [25, 40, 15, 30],
            "revenue": [125.00, 80.00, 150.00, 45.00],
            "unit_price": [5.00, 2.00, 10.00, 1.50],
        }
    )