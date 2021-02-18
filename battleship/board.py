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
        # user lists for hit and miss attacks
        self.hit_u = []
        self.miss_u = []
        # enemy lists for hit and miss attacks
        self.hit_e = []
        self.miss_e = []

    def draw_background(self):
        self.win.fill(BLACK)
        font = pygame.font.Font('freesansbold.ttf', 32) #https://www.geeksforgeeks.org/python-display-text-to-pygame-window/
        text = font.render('Select the location you wish to hit', True, WHITE, RED) #currently looks like trash, and
        textRect = text.get_rect()
        # textRect.center = (300,50)
        textRect.center = ((WIDTH /2) - 100, 50)
        self.win.blit(text, textRect)
        #pygame.draw.rect(self.win, GRAY, ())
        pygame.draw.rect(self.win, GRAY, (0, 100, 500, 500))
        pygame.draw.rect(self.win, GRAY, (700, 100, 500, 500)) #hardcoded of course
        self.draw_grid()

    def draw_grid(self):
        for i in range(10):
            pygame.draw.line(self.win, WHITE, (0, HEIGHT - self.grid_height + i * SQUARE_SIZE), (self.grid_width, HEIGHT - self.grid_height + i * SQUARE_SIZE), 3 )
            pygame.draw.line(self.win, WHITE, (WIDTH - self.grid_width, HEIGHT - self.grid_height + i * SQUARE_SIZE), (WIDTH, HEIGHT - self.grid_width + i *SQUARE_SIZE), 3 )
            pygame.draw.line(self.win, WHITE, (0 + i * SQUARE_SIZE, HEIGHT - self.grid_height), ( 0 + i * SQUARE_SIZE, HEIGHT), 3)
            pygame.draw.line(self.win, WHITE, (self.grid_width + 200 + i * SQUARE_SIZE, HEIGHT - self.grid_height), (self.grid_width + 200 + i * SQUARE_SIZE, HEIGHT), 3)

    def draw(self, player, ships):
        ships = self.get_ship(player, ships)
        list_of_ships = ships.ship
        for row, col, state in list_of_ships:
            if state == False:
                if player == 0:
                    pygame.draw.rect(self.win, BLUE, (row * SQUARE_SIZE + 700, col * SQUARE_SIZE + SQUARE_SIZE + SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                else:
                    pygame.draw.rect(self.win, BLUE, (row * SQUARE_SIZE, col * SQUARE_SIZE + SQUARE_SIZE + SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
        self.draw_grid()
        print(list_of_ships)

    def clear_ships(self, player, ships):
        ships = self.get_ship(player, ships)
        list_of_ships = ships.ship
        for row, col, state in list_of_ships:
            if state == False:
                if player == 0:
                    pygame.draw.rect(self.win, GRAY, (row * SQUARE_SIZE + 700, col * SQUARE_SIZE + SQUARE_SIZE + SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                else:
                    pygame.draw.rect(self.win, GRAY, (row * SQUARE_SIZE, col * SQUARE_SIZE + SQUARE_SIZE + SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
        self.draw_grid()
        print(list_of_ships)

    def hit_ship(self, player, row, col, ship):
        ships = self.get_ship(player, ship)
        for list_row, list_col, list_state in ships.ship:
            # hit enemies ship
            if row == list_row and col == list_col:
                ships.mark_hit(list_row, list_col)
                if player == 0:
                    pygame.draw.rect(self.win, GREEN, (row * SQUARE_SIZE, col * SQUARE_SIZE + SQUARE_SIZE + SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                    self.hit_u.append((row, col))
                else:
                    pygame.draw.rect(self.win, GREEN, (row * SQUARE_SIZE + 700, col * SQUARE_SIZE + SQUARE_SIZE + SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                    self.hit_e.append((row + 700, col))
                self.draw_grid()
                return
        # did not hit a ship
        if player == 0:
            pygame.draw.rect(self.win, RED, (row * SQUARE_SIZE, col * SQUARE_SIZE + SQUARE_SIZE + SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            self.miss_u.append((row, col))
        else:
            pygame.draw.rect(self.win, RED, (row * SQUARE_SIZE + 700, col * SQUARE_SIZE + SQUARE_SIZE + SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            self.miss_e.append((row + 700, col))
        self.draw_grid()

    def get_ship(self, player, ship):
        return ship
