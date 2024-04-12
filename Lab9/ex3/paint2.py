import pygame
import sys
import math
pygame.init()

WIDTH = 960
HEIGHT = 640

screen = pygame.display.set_mode((WIDTH,HEIGHT))
base_layer = pygame.Surface((WIDTH,HEIGHT))

lastik = False
LMBpressed = False
rectangle = False
circle = False
square = False
triangle = False
diamond = False
equal_triangle = False
romb = False

prevx = 0
prevy = 0
currx = 0
curry = 0

# rectangle 
def calculate_rect(x1,y1,x2,y2):
    return pygame.Rect(min(x1,x2),min(y1,y2),abs(x1-x2),abs(y1-y2))

# circle
def calculate_circle(x1,y1,x2,y2):
     radius =  int(math.sqrt((x2-x1)**2 + (y2-y1)**2))
     return radius

# eraser
def calculate_lastik(x1,y1,x2,y2):
      return pygame.Rect(min(x1,x2),min(y1,y2),abs(x1-x2),abs(y1-y2))

# square
def calculate_square(x1, y1, x2, y2):
    size = max(abs(x2 - x1), abs(y2 - y1))
    return pygame.Rect(min(x1,x2),min(y1,y2), size, size)

# right triangle
def calculate_right_triangle(x1,y1,x2,y2):
    sol_zhak = [x1,y1]
    on_zhak = [x2,y2]
    asty = [x1,y2]
    points = [sol_zhak,on_zhak,asty]
    return points

# equilateral_triangle
def calculate_equilateral_triangle(x1,y1,x2,y2):
    sol_zhak = [x1,y1]
    on_zhak = [x1-(x2-x1),y1+(x2-x1)*math.sqrt(3)]
    asty = [x2,y1+(x2-x1)*math.sqrt(3),]
    points = [sol_zhak,on_zhak,asty]
    return points

# rhombus
def calculate_romb(x1, y1, x2, y2):
    sol_zhak = [x1,y1]
    on_zhak = [x2,y2]
    x = (x1 + x2) / 2
    y = (y1 + y2) / 2
    diagonal = ((x2 - x1)**2 + (y2 - y1)**2)**0.5 / 2
    asty = [x -diagonal, y]
    en_asty = [x + diagonal, y]
    points = [sol_zhak, asty, on_zhak, en_asty]
    return points

# main
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        # mouse position when clicking
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            LMBpressed = True

            # first mouse coordinates when clicking
            prevx = event.pos[0]
            prevy = event.pos[1]

        if LMBpressed:
                
                # second mouse coordinates when clicking
                currx = event.pos[0]
                curry = event.pos[1]

        if event.type == pygame.KEYDOWN:
            # eraser
            if event.key == pygame.K_e:
                lastik = True
                rectangle = False
                circle = False
                square = False
                triangle = False
                diamond = False
                equal_triangle = False
                romb = False
            # rectangle
            if event.key == pygame.K_r:
                rectangle = True
                lastik = False
                circle = False
                square = False
                triangle = False
                diamond = False
                equal_triangle = False
                romb = False
            # circle
            if event.key == pygame.K_c:
                circle = True
                lastik = False
                rectangle = False
                square = False
                triangle = False
                diamond = False
                equal_triangle = False
                romb = False
            # square
            if event.key == pygame.K_s:
                square = True
                lastik = False
                rectangle = False
                circle = False
                triangle = False
                diamond = False
                equal_triangle = False
                romb = False
            # right triangle
            if event.key == pygame.K_t:
                triangle = True
                lastik = False
                rectangle = False
                circle = False
                square = False
                diamond = False
                equal_triangle = False
                romb = False
            # equilateral triangle
            if event.key == pygame.K_u:
                equal_triangle=True
                lastik = False
                LMBpressed = False
                rectangle = False
                circle = False
                square = False
                triangle = False
                diamond = False
                romb = False
            # rhombus
            if event.key ==pygame.K_1:
                romb= True
                lastik = False
                LMBpressed = False
                rectangle = False
                circle = False
                square = False
                triangle = False
                diamond = False
                equal_triangle = False
            
        # mouse position when releasing
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            LMBpressed = False
            if lastik:
                pygame.draw.rect(screen,"black",calculate_lastik(prevx,prevy,currx,curry))
            if rectangle:
                pygame.draw.rect(screen,"white",calculate_rect(prevx,prevy,currx,curry),2)
            if circle:
                radius = calculate_circle(prevx,prevy,currx,curry)
                pygame.draw.circle(screen,"white",(prevx,prevy),radius,2)
            if square:
                pygame.draw.rect(screen,"white",calculate_square(prevx,prevy,currx,curry),2)
            base_layer.blit(screen,(0,0))
            if triangle:
                points = calculate_right_triangle(prevx,prevy,currx,curry)
                pygame.draw.polygon(screen,"white",points,2)
            if equal_triangle:
                points = calculate_equilateral_triangle(prevx,prevy,currx,curry)
                pygame.draw.polygon(screen,"white",points,2)
            if romb:
                points = calculate_romb(prevx,prevy,currx,curry)
                pygame.draw.polygon(screen,"white",points,2)
            
    if LMBpressed:
        
        screen.blit(base_layer,(0,0))
        if lastik:
            pygame.draw.rect(screen,"yellow",calculate_lastik(prevx,prevy,currx,curry),2)
        if rectangle:
            pygame.draw.rect(screen,"white",calculate_rect(prevx,prevy,currx,curry),2)
        if circle:
            radius = calculate_circle(prevx,prevy,currx,curry)
            pygame.draw.circle(screen,"white",(prevx,prevy),radius,2)
        if square:
            pygame.draw.rect(screen,"white",calculate_square(prevx,prevy,currx,curry),2)
        if triangle:
                points = calculate_right_triangle(prevx,prevy,currx,curry)
                pygame.draw.polygon(screen,"white",points,2)
        if equal_triangle:
                points = calculate_equilateral_triangle(prevx,prevy,currx,curry)
                pygame.draw.polygon(screen,"white",points,2)
        if romb:
                points = calculate_romb(prevx,prevy,currx,curry)
                pygame.draw.polygon(screen,"white",points,2)
    pygame.display.flip()