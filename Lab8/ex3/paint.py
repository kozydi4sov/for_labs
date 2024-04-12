import pygame
import math

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

base_layer = pygame.Surface((WIDTH, HEIGHT))

clock = pygame.time.Clock()

LMBpressed = False

prevX = 0
prevY = 0
currX = 0
currY = 0

rectangle = False
circle = False
eraser = False

# Function for defining a rectangle
def det_rectangle(x1, y1, x2, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))

# Function for defining a circle
def det_circle(x1, y1, x2, y2):
     radius =  int(math.sqrt((x2-x1)**2 + (y2-y1)**2))
     return radius

# Function for defining a eraser
def det_easer(x1, y1, x2, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))

while True:
    
    for event in pygame.event.get():
        if LMBpressed:
            screen.blit(base_layer, (0, 0))
        if event.type == pygame.QUIT:
            exit()

        # mouse position when clicking
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            LMBpressed = True

            # first mouse coordinates when clicking
            prevX = event.pos[0]
            prevY = event.pos[1]

        if LMBpressed:
            # second mouse coordinates when clicking
            currX = event.pos[0]
            currY = event.pos[1]

        # to bind the buttons
        if event.type == pygame.KEYDOWN:

            # rectangle
            if event.key == pygame.K_r:
                rectangle = True
                circle = False
                eraser = False
            
            # circle
            if event.key == pygame.K_c:
                rectangle = False
                circle = True
                eraser = False

            # eraser
            if event.key == pygame.K_e:
                rectangle = False
                circle = False
                eraser = True
        
        # mouse position when releasing
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:

            LMBpressed = False

            if rectangle:
                pygame.draw.rect(screen, "pink", det_rectangle(prevX, prevY, currX, currY), 3)

            if circle:
                radius = det_circle(prevX, prevY, currX, currY)
                pygame.draw.circle(screen, "pink", (prevX,prevY), radius, 3)

            if eraser:
                pygame.draw.rect(screen, "black", (prevX, prevY, currX, currY))
            
            base_layer.blit(screen,(0,0))

    if LMBpressed:

        screen.blit(base_layer,(0,0))

        if rectangle:
            pygame.draw.rect(screen, "pink", det_rectangle(prevX, prevY, currX, currY), 3)

        if circle:
            radius = det_circle(prevX, prevY, currX, currY)
            pygame.draw.circle(screen, "pink", (prevX, prevY), radius, 3)

        if eraser:
            pygame.draw.rect(screen, "green", det_easer(prevX, prevY, currX, currY), 3)

    pygame.display.flip()
    clock.tick(60)