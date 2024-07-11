import pygame

import config
from config import WIGHT, HEIGHT
from board import Board

pygame.init()
screen = pygame.display.set_mode((WIGHT, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("CHESS")
image = pygame.image.load('resources/chess_icon.png').convert_alpha()
pygame.display.set_icon(image)

clock = pygame.time.Clock()
board = Board(WIGHT, HEIGHT)
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            running = False
        if event.type == pygame.VIDEORESIZE:
            WIGHT = event.w
            HEIGHT = event.h
            board.change_board_size(WIGHT, HEIGHT)

    screen.fill("white")
    screen.blit(board.image, ((WIGHT // 2) - board.image.get_rect().width // 2, 0)) # Отображаем доску
    pygame.display.update()
    clock.tick(60)

pygame.quit()
