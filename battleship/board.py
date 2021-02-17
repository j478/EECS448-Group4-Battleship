#	Author: Umar Khan
#	Date: 2/14/2021
#   Start: 8:40 PM

from . constants import *
from . ship import *

class Board:
    def __init__(self, win): #p0ships, p1ships
        #self.p0ships = p0ships
        #self.p1ships = p1ships
        self.grid_width = 500
        self.grid_height = 500 #buffer of 200 for the labels and gaps in between the two different grids
        self.win = win
        self.draw_background()

    def draw_background(self):
        self.win.fill(BLACK)
        font = pygame.font.Font('freesansbold.ttf', 32) #https://www.geeksforgeeks.org/python-display-text-to-pygame-window/
        text = font.render('Select the location you wish to hit', True, WHITE, RED) #currently looks like trash, and
        textRect = text.get_rect()
        textRect.center = (300,50)
        self.win.blit(text, textRect)
        #pygame.draw.rect(self.win, GRAY, ())
        pygame.draw.rect(self.win, GRAY, (0, 100, 500, 500))
        pygame.draw.rect(self.win, GRAY, (700, 100, 500, 500)) #hardcoded of course

        for i in range(10):
            pygame.draw.line(self.win, WHITE, (0, HEIGHT - self.grid_height + i * SQUARE_SIZE), (self.grid_width, HEIGHT - self.grid_height + i * SQUARE_SIZE), 3 )
            pygame.draw.line(self.win, WHITE, (WIDTH - self.grid_width, HEIGHT - self.grid_height + i * SQUARE_SIZE), (WIDTH, HEIGHT - self.grid_width + i *SQUARE_SIZE), 3 )
            pygame.draw.line(self.win, WHITE, (0 + i * SQUARE_SIZE, HEIGHT - self.grid_height), ( 0 + i * SQUARE_SIZE, HEIGHT), 3)
            pygame.draw.line(self.win, WHITE, (self.grid_width + 200 + i * SQUARE_SIZE, HEIGHT - self.grid_height), (self.grid_width + 200 + i * SQUARE_SIZE, HEIGHT), 3)

    def get_ship(self, ship):
        print(ship.ship)
        return ship.ship

    def hit_ship(self, player, row, col, ship):
        ships = self.get_ship(ship)
        for list_row, list_col, list_state in ships:
            if list_row == row and list_col == col:
                self.draw(player, row, col, True)
                print(f'Attacked ship at ({row}, {col})')
                return
        self.draw(player, row, col, False)
        print(f'There was no ship at ({row}, {col})')

    def draw(self, player, row, col, success):
        if player == 0:
            if success:
                pygame.draw.rect(self.win, RED, (row * SQUARE_SIZE, col * SQUARE_SIZE + SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            else:
                pygame.draw.rect(self.win, BROWN, (row * SQUARE_SIZE, col * SQUARE_SIZE + SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
        else:
            if success:
                pygame.draw.rect(self.win, RED, (row * SQUARE_SIZE + 700, col * SQUARE_SIZE + SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            else:
                pygame.draw.rect(self.win, BROWN, (row * SQUARE_SIZE + 700, col * SQUARE_SIZE + SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))


    def initialize_game(self):
        pass
