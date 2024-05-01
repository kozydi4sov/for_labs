import psycopg2
import csv
conn = psycopg2.connect(
    host="localhost", 
    dbname="Lab10", 
    user="postgres", 
    password="2305"
    )

cur = conn.cursor()
conn.set_session(autocommit=True)

cur.execute("""CREATE TABLE phonebook (
            fullname VARCHAR(255),
            phone_number VARCHAR(20)
);
""")

filename = 'Lab10/phonebook.csv'
with open (filename, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
            
        fullname, phone_number = row

        #INSERT SOMETHING INTO TABLE
        cur.execute(f"""INSERT INTO phonebook (fullname, phone_number) VALUES
                    ('{fullname}', '{phone_number}'); """)

        conn.commit()