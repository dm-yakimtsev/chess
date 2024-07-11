import pygame


class Board:
    def __init__(self, wight, height):
        self.main_image = pygame.image.load('resources/85c32d6d3339a849aec9e6ecbec04a7e.jpg') # Изображение с исходными размерами
        self.image = pygame.transform.scale(self.main_image, (height, height))
        self.board_rect = self.image.get_rect()

    def change_board_size(self, wight, height):
        """Подгоняет картинку доски под размеры окна"""
        self.image = pygame.transform.scale(self.main_image, (height, height))

