import psycopg2
from config import load_config

def call_insert_or_update_user_procedure():
    try:
        # Read database configuration(Подключение к базе данных)
        config = load_config()
        with psycopg2.connect(**config) as conn:
            # Connect to the PostgreSQL database( Получаем данные от пользователя)
            new_name = input("Enter the name: ")
            new_phone = input("Enter the phone number: ")
            
            with conn.cursor() as cur:
                # Execute the function call(Вызов процедуры с использованием ключевого слова CALL)
                cur.execute("CALL insert_or_update_user(%s, %s)", (new_name, new_phone))
                # Fetch all rows from the result set(Применение изменений к базе данных)
                conn.commit()
                print("Procedure executed successfully.")
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

if __name__ == "__main__":
    call_insert_or_update_user_procedure()