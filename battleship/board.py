#	Author: Umar Khan
#	Date: 2/14/2021
#   Start: 8:40 PM


from .constants import *
from .ship import *
import time

class Board:
    LEFT_PADDING = 25
    RIGHT_PADDING = 25
    MIDDLE_PADDING = 50 
    TOP_PADDING = 75
    BOTTOM_PADDING = 25
    GRID_WIDTH = 550
    GRID_HEIGHT = 550
    def __init__(self, win, player0ships, player1ships):  # p0ships, p1ships
        self.player0ships = player0ships
        self.player1ships = player1ships
        self.player_ships = [self.player0ships, self.player1ships]
        self.win = win
        # 0 = nothing, 1 = hit, 2 = miss
        self.player0_hits_misses = []
        self.player1_hits_misses = []
        self.initialize_hits_misses()
        self.player_hits_misses = [self.player0_hits_misses, self.player1_hits_misses] 
        self.draw(1)


        
    def initialize_hits_misses(self):
        for i in range(10):
            self.player0_hits_misses.append([])
            self.player1_hits_misses.append([])
            for j in range(10):
                self.player0_hits_misses[i].append(0)
                self.player1_hits_misses[i].append(0)
        self.player0_hits_misses[3][3] = 1
        self.player0_hits_misses[7][7] = 2
        self.player0_hits_misses[4][4] = 2
        self.player1_hits_misses[5][3] = 1
        self.player1_hits_misses[5][7] = 2
        self.player1_hits_misses[5][4] = 1
    def draw_background(self):
        self.win.fill(BLACK)
        font = pygame.font.Font('freesansbold.ttf', 32)  # https://www.geeksforgeeks.org/python-display-text-to-pygame-window/
        text = font.render('Select the location you wish to hit', True, WHITE, RED)
        textRect = text.get_rect()
        textRect.center = (WIDTH // 4, self.TOP_PADDING // 2)
        self.win.blit(text, textRect)
        text = font.render("Player ships", True, WHITE, RED)
        textRect.center = ( (WIDTH // 4) * 3.5, self.TOP_PADDING // 2)
        self.win.blit(text, textRect)
        pygame.draw.rect(self.win, GRAY, (self.LEFT_PADDING, self.TOP_PADDING, self.GRID_WIDTH, self.GRID_HEIGHT))
        pygame.draw.rect(self.win, GRAY, (self.LEFT_PADDING + self.GRID_WIDTH + self.MIDDLE_PADDING, self.TOP_PADDING, self.GRID_WIDTH, self.GRID_HEIGHT))  
        self.draw_grid()

    def draw_grid(self):
        for i in range(11):
            # (win, color, (start X, start Y) , (end X, end Y))
            #horizontals
            pygame.draw.line(self.win, WHITE, (self.LEFT_PADDING, self.TOP_PADDING + i * SQUARE_SIZE + 50), 
                                              (self.LEFT_PADDING + self.GRID_WIDTH, self.TOP_PADDING + i * SQUARE_SIZE + 50))
            pygame.draw.line(self.win, WHITE, (WIDTH - self.RIGHT_PADDING - self.GRID_WIDTH, self.TOP_PADDING + i * SQUARE_SIZE + 50),
                                              (WIDTH - self.RIGHT_PADDING, self.TOP_PADDING + i * SQUARE_SIZE + 50))
            #verticals
            pygame.draw.line(self.win, WHITE, (self.LEFT_PADDING + i * SQUARE_SIZE + 50, self.TOP_PADDING),
                                              (self.LEFT_PADDING + i * SQUARE_SIZE + 50, HEIGHT - self.BOTTOM_PADDING))
            pygame.draw.line(self.win, WHITE, (WIDTH - self.RIGHT_PADDING - self.GRID_WIDTH + i * SQUARE_SIZE + 50, self.TOP_PADDING),
                                              (WIDTH - self.RIGHT_PADDING - self.GRID_WIDTH + i * SQUARE_SIZE + 50, HEIGHT - self.BOTTOM_PADDING))

            if i != 0:
                font = pygame.font.Font('freesansbold.ttf', 32)
                txt = "" + str(i)
                text = font.render(txt, True, BLACK, GRAY)
                textRect = text.get_rect()
                
                #numbers in top row
                textRect.center = (self.LEFT_PADDING + i * SQUARE_SIZE + SQUARE_SIZE // 2, self.TOP_PADDING + SQUARE_SIZE // 2 )
                self.win.blit(text, textRect)
                textRect.center = (self.LEFT_PADDING + self.GRID_WIDTH + self.MIDDLE_PADDING + i * SQUARE_SIZE + SQUARE_SIZE // 2, self.TOP_PADDING + SQUARE_SIZE // 2)
                self.win.blit(text, textRect)

                #letters on leftmost column
                txt = chr(64 + i)
                text = font.render(txt, True, BLACK, GRAY)
                textRect.center = (self.LEFT_PADDING + SQUARE_SIZE // 2, self.TOP_PADDING + i * SQUARE_SIZE + SQUARE_SIZE // 2)
                self.win.blit(text, textRect)
                textRect.center = (self.LEFT_PADDING + self.GRID_WIDTH + self.MIDDLE_PADDING + SQUARE_SIZE // 2, self.TOP_PADDING + i * SQUARE_SIZE + SQUARE_SIZE // 2)
                self.win.blit(text, textRect)
                #65 - 74 65 = A, 74 = J from https://stackoverflow.com/questions/4528982/convert-alphabet-letters-to-number-in-python

    def draw(self, player):
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

        self.draw_background()

        for ship in self.player_ships[player]:
            ship.draw(self.win)

        for i, dude in enumerate(self.player_hits_misses):
            for row,two_d_array in enumerate(dude):
                for col, state in enumerate(two_d_array):
                    # 0 = nothing, 1 = hit, 2 = miss for state
                    if i == player: #current player is active, meaning print right
                        center_x = (WIDTH - self.RIGHT_PADDING - self.GRID_WIDTH + 50) + row * SQUARE_SIZE + SQUARE_SIZE // 2
                        center_y = (self.TOP_PADDING + 50) + col * SQUARE_SIZE + SQUARE_SIZE // 2
                        if state == 1: #miss
                            pygame.draw.circle(self.win, BLACK, (center_x, center_y), SQUARE_SIZE // 4)
                        elif state == 2: #hit
                            pygame.draw.circle(self.win, RED, (center_x, center_y), SQUARE_SIZE // 4)
                        #else: #for testing
                        #    pygame.draw.circle(self.win, WHITE, (center_x, center_y), SQUARE_SIZE // 4)
                    else: #print left
                        center_x = (self.LEFT_PADDING + 50) + row * SQUARE_SIZE + SQUARE_SIZE // 2
                        center_y = (self.TOP_PADDING + 50) + col * SQUARE_SIZE + SQUARE_SIZE // 2
                        if state == 1: #miss
                            pygame.draw.circle(self.win, BLACK, (center_x, center_y), SQUARE_SIZE // 4)
                        elif state == 2: #hit
                            pygame.draw.circle(self.win, RED, (center_x, center_y), SQUARE_SIZE // 4)
                        #else: #for testing
                        #   pygame.draw.circle(self.win, WHITE, (center_x, center_y), SQUARE_SIZE // 4)

    ###the GAME class would be attempting a hit on a square row and col, but it would not know if there is a ship there. So it can not pass ship
    ### hit_ship(self, player, row, col)
    def hit_ship(self, player, row, col):
        ###first determine which player it is
        ###then you may have to loop through the ships and their locations
        ###if any of the ships contain a row,col == row and col that were passed.
        ###     Then grab that ship and do ship.hit(row,col)
        ###     mark a hit for that player in playerxhits_misses
        ###     return True
        ###else
        ###     mark a miss and return False

        if player == 0:
            for ship_row, ship_col, state in self.player1ships.ship:
                if ship_row == row and ship_col == col:
                    self.player0ships.mark_hit(row, col)
                    self.p0_hit_misses.append(tuple((row, col, 2)))
                    print(f'(PLAYER 0) Hit/Miss List: {self.p0_hit_misses}')
                    print(f'(PLAYER 0) Successful attack at: ({row}, {col})')
                    return
            self.p0_hit_misses.append(tuple((row, col, 1)))
            print(f'(PLAYER 0) Hit/Miss List: {self.p0_hit_misses}')
            print(f'(PLAYER 0) Missed attack at: ({row}, {col})')
        else:
            for ship_row, ship_col, state in self.player0ships.ship:
                if ship_row == row and ship_col == col:
                    self.player1ships.mark_hit(row, col)
                    self.p1_hit_misses.append(tuple((row, col, 2)))
                    print(f'(PLAYER 1) Hit/Miss List: {self.p1_hit_misses}')
                    print(f'(PLAYER 1) Successful attack at: ({row}, {col})')
                    return
            self.p1_hit_misses.append(tuple((row, col, 1)))
            print(f'(PLAYER 1) Hit/Miss List: {self.p1_hit_misses}')
            print(f'(PLAYER 1) Missed attack at: ({row}, {col})')

    def info(self):
        print(f'Player 0 ships: {self.player0ships.ship}')
        print(f'Player 0 hit/misses: {self.p0_hit_misses}')
        print(f'Player 1 ships: {self.player1ships.ship}')
        print(f'Player 1 hit/misses: {self.p1_hit_misses}')
