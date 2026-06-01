import pandas as pd

from src.data.sales_data import save_processed_sales_data


def test_save_processed_sales_data_creates_file(tmp_path) -> None:
    sales_df = pd.DataFrame(
        {
            "product": ["Widget A"],
            "quantity": [10],
            "revenue": [100.0],
            "unit_price": [10.0],
        }
    )
    
    output_file = tmp_path / "sales_data_processed.csv"
    
    save_processed_sales_data(sales_df, output_file)

    assert output_file.exists()