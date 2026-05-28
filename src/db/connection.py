from pathlib import Path
import sqlite3

from src.config import DB_PATH

def get_connection(db_path: Path = DB_PATH) -> sqlite3.Connection:
    db_path.parent.mkdir(parents=True, exist_ok=True)

    return sqlite3.connect(db_path)