from pathlib import Path
import sqlite3

def execute_sql_file(
        connection: sqlite3.Connection,
        sql_file_path: str | Path
) -> None:
    
    sql_path = Path(sql_file_path)

    with sql_path.open("r", encoding="utf-8") as file:
        sql_script = file.read()

    connection.executescript(sql_script)

    connection.commit()