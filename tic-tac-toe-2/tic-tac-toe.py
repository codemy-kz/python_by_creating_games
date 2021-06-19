import pygame
import sys
import random

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BOARD_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

LINE_WIDTH = 10

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")

FPS = 30
clock = pygame.time.Clock()

def draw_board():
    screen.fill(BOARD_COLOR)
    for x in range(1,3):
        pygame.draw.line(screen, (LINE_COLOR), (0, x*200), (SCREEN_WIDTH, x*200), LINE_WIDTH)    
        pygame.draw.line(screen, (LINE_COLOR), (x*200, 0), (x*200, SCREEN_HEIGHT), LINE_WIDTH)

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
