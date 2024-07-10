import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720), )
pygame.display.set_caption("CHESS")
image = pygame.image.load('resources/chess_icon.png').convert_alpha()
pygame.display.set_icon(image)

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    screen.fill("black")

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
