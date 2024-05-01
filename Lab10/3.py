import psycopg2
import time
conn = psycopg2.connect(
    host="localhost",
    dbname="Lab10",
    user="postgres",
    password="2305"
)

cur = conn.cursor()
conn.set_session(autocommit=True)

cur.execute("""UPDATE phonebook
               SET fullname = 'Abishkenova Akerke'
               WHERE fullname = 'Ilyas Azamat' 
            """)
conn.commit()

time.sleep(5)


cur.execute("""UPDATE phonebook
               SET fullname = 'Ilyas Azamat'
               WHERE fullname = 'Abishkenova Akerke' 
            """)
conn.commit()
