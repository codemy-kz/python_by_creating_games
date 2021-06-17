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

line_width = 6
def draw_board():
    screen.fill(BOARD_COLOR)
    for x in range(1,3):
        pygame.draw.line(screen, (BLACK), (0, x*100), (SCREEN_WIDTH, x*100), line_width)    
        pygame.draw.line(screen, (BLACK), (x*100, 0), (x*100, SCREEN_HEIGHT), line_width)

board = [
    [0, 0, 0], 
    [0, 0, 0], 
    [0, 0, 0]
]

flRunning = True

while flRunning:
    clock.tick(FPS)


    draw_board()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flRunning = False

    pygame.display.update()

pygame.quit()
