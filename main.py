import pygame
from control import Control
from config import WIGHT, HEIGHT


pygame.init()
screen = pygame.display.set_mode((WIGHT, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("CHESS")
image = pygame.image.load('resources/chess_icon.png').convert_alpha()
pygame.display.set_icon(image)

clock = pygame.time.Clock()

control = Control(WIGHT, HEIGHT)

while control.running:
    control.get_event()

    screen.fill("white")
    screen.blit(control.board.image,
                ((control.wight // 2) - control.board.image.get_rect().width // 2, 0))  # Отображаем доску по центру
    control.board.render()
    pygame.display.update()
    clock.tick(60)

pygame.quit()
