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
