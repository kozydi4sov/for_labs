import psycopg2
from config import load_config

def create_delete_user_data_procedure():
    """Create delete_user_data procedure in the PostgreSQL database"""
    command = """
    CREATE OR REPLACE PROCEDURE delete_user_data(IN delete_criteria VARCHAR)
    LANGUAGE plpgsql
    AS $$
    BEGIN
    -- Проверяем, является ли критерий удаления именем пользователя или номером телефона
    IF EXISTS (SELECT 1 FROM phonebook WHERE fullname = delete_criteria) THEN
    -- Удаляем записи по имени пользователя
    DELETE FROM phonebook WHERE fullname = delete_criteria;
    ELSIF EXISTS (SELECT 1 FROM phonebook WHERE phone_number = delete_criteria) THEN
    -- Удаляем записи по номеру телефона
    DELETE FROM phonebook WHERE phone_number = delete_criteria;
    ELSE
    -- Если ни по имени, ни по номеру телефона не найдено записей, выводим сообщение об ошибке
    RAISE EXCEPTION 'No records found for the given criteria: %', delete_criteria;
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
    create_delete_user_data_procedure()