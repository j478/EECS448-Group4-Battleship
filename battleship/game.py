#	Author: Rishab Bhat
#	Date: 2/18/21
import pygame
from .constants import *
from .board import *
import time


class Game:
    # @pre - initialize Game Class
    # @param - passed Pygame window and arrays of ships for players 1 and 2
    # @post - Creates a Board class. Stores the current player's turn
    # @return - None
    def __init__(self, win, p0ships, p1ships):
        self.board = Board(win, p0ships, p1ships)
        self.player_turn = 0
        self.player_0_ships, self.player_1_ships = len(p0ships), len(p1ships)
        self.win = win

    # @pre - Checks for a hit in the Board class on the opposing player's ship
    # @param - passed row and col of attempted hit
    # @post - updates data structures in Board class and any hit Ship
    # @return - None
    def hit_ship(self, row, col):
        ship = self.board.hit_ship(self.player_turn, row, col)
        self.print_hit(ship)
        if ship != 0:
            if ship.is_destroyed():
                if self.player_turn == 0:
                    self.player_1_ships -= 1
                else:
                    self.player_0_ships -= 1

    # @pre - Prints the result of an attempted hit or miss
    # @param - passed a Ship object or 0
    # @post - prints result of attempt to User
    # @return - None
    def print_hit(self, ship):
        self.win.fill(GRAY)
        if ship != 0:
            if ship.is_destroyed():
                txt = f"Player {self.player_turn + 1} sunk a battleship!"
            else:
                txt = f"Player {self.player_turn + 1} hit a battleship!"
        else:
            txt = f"Player {self.player_turn + 1} miss!"
        font = pygame.font.Font('freesansbold.ttf',
                                50)  # https://www.geeksforgeeks.org/python-display-text-to-pygame-window/
        text = font.render(txt, True, WHITE, RED)
        textRect = text.get_rect()
        textRect.center = (WIDTH // 2, HEIGHT // 2)
        self.win.blit(text, textRect)
        pygame.display.update()
        time.sleep(0.75)

        # @pre - Updates the output to the screen

    # @param - None
    # @post - prints the grids and ships of the window
    # @return - None
    def update(self):
        self.hover()
        self.board.update(self.player_turn)

    # @pre - will print to the players to switch users
    # @param - None
    # @post - Prints to the board "Switching player in 2 seconds"
    # @return - None
    def switch_players(self):
        self.win.fill(BLACK)
        font = pygame.font.Font('freesansbold.ttf',
                                50)  # https://www.geeksforgeeks.org/python-display-text-to-pygame-window/
        text = font.render(f'Switching to Player {self.player_turn + 1} in two seconds', True, WHITE, RED)
        textRect = text.get_rect()
        textRect.center = (WIDTH // 2, HEIGHT // 2)
        self.win.blit(text, textRect)
        pygame.display.update()
        time.sleep(2)

    # @pre - Changes the player_turn
    # @param - None
    # @post - self.player_turn is reversed
    # @return - None
    def change_turn(self):
        if self.player_turn == 0:
            self.player_turn = 1
        elif self.player_turn == 1:
            self.player_turn = 0

    # @pre - determines if the game should be over
    # @param - None
    # @post - causes game to end if one of the players has 0 ships left
    # @return - True or False
    def game_over(self):
        if self.player_0_ships == 0 or self.player_1_ships == 0:
            return True
        else:
            return False

    # @pre - If the mouse is on the left grid, it will show to the user which row and col is currently selected
    # @param - None
    # @post - draws a green circle in the middle of a box if the mouse is on the grid
    # @return - None
    def hover(self):
        pos = pygame.mouse.get_pos()
        row, col = self.get_row_col_from_pos(pos)
        if row != -1 and col != -1:
            pygame.draw.circle(self.win, GREEN, (TOP_PADDING + col * SQUARE_SIZE + SQUARE_SIZE // 2,
                                                 LEFT_PADDING + SQUARE_SIZE + SQUARE_SIZE + row * SQUARE_SIZE + SQUARE_SIZE // 2),
                               SQUARE_SIZE // 4)
            pygame.display.update()

    # @pre - uses the pixel position in x and y to get the row and column on the left grid
    # @param - passed pos (x,y)
    # @post - gives corresponding row and column to the hover() method
    # @return - row, col
    def get_row_col_from_pos(self, pos):
        x, y = pos
        if (x > LEFT_PADDING + SQUARE_SIZE) and x < (LEFT_PADDING + GRID_WIDTH):
            if (y > TOP_PADDING + SQUARE_SIZE) and y < (HEIGHT - BOTTOM_PADDING):
                col = (x - LEFT_PADDING - SQUARE_SIZE) // SQUARE_SIZE  # return 0-9
                row = (y - TOP_PADDING - SQUARE_SIZE) // SQUARE_SIZE
            else:
                row = -1
                col = -1
        else:
            row = -1
            col = -1
        return row, col

    # @pre - if the mouse makes a click in a relevant position(on the left grid), then it attepts a hit
    # @param - pos (x,y) in pixels
    # @post - if the position is valid, then it will attempt a hit and then change players
    # @return - None
    def select(self, pos):
        row, col = self.get_row_col_from_pos(pos)
        if row != -1 and col != -1:
            self.hit_ship(row, col)
            self.change_turn()
            self.switch_players()
