import pygame
import sys
import random
import numpy as np

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BOARD_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

LINE_WIDTH = 10
BOARD_ROWS = 3
BOARD_COLS = 3
CIRCLE_WIDTH = 15
CIRCLE_RADIUS = 60
CROSS_WIDTH =25
SPACE = 30

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

board = np.zeros((BOARD_ROWS, BOARD_COLS))

def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:
                pygame.draw.circle(screen, CIRCLE_COLOR, (int(col*200 + 200/2), int(row*200+200/2)), CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board[row][col] == 2:
                pygame.draw.line(screen,CROSS_COLOR, (int(col*200+SPACE), int(row*200+SPACE)), (int(col*200+200-SPACE), int(row*200+200-SPACE)), CROSS_WIDTH)
                pygame.draw.line(screen,CROSS_COLOR, (int(col*200+200-SPACE), int(row*200+SPACE)), (int(col*200+SPACE), int(row*200+200-SPACE)), CROSS_WIDTH)

def mark_square(row, col, player):
    board[row][col] = player

def available_square(row, col):
    return board[row][col] == 0

def is_board_full():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 0:
                return False
    return True
    




flRunning = True

player = random.choice([1, 2])

while flRunning:
    clock.tick(FPS)


    draw_board()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flRunning = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseX = event.pos[0]
            mouseY = event.pos[1]
            
            clicked_row = mouseY // 200
            clicked_col = mouseX // 200
            # print(clicked_row, clicked_col)

            if available_square(clicked_row, clicked_col):
                mark_square(clicked_row, clicked_col, player)
                
                if player == 1:
                    player = 2
                elif player == 2:
                    player = 1
            
    draw_figures()
    print(board)
    pygame.display.update()

pygame.quit()
