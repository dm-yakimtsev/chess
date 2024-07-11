import pygame


class Board:
    def __init__(self, wight, height):
        self.main_image = pygame.image.load(
            'resources/85c32d6d3339a849aec9e6ecbec04a7e.jpg')  # Изображение с исходными размерами
        self.image = pygame.transform.scale(self.main_image, (height, height))

        self.content = [[[] for i in range(8)] for j in range(8)]

    def change_board_size(self, wight, height):
        """Подгоняет картинку доски под размеры окна"""
        self.image = pygame.transform.scale(self.main_image, (height, height))

    def find_cell(self, pos, wight, height):
        """Переводит координаты клика мышки в координаты клетки на доске от 0 до 7"""
        board_rect = self.image.get_rect()
        x = pos[0] - ((wight // 2) - board_rect.width // 2)  # Вычитаем расстояние до края
        y = pos[1]  # Высота доски такая же как и высота экрана
        indent = (height // 8) // 2  # Размер отступа
        cell_size = (height - indent * 2) // 8  # Размер клетки

        if board_rect.collidepoint(x, y):  # Если кликнули по доске проверяем по какой клетке
            y_count = 0
            for i in range(indent, height - cell_size, cell_size):
                x_count = 0
                for j in range(indent, height - cell_size, cell_size):

                    if pygame.Rect(j, i, cell_size,
                                   cell_size).collidepoint(x, y):
                        print(y_count, x_count)
                    x_count += 1
                y_count += 1
