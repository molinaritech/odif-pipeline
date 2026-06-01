import pandas as pd
import pytest


@pytest.fixture
def valid_sales_df() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "product": ["Widget A"],
            "quantity": [10],
            "revenue": [100.0],
        }
    )