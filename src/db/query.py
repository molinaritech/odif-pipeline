import sqlite3

import pandas as pd

def query_to_dataframe(
        sql_query: str,
        connection: sqlite3.Connection,
) -> pd.DataFrame:
    return pd.read_sql_query(sql_query, connection)