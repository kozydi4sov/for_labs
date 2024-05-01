import psycopg2

fullname = input("Fullname: ")
phone_number = input("Phone Number: ")

conn = psycopg2.connect(
    host="localhost", 
    dbname="Lab10", 
    user="postgres", 
    password="2305"
    )

cur = conn.cursor()
conn.set_session(autocommit=True)

cur.execute("""CREATE TABLE if not exists phonebook (
            fullname VARCHAR(255),
            phone_number VARCHAR(20)
);
""")

cur.execute(f"""INSERT INTO phonebook (fullname, phone_number) VALUES
            ('{fullname}', '{phone_number}');""")

conn.commit()