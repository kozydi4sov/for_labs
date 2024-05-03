import psycopg2 
from config import load_config

def drop_func():
    """Drop the search_phonebook function if it exists"""
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("DROP FUNCTION IF EXISTS search_phonebook(VARCHAR)")
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

if __name__ == "__main__":
    drop_func()