import pygame
from pygame.locals import *
import random

SCREEN_WIDTH = 300
SCREEN_HEIGHT = 300


pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")

FPS = 30
clock = pygame.time.Clock()

flRunning = True

while flRunning:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flRunning = False

    pygame.display.update()

pygame.quit()
