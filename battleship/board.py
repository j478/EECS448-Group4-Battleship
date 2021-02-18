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
        ###could combine both of them into a single grid where you initialize say self.p0_hits_misses = [0,0,1,2, ....]
        ###where a 0 would be nothing has happened here, a 1 was a miss and a 2 was a hit. This would make for much
        ###easier printing
        ###there is also not one user as there is player 0 and player 1. So, you would be designating one of the players as 
        ###an enemy which is fine, but seems to be more confusing. There will only be one board class 
        # user lists for hit and miss attacks
        self.hit_u = []
        self.miss_u = []
        # enemy lists for hit and miss attacks
        self.hit_e = []
        self.miss_e = []

    def draw_background(self):
        self.win.fill(BLACK)
        font = pygame.font.Font('freesansbold.ttf', 32) #https://www.geeksforgeeks.org/python-display-text-to-pygame-window/
        text = font.render('Select the location you wish to hit', True, WHITE, RED) 
        textRect = text.get_rect()
        # textRect.center = (300,50)
        textRect.center = ((WIDTH /2) - 100, 50)
        self.win.blit(text, textRect)
        ###constants here with the padding, explained in draw_grid
        pygame.draw.rect(self.win, GRAY, (0, 100, 500, 500))
        pygame.draw.rect(self.win, GRAY, (700, 100, 500, 500)) #hardcoded of course
        self.draw_grid()

    def draw_grid(self):
        for i in range(10):
            ###Would it be possible to make constants here. I.e. WIDTH_PADDING = 200, HEIGHT_PADDING = 100
            ###I was also thinking it would be cool to have the grids like this: 
            ###  _| 1 | 2 | 3 | 4 | ...
            ###  A|
            ###  B|
            ###  C| 
            ###which would affect the padding but could also be accounted for with a constant where a box with label A would just be the 
            ###same size as a normal box
            pygame.draw.line(self.win, WHITE, (0, HEIGHT - self.grid_height + i * SQUARE_SIZE), (self.grid_width, HEIGHT - self.grid_height + i * SQUARE_SIZE), 3 )
            pygame.draw.line(self.win, WHITE, (WIDTH - self.grid_width, HEIGHT - self.grid_height + i * SQUARE_SIZE), (WIDTH, HEIGHT - self.grid_width + i *SQUARE_SIZE), 3 )
            pygame.draw.line(self.win, WHITE, (0 + i * SQUARE_SIZE, HEIGHT - self.grid_height), ( 0 + i * SQUARE_SIZE, HEIGHT), 3)
            pygame.draw.line(self.win, WHITE, (self.grid_width + 200 + i * SQUARE_SIZE, HEIGHT - self.grid_height), (self.grid_width + 200 + i * SQUARE_SIZE, HEIGHT), 3)
    
    ###dont need to pass the ships as these will already be stored in member variables. I commented them out for testing purposes but this 
    ###is how it will interact with the Game class and get the location of the ships in the first place
    def draw(self, player, ships):
        ###this will just call itself and then return itself, I believe it only returns a single ship as well 
        ships = self.get_ship(player, ships)
        ###Unsure of what ships.ship would do 
        list_of_ships = ships.ship
        for row, col, state in list_of_ships:
            if state == False:
                if player == 0:
                    pygame.draw.rect(self.win, BLUE, (row * SQUARE_SIZE + 700, col * SQUARE_SIZE + SQUARE_SIZE + SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                else:
                    pygame.draw.rect(self.win, BLUE, (row * SQUARE_SIZE, col * SQUARE_SIZE + SQUARE_SIZE + SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
        self.draw_grid()
        ###Basically I believe it shoudl go like this. 
        ### draw_background()
        ###if player == 0:
        ###     print that players ships on the right hand grid. 
        ###     for ship in self.player0ships:
        ###         ship.draw()
        ###     for loc in player0_hits_misses:
        ###         if loc == 1:# miss
        ###             draw small black circle in center of square
        ###         if loc == 2: # hit
        ###             draw small red circle in center of square(which will go over top of the ship if there is one there)
        ###else:
        ### do for player 2
        print(list_of_ships)

    ###I do not believe this is necessary as a ship does not need to be cleared. It still needs to be displayed but it will just display that it 
    ### is sunk. This will be done in the Ship class, but will display using ship.draw()
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
    
    ###the GAME class would be attempting a hit on a square row and col, but it would not know if there is a ship there. So it can not pass ship
    ### hit_ship(self, player, row, col)
    def hit_ship(self, player, row, col, ship):
        ###first determine which player it is 
        ###then you may have to loop through the ships and their locations
        ###if any of the ships contain a row,col == row and col that were passed. 
        ###     Then grab that ship and do ship.hit(row,col)
        ###     mark a hit for that player in playerxhits_misses 
        ###     return True
        ###else 
        ###     mark a miss and return False
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

    ###this is not really relevant, if you already are passing the ship, then why run the function?
    ### get_ship(self, player, row, col)
    def get_ship(self, player, ship):
        return ship
