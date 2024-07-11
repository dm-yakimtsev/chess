import pygame


class Figure:
    def __init__(self, x, y):
        self.x = x  # Индексы в матрице Board.content
        self.y = y
        self.is_selected = False

    def get_steps(self):
        pass


class Pawn(Figure):
    def __init__(self, x, y, color):
        super().__init__(x, y)
        self.color = color
        if self.color == 0:  # 0 это черные 1 это белые
            self.main_image = pygame.image.load('resources/black_pawn.png')
        else:
            self.main_image = pygame.image.load('resources/black_pawn.jpg')
