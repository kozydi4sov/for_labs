import pygame
import psycopg2
from pygame.locals import *
from random import randrange

# Функция для запроса имени пользователя
def get_username(screen):
    username = ""
    font = pygame.font.Font(None, 36)
    input_box = pygame.Rect(100, 200, 140, 32)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    input_text = font.render('Enter your name:', True, (255, 255, 255))

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return
            if event.type == KEYDOWN:
                if active:
                    if event.key == K_RETURN:
                        return username
                    elif event.key == K_BACKSPACE:
                        username = username[:-1]
                    else:
                        username += event.unicode
                if event.key == K_TAB:
                    active = not active
                    color = color_active if active else color_inactive
            if event.type == MOUSEBUTTONDOWN:
                # Если пользователь кликает на поле ввода, активируем его
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive

        screen.fill((30, 30, 30))
        txt_surface = font.render(username, True, (255, 255, 255))
        width = max(200, txt_surface.get_width() + 10)
        input_box.w = width
        pygame.draw.rect(screen, color, input_box, 2)
        screen.blit(input_text, (input_box.x, input_box.y - 30))
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        pygame.display.flip()

# Функция для отображения диалогового окна выбора уровня сложности
def show_difficulty_selection(screen):
    font = pygame.font.Font(None, 36)
    text_easy = font.render("Easy level", True, (255, 255, 255))
    text_hard = font.render("Hard level", True, (255, 255, 255))
    rect_easy = text_easy.get_rect(center=(RES // 2, RES // 2 - 50))
    rect_hard = text_hard.get_rect(center=(RES // 2, RES // 2 + 50))
    selected = None

    while True:
        screen.fill((30, 30, 30))
        screen.blit(text_easy, rect_easy)
        screen.blit(text_hard, rect_hard)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return
            if event.type == MOUSEBUTTONDOWN:
                if rect_easy.collidepoint(event.pos):
                    selected = "easy"
                elif rect_hard.collidepoint(event.pos):
                    selected = "hard"
            if selected:
                return selected
            
# Генерация координат для яблока, учитывая стены (если уровень сложности "hard")
def generate_apple_position(wall_segments):
    while True:
        apple_pos = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
        if wall_segments is None or not any(pygame.Rect(*segment).collidepoint(apple_pos) for segment in wall_segments):
            return apple_pos
        
def pause():
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            paused = False

    pygame.display.update()
    clock.tick(15)

# Инициализация Pygame
pygame.init()
RES = 800
SIZE = 50
screen = pygame.display.set_mode([RES, RES])
clock = pygame.time.Clock()

# Вызываем функцию для выбора уровня сложности
difficulty = show_difficulty_selection(screen)

# Вызываем функцию для запроса имени пользователя
username = get_username(screen)

# Если пользователь закрывает окно без ввода имени, завершаем игру
if not username:
    pygame.quit()
    exit()

# Сохранение имени пользователя в базу данных PostgreSQL
# Подключение к вашей базе данных
conn = psycopg2.connect(
    host="localhost",
    dbname="Snake",
    user="postgres",
    password="2305"
)

# Создание курсора для выполнения SQL-запросов
cur = conn.cursor()

# Создание таблицы для хранения имен пользователей
cur.execute("""
    CREATE TABLE IF NOT EXISTS snake (
        user_name VARCHAR(255) PRIMARY KEY,
        user_score INT 
    )
""")

# Вставка или обновление данных пользователя в таблице
cur.execute("INSERT INTO snake (user_name, user_score, level) VALUES (%s, 0, %s) ON CONFLICT (user_name) DO UPDATE SET user_score = EXCLUDED.user_score, level = EXCLUDED.level", (username, difficulty))

# Подтверждение транзакции
conn.commit()

# Закрытие соединения
conn.close()

# Переменная для хранения счета пользователя
score = 0

RES = 800
SIZE = 50

pygame.init()
screen = pygame.display.set_mode([RES, RES])
clock = pygame.time.Clock()
font_score = pygame.font.SysFont("Arial", 26, bold=True)
font_gameover = pygame.font.SysFont("Arial", 66, bold=True)

# Функция для перезапуска игры
def restart_game(difficulty):
    global FPS
    if difficulty == "easy":
        FPS = 10
    elif difficulty == "hard":
        FPS = 15
    global x, y, apple, directions, length, snake, dx, dy, score
    x, y = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
    apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
    directions = {"W": True, "S": True, "A": True, "D": True}
    length = 1
    snake = [{x, y}]
    dx, dy = 0, 0
    score = 0
    level = 1
    count = 0

    second_apple = ()
    second_apple_timer = 0
    second_apple_interval = 4000
    second_apple_to_appear = 4000

    # Если уровень сложности "hard", добавляем стену
    if difficulty == "hard":
        wall_color = pygame.Color("blue")
        # Определяем координаты и размеры прямоугольников для создания буквы "Г"
        wall_segments = [
            (RES // 2 - SIZE * 2, RES // 2 - SIZE * 2, SIZE, SIZE * 5),  # Вертикальная часть буквы "Г"
            (RES // 2 - SIZE * 2, RES // 2 - SIZE * 2, SIZE * 4, SIZE),  # Горизонтальная часть буквы "Г"
        ]

    # Генерация позиции для первого яблока
    if difficulty == "easy":
        apple = generate_apple_position(None)
    else:
        apple = generate_apple_position(wall_segments)

    while True:
        screen.fill(pygame.Color("black"))
        # drawing snake
        [(pygame.draw.rect(screen, pygame.Color("green"), (i, j, SIZE - 2, SIZE - 2))) for i, j in snake]
        pygame.draw.rect(screen, pygame.Color("red"), (*apple, SIZE, SIZE))

        present_time = pygame.time.get_ticks()

        if present_time - second_apple_timer >= second_apple_to_appear:
            second_apple_timer = present_time
            second_apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)

        if second_apple:
            if present_time - second_apple_timer < second_apple_interval:
                pygame.draw.rect(screen, pygame.Color("yellow"), (*second_apple, SIZE + 7, SIZE + 7))
                if snake[-1] == second_apple:
                    length += 2
                    score += 2
                    count += 2
                    second_apple = ()

            else:
                second_apple = ()

        # Если уровень сложности "hard", отрисовываем стену
        if difficulty == "hard":
            for segment in wall_segments:
                pygame.draw.rect(screen, wall_color, segment)
        
        # show score
        render_score = font_score.render(f"SCORE: {count}", 1, pygame.Color("orange"))
        screen.blit(render_score, (5, 5))

        render_level = font_score.render(f"LEVEL: {level}", 1, pygame.Color("orange"))
        screen.blit(render_level, (680, 5))

        render_speed = font_score.render(f"SPEED: {FPS}", 1, pygame.Color("orange"))
        screen.blit(render_speed, (5, 30))

        # snake movement 
        x += dx * SIZE
        y += dy * SIZE
        snake.append((x, y))
        snake = snake[-length:]
        
        # eating apple
        if snake[-1] == apple:
            apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
            length += 1
            score += 1
            count += 1
        
        if score % 5 >= 0 and score > 4 :
            level += 1
            score = score - 5
            FPS += 1

        # game over 
        if x < 0 or x > RES - SIZE or y < 0 or y > RES - SIZE or len(snake) != len(set(snake)):
            while True:
                render_gameover = font_gameover.render("GAME OVER", 1, pygame.Color("white"))
                screen.blit(render_gameover, (RES // 2 - 200, RES // 3))
                pygame.display.flip()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            # Обновление счета в базе данных перед перезапуском игры
                            conn = psycopg2.connect(
                                host="localhost",
                                dbname="Snake",
                                user="postgres",
                                password="2305"
                            )
                            cur = conn.cursor()
                            cur.execute("UPDATE snake SET user_score = user_score + %s WHERE user_name = %s", (count, username))
                            conn.commit()
                            cur.close()
                            conn.close()
                            restart_game(difficulty)

        # Проверка столкновения с границами стены (если уровень сложности "hard")
        if difficulty == "hard":
            for segment in wall_segments:
                wall_rect = pygame.Rect(*segment)
                if wall_rect.collidepoint(snake[-1]):
                    while True:
                        render_gameover = font_gameover.render("GAME OVER", 1, pygame.Color("white"))
                        screen.blit(render_gameover, (RES // 2 - 200, RES // 3))
                        pygame.display.flip()
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                exit()
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_SPACE:
                                    # Обновление счета в базе данных перед перезапуском игры
                                    conn = psycopg2.connect(
                                        host="localhost",
                                        dbname="Snake",
                                        user="postgres",
                                        password="2305"
                                    )
                                    cur = conn.cursor()
                                    cur.execute("UPDATE snake SET user_score = user_score + %s WHERE user_name = %s", (count, username))
                                    conn.commit()
                                    cur.close()
                                    conn.close()
                                    restart_game(difficulty)

                
        pygame.display.flip()
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause()


        # control
        key = pygame.key.get_pressed()
        if key[pygame.K_w] and directions["W"]:
            dx, dy = 0, -1
            directions = {"W": True, "S": False, "A": True, "D": True,}
        if key[pygame.K_s] and directions["S"]:
            dx, dy = 0, 1
            directions = {"W": False, "S": True, "A": True, "D": True,}
        if key[pygame.K_a]and directions["A"]:
            dx, dy = -1, 0
            directions = {"W": True, "S": True, "A": True, "D": False,}
        if key[pygame.K_d]and directions["D"]:
            dx, dy = 1, 0
            directions = {"W": True, "S": True, "A": False, "D": True,}

# Запуск игры с выбранным уровнем сложности
restart_game(difficulty)