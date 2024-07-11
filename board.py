import pygame
from figures import Pawn


class Board:
    def __init__(self, wight, height):
        self.main_image = pygame.image.load(
            'resources/85c32d6d3339a849aec9e6ecbec04a7e.jpg')  # Изображение с исходными размерами
        self.image = pygame.transform.scale(self.main_image, (height, height))
        self.wight = wight
        self.height = height
        self.indent = (height // 8) // 2  # Размер отступа
        self.cell_size = (height - self.indent * 2) // 8  # Размер клетки
        self.content = [[None, None, None, None, None, None, None, None],
                        [None, None, None, None, None, None, None, None],
                        [None, None, None, None, None, None, None, None],
                        [None, None, None, None, None, None, None, None],
                        [None, None, None, None, None, None, None, None],
                        [None, None, None, None, None, None, None, None],
                        [Pawn(0, 6, color=0), Pawn(1, 6, color=0), Pawn(2, 6, color=0), Pawn(3, 6, color=0),
                         Pawn(4, 6, color=0), Pawn(5, 6, color=1), Pawn(6, 6, color=1), Pawn(7, 6, color=0)],
                        [None, None, None, None, None, None, None, None]]  # Начальное расположение фигур

    def change_board_size(self, wight, height):
        """Изменяет размеры доски"""
        self.image = pygame.transform.scale(self.main_image, (height, height))
        self.wight = wight
        self.height = height
        self.indent = (height // 8) // 2  # Размер отступа
        self.cell_size = (height - self.indent * 2) // 8  # Размер клетки

    def find_cell(self, pos, wight, height):
        """Переводит координаты клика мышки в координаты клетки на доске от 0 до 7"""
        board_rect = self.image.get_rect()
        x = pos[0] - ((wight // 2) - board_rect.width // 2)  # Вычитаем расстояние до края
        y = pos[1]  # Высота доски такая же как и высота экрана

        if board_rect.collidepoint(x, y):  # Если кликнули по доске проверяем по какой клетке
            y_count = 0
            for i in range(self.indent, height - self.cell_size, self.cell_size):
                x_count = 0
                for j in range(self.indent, height - self.cell_size, self.cell_size):
                    if x_count < 8 and y_count < 8:  # Ограничиваю количество клеток
                        if pygame.Rect(j, i, self.cell_size,
                                       self.cell_size).collidepoint(x, y):
                            return self.content[x_count][y_count]
                    x_count += 1
                y_count += 1

    def render(self):
        """Рисует фигуры на доске"""
        y = 0
        for i in range(self.indent, self.height - self.cell_size, self.cell_size):
            x = 0
            for j in range(self.indent, self.height - self.cell_size, self.cell_size):
                if x < 8 and y < 8:  # Ограничиваю количество клеток
                    if self.content[x][y] is not None:
                        figure = self.content[x][y]
                        image = pygame.transform.scale(figure.main_image, (self.cell_size, self.cell_size))
                        self.image.blit(image, (i, j))
                x += 1
            y += 1
