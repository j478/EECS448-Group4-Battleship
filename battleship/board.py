#	Author: Umar Khan
#	Date: 2/15/2021
#   Start: 8:40 PM

from . constants import *
import numpy
import pygame, sys
from . ship import *
#from. tile import *

#################################
# This version does not use the Tile class. Attacks work but still working on placing ships.
# Need to figure out a way to interact with the ship class
class Board():
    def __init__(self, win):
        self.attacked = False
        self.board_rows = ROWS
        self.board_cols = COLS
        self.tile_padding = 1.25
        self.board = numpy.full((ROWS, COLS), self.attacked)
        self.tile_size = SQUARE_SIZE / 2 / 2 / 2
        self.board_layout = BOARD_LAYOUT_test
        self.user_board = numpy.full((ROWS, COLS), self.attacked)
        self.enemy_board = numpy.full((ROWS, COLS), self.attacked)
        self.has_ship = False

    def read_board_layout(self, win, board_layout):
        with open(board_layout, 'r') as f:
            board = f.readlines()
        board = [line.strip() for line in board]
        print(board)
        return board

    def draw_background(self, win):
        self.modify_user_file()
        self.modify_enemy_file()
        row_label = 0
        col_label = 0
        board_lo = self.read_board_layout(win, self.board_layout)
        for j, tile in enumerate(board_lo):
            for i, tile_contents in enumerate(tile):
                rect = pygame.Rect(i * self.tile_size * self.tile_padding, j * self.tile_size * self.tile_padding, self.tile_size, self.tile_size)
                pygame.draw.rect(win, self.tile_color(tile_contents, board_lo), rect)

    def tile_color(self, tile_contents, board_lo):
        # - for label, # for untouched tile, * for user board attacked, X for enemy board attacked, O place ship
        tile_color = BLACK
        if tile_contents == '-':
            tile_color = WHITE
        if tile_contents == 'O':
            tile_color = BLUE
        if tile_contents == "#":
            tile_color = GRAY
        if tile_contents == '*' or tile_contents == 'X':
            tile_color = RED
        return tile_color

    def modify_user_file(self):
        with open(self.board_layout, "w") as text_file:
            for row in range(len(self.user_board)):
                text_file.write('-')
                for col in range(len(self.user_board[0])):
                    if row == 0:
                        text_file.write('-')
                    # elif self.user_board[row - 1][col - 1].has_ship == True:
                    #     text_file.write('O')
                    elif self.user_board[row - 1][col] == False:
                        text_file.write("#")
                    elif self.user_board[row - 1][col] == True:
                        text_file.write('*')
                    else:
                        pass
                text_file.write('\n')
            text_file.write('\n')

    def modify_enemy_file(self):
        with open(self.board_layout, "a") as text_file:
            for row in range(len(self.enemy_board)):
                text_file.write('-')
                for col in range(len(self.enemy_board[0])):
                    if row == 0:
                        text_file.write('-')
                    elif self.enemy_board[row - 1][col] == False:
                        text_file.write("#")
                    elif self.enemy_board[row - 1][col] == True:
                        text_file.write('X')
                    else:
                        pass
                text_file.write("\n")

    def hit_ship(self, row, col, enemy):
        # if enemy is True, then the enemy is attacking user. Affecting user board
        with open(self.board_layout, "a") as text_file:
            text_file.close()
            if enemy == True:
                self.user_board[row][col] = True
                self.modify_user_file()
            else:
                self.enemy_board[row][col] = True
                self.modify_enemy_file()
        print(self.user_board)

    #################################

# !!!!!!!!!!!!!!!!!!
# This version uses the Tile class. The tile class determines what state each tile is. Not finished implementing so does not work yet
# class Board():
#     def __init__(self, win):
#         #self.attacked = False
#         self.board_rows = ROWS
#         self.board_cols = COLS
#         self.tile_padding = 1.25
#         #self.board = numpy.full((ROWS, COLS), self.attacked)
#         self.tile_size = SQUARE_SIZE / 2 / 2 / 2
#         self.board_layout = BOARD_LAYOUT_test
#         self.user = 0
#         self.enemy = 1
#         self.user_board = [[Tile(i, j, self.user) for j in range(COLS)] for i in range(ROWS)]
#         self.enemy_board = [[Tile(i, j, self.enemy) for j in range(COLS)] for i in range(ROWS)]
#         self.has_ship = False
#
#     def read_board_layout(self, win, board_layout):
#         with open(board_layout, 'r') as f:
#             board = f.readlines()
#         board = [line.strip() for line in board]
#         print(board)
#         return board
#
#     def draw_background(self, win):
#         self.modify_user_file()
#         self.modify_enemy_file()
#         row_label = 0
#         col_label = 0
#         board_lo = self.read_board_layout(win, self.board_layout)
#         for j, tile in enumerate(board_lo):
#             for i, tile_contents in enumerate(tile):
#                 rect = pygame.Rect(i * self.tile_size * self.tile_padding, j * self.tile_size * self.tile_padding, self.tile_size, self.tile_size)
#                 pygame.draw.rect(win, self.tile_color(tile_contents, board_lo), rect)
#
#     def tile_color(self, tile_contents, board_lo):
#         # - for label, # for untouched tile, * for user board attacked, X for enemy board attacked, O place ship
#         # L for label, E for empty tile, M for my ship, + for attacked but missed, X for attacked ship
#         tile_color = BLACK
#         if tile_contents == 'L':
#             tile_color = WHITE
#         if tile_contents == 'M':
#             tile_color = BLUE
#         if tile_contents == "E":
#             tile_color = GRAY
#         if tile_contents == '*':
#             tile_color = RED
#         return tile_color
#
#     def modify_user_file(self):
#         with open(self.board_layout, "w") as text_file:
#             for row in range(len(self.user_board)):
#                 text_file.write('L')
#                 for col in range(len(self.user_board[0])):
#                     if row == 0:
#                         text_file.write('L')
#                     elif Tile(row - 1, col, 0).attacked_ship == True:
#                         text_file.write('*')
#                     elif Tile(row -1, col, 0).my_ship == True:
#                         text_file.write('M')
#                     elif Tile(row - 1, col, 0).empty_tile == True:
#                         text_file.write('E')
#                     else:
#                         pass
#                 text_file.write('\n')
#             text_file.write('\n')
#
#     def modify_enemy_file(self):
#         with open(self.board_layout, "a") as text_file:
#             for row in range(len(self.enemy_board)):
#                 text_file.write('L')
#                 for col in range(len(self.enemy_board[0])):
#                     if row == 0:
#                         text_file.write('L')
#                     elif Tile(row - 1, col, 1).attacked_ship == True:
#                         text_file.write('*')
#                     elif Tile(row - 1, col, 1).my_ship == True:
#                         text_file.write('M')
#                     elif Tile(row - 1, col, 1).empty_tile == True:
#                         text_file.write('E')
#                     else:
#                         pass
#                 text_file.write("\n")
#
#     def hit_ship(self, row, col, type):
#         # if enemy is True, then the enemy is attacking user. Affecting user board
#         # user attacking enemy
#         Tile(row, col, type).attacked_ship = True
#         if type == 0:
#             self.modify_enemy_file()
#         else:
#             self.modify_user_file()
# !!!!!!!!!!!!!!!!!!!!!!!!
