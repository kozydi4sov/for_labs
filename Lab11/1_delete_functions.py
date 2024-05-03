import psycopg2 
from config import load_config

def delete_func():
    
    """Create functions in the PostgreSQL database"""
    commands = (
        """
        DROP FUNCTION IF EXISTS search_phonebook(character varying);
        """
    )
    
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                # execute the CREATE FUNCTION statement
                for command in commands:
                    cur.execute(commands)
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)