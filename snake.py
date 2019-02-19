import pygame
from pygame.locals import *
import numpy as np


pygame.init()
pygame.font.init()
pygame.display.init


pygame.display.set_caption("Snake")
screen = pygame.display.set_mode( ( 720, 480 ), pygame.DOUBLEBUF, 8 )
screen.set_colorkey(2)
clock = pygame.time.Clock()


snake_size = 1
speed = snake_size * 2
Snake_Color = (255,255,250)
treat_color = (63,110,186)
treat_count = 0
GoingRight = True
GoingLeft = False
GoingUp = False
GoingDown = False
x = 20
y = 20
snake = [(x,y), (x,y)]
def snake_movement(snake, treat_count):
    last_snake = snake[0]

    pygame.draw.circle(screen, (0), (last_snake[0],last_snake[1]), snake_size)
    pygame.display.update()
    del snake[0]
def treat(treat_count):
        snake.insert(0,(x,y))
        treat_count += 1
        treat.x_treat = np.random.randint(3,720 / snake_size / 3) * 30
        treat.y_treat = np.random.randint(3,480 / snake_size / 3) * 30
        pygame.draw.circle(screen,treat_color, (treat.x_treat,treat.y_treat), snake_size)
def texts(score):
    fonttype =pygame.font.get_fonts()[15]
    #print (fonttype)
    font=pygame.font.SysFont(fonttype,130)
    print ("Your score is: ", score)
    scoretext=font.render("Score:"+str(score), 5,(155,105,255))
    screen.blit(scoretext, (720/3, 480/2))
    pygame.display.update()
    pygame.time.wait(3000)
def GameOver():
    texts(len(snake)-3)
    pygame.quit()
    exit()
def crash(snake, x, y):
    for i in snake[0:len(snake)-1]:
        snake_x = i[0]
        snake_y = i[1]
        if snake_x == x and snake_y == y:
            GameOver()
            print("game over")

while(True):
    for event in pygame.event.get():
        treat(treat_count)
        for i in range(10000):
            if ((x > 720) or (x < 0) or (y > 480) or (y < 0)):
                GameOver()
            if x in range(treat.x_treat - snake_size*2, treat.x_treat + snake_size*2) and y in range(treat.y_treat - snake_size*2, treat.y_treat + snake_size*2):
                pygame.draw.circle(screen, (0), (treat.x_treat, treat.y_treat), snake_size)
                treat(treat_count)
            pygame.display.flip()
            #pygame.display.update()
            pygame.event.pump()
            keys = pygame.key.get_pressed()
            if ((keys[K_RIGHT]) or GoingRight) and not GoingLeft:
                GoingRight = True
                GoingLeft = False
                GoingUp = False
                GoingDown = False
                x = x + speed
            if ((keys[K_LEFT]) or GoingLeft) and not GoingRight:
                GoingRight = False
                GoingLeft = True
                GoingUp = False
                GoingDown = False
                x = x - speed
            if ((keys[K_UP]) or GoingUp) and not GoingDown:
                GoingRight = False
                GoingLeft = False
                GoingUp = True
                GoingDown = False
                y = y - speed
            if ((keys[K_DOWN]) or GoingDown) and not GoingUp:
                GoingRight = False
                GoingLeft = False
                GoingUp = False
                GoingDown = True
                y = y + speed
            snake.append((x,y))
            snake_movement(snake,treat_count)
            pygame.draw.circle(screen,Snake_Color, (x,y), snake_size)
            crash(snake,x,y)
            pygame.event.pump()
            clock.tick(15)
