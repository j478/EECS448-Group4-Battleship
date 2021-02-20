#	Author: Rishab Bhat
#	Date: 2/18/21
import pygame
from .constants import *
from .board import *
import time

class Game:

    
    def __init__(self, win, p0ships, p1ships):

        self.board = Board(win, p0ships, p1ships)
        self.player_turn = 0
        self.player_0_ships, self.player_1_ships = len(p0ships), len(p1ships)
        self.win = win

    def hit_ship(self, row, col):
        ship = self.board.hit_ship(self.player_turn, row,col)
        if ship != 0:
            if ship.is_destroyed():
                if self.player_turn == 0:
                    self.player_1_ships -= 1
                else:
                    self.player_0_ships -= 1

    

    def update(self):
        self.hover()
        self.board.update(self.player_turn)
        


 

    def switch_players(self):
        self.win.fill(BLACK)
        
        font = pygame.font.Font('freesansbold.ttf', 50)  # https://www.geeksforgeeks.org/python-display-text-to-pygame-window/
        text = font.render(f'Switching to Player {self.player_turn +1} in three seconds', True, WHITE, RED)
        textRect = text.get_rect()
        textRect.center = (WIDTH // 2, HEIGHT // 2)
        self.win.blit(text, textRect)
        pygame.display.update()
      #  time.sleep(3)

        

    

    def change_turn(self):
         if self.player_turn == 0:
            self.player_turn = 1
         elif self.player_turn == 1:
            self.player_turn = 0
    

    def game_over(self):

        if self.player_0_ships == 0 or self.player_1_ships == 0:

            return True
        else: 
            return False

   

    def hover(self):
        pos = pygame.mouse.get_pos()
        row, col = self.get_row_col_from_pos(pos)
        if row != -1 and col != -1:
            pygame.draw.circle(self.win, GREEN, (TOP_PADDING + col * SQUARE_SIZE + SQUARE_SIZE // 2, LEFT_PADDING + SQUARE_SIZE + SQUARE_SIZE + row * SQUARE_SIZE + SQUARE_SIZE //2), SQUARE_SIZE // 4)
            
            pygame.display.update()
    def get_row_col_from_pos(self, pos):
        x,y = pos
        if (x > LEFT_PADDING + SQUARE_SIZE) and x < (LEFT_PADDING +  GRID_WIDTH):
            if (y > TOP_PADDING + SQUARE_SIZE) and y < (HEIGHT - BOTTOM_PADDING):
                col = (x - LEFT_PADDING - SQUARE_SIZE) // SQUARE_SIZE #return 0-9
                row = (y - TOP_PADDING - SQUARE_SIZE) //SQUARE_SIZE
            else:
                row = -1
                col = -1
        else:
            row = -1
            col = -1
        return row, col

    def select(self, pos):
        row, col = self.get_row_col_from_pos(pos)
        if row != -1 and col != -1:
            self.hit_ship(row, col)
            self.change_turn()
            self.switch_players()
            