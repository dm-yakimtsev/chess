import pygame
from board import Board


class Control:
    def __init__(self, wight, height):
        self.board = Board(wight, height)
        self.running = True
        self.wight = wight
        self.height = height

    def get_event(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.board.find_cell(event.pos, self.wight, self.height)

            if event.type == pygame.VIDEORESIZE:
                self.wight = event.w
                self.height = event.h
                self.board.change_board_size(self.wight, self.height)
