import pygame 
from random import randrange

RES = 800
SIZE = 50

x, y = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
directions = {"W": True, "S": True, "A": True, "D": True,}
length = 1
snake = [{x, y}]
dx, dy = 0, 0
FPS = 10
score = 0
level = 1
count = 0

pygame.init()
screen = pygame.display.set_mode([RES, RES])
clock = pygame.time.Clock()
font_score = pygame.font.SysFont("Arial", 26, bold=True)
font_gameover = pygame.font.SysFont("Arial", 66, bold=True)

# restart
def restart_game():
    global x, y, apple, directions, length, snake, dx, dy, FPS, score
    x, y = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
    apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
    directions = {"W": True, "S": True, "A": True, "D": True}
    length = 1
    snake = [{x, y}]
    dx, dy = 0, 0
    FPS = 10
    score = 0
    level = 1
    count = 0

    while True:
        screen.fill(pygame.Color("black"))
    # drawing snake
        [(pygame.draw.rect(screen, pygame.Color("green"), (i, j, SIZE - 2, SIZE - 2))) for i, j in snake]
        pygame.draw.rect(screen, pygame.Color("red"), (*apple, SIZE, SIZE))
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
                            restart_game()
                

    
                

        pygame.display.flip()
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

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
    
    

restart_game()