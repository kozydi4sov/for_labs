import psycopg2
conn = psycopg2.connect(
    host="localhost", 
    dbname="Lab10", 
    user="postgres", 
    password="2305"
    )

cur = conn.cursor()
conn.set_session(autocommit=True)

cur.execute("""DROP TABLE phonebook""")
conn.commit()