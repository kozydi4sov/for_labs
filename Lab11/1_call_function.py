import psycopg2
from config import load_config

def call_search_phonebook(spisok):
    """Call the search_phonebook function"""
    try:
        # read database configuration
        config = load_config()
        # connect to the PostgreSQL database
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                # execute the function call
                cur.execute("SELECT * FROM search_phonebook(%s)", (spisok,))
                # fetch all rows from the result set
                results = cur.fetchall()
                return results
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

if __name__ == '__main__':
    spisok = ""  # Пустой образец (шаблон)
    results = call_search_phonebook(spisok)
    if results:
        print("Search results:")
        for row in results:
            print(row)
    else:
        print("No results found.")