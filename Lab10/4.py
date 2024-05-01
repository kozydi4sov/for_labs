#4

import psycopg2
conn = psycopg2.connect(
    host="localhost", 
    dbname="Lab10", 
    user="postgres", 
    password="2305"
    )

cur = conn.cursor()
conn.set_session(autocommit=True)

#SELECT SOMETHING 
cur.execute("""SELECT * FROM phonebook ORDER BY fullname DESC;""")
print(cur.fetchall())

cur.execute("""SELECT * FROM phonebook ORDER BY fullname;""")
print(cur.fetchall())

cur.execute("""SELECT * FROM phonebook WHERE fullname LIKE 'A%';""")
print(cur.fetchall())

conn.commit()