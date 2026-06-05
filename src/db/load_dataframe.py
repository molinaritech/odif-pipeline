import sqlite3

import pandas as pd


def load_dataframe_to_table(
        dataFrame: pd.DataFrame,
        table_name: str,
        connection: sqlite3.Connection,
) -> None:
    dataFrame.to_sql(
        table_name,
        connection,
        if_exists="replace",
        index=False,
    )