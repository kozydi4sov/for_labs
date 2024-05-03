import psycopg2
from config import load_config

def create_insert_or_update_user_procedure():
    """Create insert_or_update_user procedure in the PostgreSQL database"""
    command = """
    CREATE OR REPLACE PROCEDURE insert_or_update_user(IN new_name VARCHAR, IN new_phone VARCHAR)
    LANGUAGE plpgsql
    AS $$
    BEGIN
    -- Проверяем, существует ли пользователь с заданным именем
    IF EXISTS (SELECT 1 FROM phonebook WHERE fullname = new_name) THEN
    -- Если пользователь существует, обновляем его номер телефона
    UPDATE phonebook SET phone_number = new_phone WHERE fullname = new_name;
    RAISE NOTICE 'Phone number updated for user %', new_name;
    ELSE
    -- Если пользователь не существует, вставляем новую запись
    INSERT INTO phonebook (fullname, phone_number) VALUES (new_name, new_phone);
    RAISE NOTICE 'New user % inserted with phone number %', new_name, new_phone;
    END IF;
    END;
    $$;
    """
    
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(command)
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

if __name__ == '__main__':
    create_insert_or_update_user_procedure()