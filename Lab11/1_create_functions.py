import psycopg2 
from config import load_config

def create_func():
    
    """Create functions in the PostgreSQL database"""
    commands = (
        """
        CREATE OR REPLACE FUNCTION search_phonebook(spisok VARCHAR)
        RETURNS TABLE(fullname VARCHAR, phone_number VARCHAR) AS
        $$
        BEGIN
        RETURN QUERY
        SELECT phonebook.fullname, phonebook.phone_number
        FROM phonebook
        WHERE phonebook.fullname ILIKE '%' || spisok || '%';
        END;
        $$
        LANGUAGE plpgsql;
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

if __name__ == '__main__':
    create_func()
