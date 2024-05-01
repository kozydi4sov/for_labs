import psycopg2
conn = psycopg2.connect(
    host="localhost", 
    dbname="Lab10", 
    user="postgres", 
    password="2305"
    )

cur = conn.cursor()
conn.set_session(autocommit=True)

fullname = input("The name you want to remove: ")

cur.execute(f"""DELETE FROM phonebook WHERE fullname = '{fullname}'
""")

conn.commit()