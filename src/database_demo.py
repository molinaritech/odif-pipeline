from src.config import QUERIES_FILE, SCHEMA_FILE
from src.db.connection import get_connection
from src.db.execute_sql import execute_sql_file


def main() -> None:
    
    with get_connection() as connection:
        execute_sql_file(connection, SCHEMA_FILE)
        execute_sql_file(connection, QUERIES_FILE)
    
    print("Database workflow completed successfully.")


if __name__ == "__main__":
    main()