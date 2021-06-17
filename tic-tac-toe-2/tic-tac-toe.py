import pygame
from pygame.locals import *
import random

SCREEN_WIDTH = 300
SCREEN_HEIGHT = 300

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BOARD_COLOR = (255, 255, 200)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")

FPS = 30
clock = pygame.time.Clock()

# айнымалылар
line_width = 6
board = [
    [0, 0, 0], 
    [0, 0, 0], 
    [0, 0, 0]
]

flRunning = True
clicked = False
pos = []
player = 1

def draw_grid():
    screen.fill(BOARD_COLOR)
    for x in range(1,3):
        pygame.draw.line(screen, (BLACK), (0, x*100), (SCREEN_WIDTH, x*100), line_width)    
        pygame.draw.line(screen, (BLACK), (x*100, 0), (x*100, SCREEN_HEIGHT), line_width)

def draw_board():
    x_pos = 0
    for x in board:
        y_pos = 0
        for y in x:
            if y == 1:
                pygame.draw.line(screen, (GREEN), (x_pos*100+15, y_pos*100+15), (x_pos*100+85, y_pos*100+85), line_width)
                pygame.draw.line(screen, (GREEN), (x_pos*100+15, y_pos*100+85), (x_pos*100+85, y_pos*100+15), line_width)
            if y == -1:
                pygame.draw.circle(screen, (RED), (x_pos*100 + 50, y_pos*100 + 50), 38, line_width)
            y_pos += 1
        x_pos += 1

while flRunning:
    clock.tick(FPS)


    draw_grid()
    draw_board()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flRunning = False
        if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
            clicked = True
            pos = pygame.mouse.get_pos()
            cell_x = pos[0] 
            cell_y = pos[1] 
            if board[cell_x // 100][cell_y // 100] == 0:
                 board[cell_x // 100][cell_y // 100] = player
                 player *= -1

        if event.type == pygame.MOUSEBUTTONUP and clicked == True:
            clicked = False
            

    pygame.display.update()

pygame.quit()
