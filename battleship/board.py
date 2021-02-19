#	Author: Umar Khan
#	Date: 2/14/2021
#   Start: 8:40 PM


from .constants import *
from .ship import *
import time

class Board:

    def __init__(self, win, player0ships, player1ships):  
        self.player0ships = player0ships
        self.player1ships = player1ships
        self.player_ships = [self.player0ships, self.player1ships]
        self.win = win
        # 0 = nothing, 1 = hit, 2 = miss
        self.player0_hits_misses = []
        self.player1_hits_misses = []
        self.initialize_hits_misses()
        self.player_hits_misses = [self.player0_hits_misses, self.player1_hits_misses] 
        self.draw(0)
        

    def initialize_hits_misses(self):
        for i in range(10):
            self.player0_hits_misses.append([])
            self.player1_hits_misses.append([])
            for j in range(10):
                self.player0_hits_misses[i].append(0)
                self.player1_hits_misses[i].append(0)

    def draw_background(self):
        self.win.fill(BLACK)
        font = pygame.font.Font('freesansbold.ttf', 32)  # https://www.geeksforgeeks.org/python-display-text-to-pygame-window/
        text = font.render('Select the location you wish to hit', True, WHITE, RED)
        textRect = text.get_rect()
        textRect.center = (WIDTH // 4, TOP_PADDING // 2)
        self.win.blit(text, textRect)
        text = font.render("Player ships", True, WHITE, RED)
        textRect.center = ( (WIDTH // 4) * 3.5, TOP_PADDING // 2)
        self.win.blit(text, textRect)
        pygame.draw.rect(self.win, BLUE, (LEFT_PADDING, TOP_PADDING, GRID_WIDTH, GRID_HEIGHT))
        pygame.draw.rect(self.win, BLUE, (LEFT_PADDING + GRID_WIDTH + MIDDLE_PADDING, TOP_PADDING, GRID_WIDTH, GRID_HEIGHT))  
        self.draw_grid()

    def draw_grid(self):
        for i in range(11):
            # (win, color, (start X, start Y) , (end X, end Y))
            #horizontals
            pygame.draw.line(self.win, WHITE, (LEFT_PADDING, TOP_PADDING + i * SQUARE_SIZE + 50), 
                                              (LEFT_PADDING + GRID_WIDTH, TOP_PADDING + i * SQUARE_SIZE + 50))
            pygame.draw.line(self.win, WHITE, (WIDTH - RIGHT_PADDING - GRID_WIDTH, TOP_PADDING + i * SQUARE_SIZE + 50),
                                              (WIDTH - RIGHT_PADDING, TOP_PADDING + i * SQUARE_SIZE + 50))
            #verticals
            pygame.draw.line(self.win, WHITE, (LEFT_PADDING + i * SQUARE_SIZE + 50, TOP_PADDING),
                                              (LEFT_PADDING + i * SQUARE_SIZE + 50, HEIGHT - BOTTOM_PADDING))
            pygame.draw.line(self.win, WHITE, (WIDTH - RIGHT_PADDING - GRID_WIDTH + i * SQUARE_SIZE + 50, TOP_PADDING),
                                              (WIDTH - RIGHT_PADDING - GRID_WIDTH + i * SQUARE_SIZE + 50, HEIGHT - BOTTOM_PADDING))

            if i != 0:
                font = pygame.font.Font('freesansbold.ttf', 32)
                txt = "" + str(i)
                text = font.render(txt, True, BLACK, BLUE)
                textRect = text.get_rect()
                
                #numbers in top row
                textRect.center = (LEFT_PADDING + i * SQUARE_SIZE + SQUARE_SIZE // 2, TOP_PADDING + SQUARE_SIZE // 2 )
                self.win.blit(text, textRect)
                textRect.center = (LEFT_PADDING + GRID_WIDTH + MIDDLE_PADDING + i * SQUARE_SIZE + SQUARE_SIZE // 2, TOP_PADDING + SQUARE_SIZE // 2)
                self.win.blit(text, textRect)

                #letters on leftmost column
                txt = chr(64 + i)
                text = font.render(txt, True, BLACK, BLUE)
                textRect.center = (LEFT_PADDING + SQUARE_SIZE // 2, TOP_PADDING + i * SQUARE_SIZE + SQUARE_SIZE // 2)
                self.win.blit(text, textRect)
                textRect.center = (LEFT_PADDING + GRID_WIDTH + MIDDLE_PADDING + SQUARE_SIZE // 2, TOP_PADDING + i * SQUARE_SIZE + SQUARE_SIZE // 2)
                self.win.blit(text, textRect)
                #65 - 74 65 = A, 74 = J from https://stackoverflow.com/questions/4528982/convert-alphabet-letters-to-number-in-python

    def draw(self, player):

        self.draw_background()
        for ship in self.player_ships[player]:
            ship.draw(True, self.win) 
        if player != 0:
            for ship in self.player_ships[0]:
                if ship.is_destroyed():
                    ship.draw(False, self.win)
        else:
            for ship in self.player_ships[1]:
                if ship.is_destroyed():
                    ship.draw(False, self.win)

        for i, dude in enumerate(self.player_hits_misses):
            for row,two_d_array in enumerate(dude):
                for col, state in enumerate(two_d_array):
                    # 0 = nothing, 1 = hit, 2 = miss for state
                    if i == player: #current player is active, meaning print right
                        center_x = (WIDTH - RIGHT_PADDING - GRID_WIDTH + 50) + row * SQUARE_SIZE + SQUARE_SIZE // 2
                        center_y = (TOP_PADDING + 50) + col * SQUARE_SIZE + SQUARE_SIZE // 2
                        if state == 1: #miss
                            pygame.draw.circle(self.win, BLACK, (center_x, center_y), SQUARE_SIZE // 4)
                        elif state == 2: #hit
                            pygame.draw.circle(self.win, RED, (center_x, center_y), SQUARE_SIZE // 4)
                        #else: #for testing
                        #    pygame.draw.circle(self.win, WHITE, (center_x, center_y), SQUARE_SIZE // 4)
                    else: #print left
                        center_x = (LEFT_PADDING + 50) + row * SQUARE_SIZE + SQUARE_SIZE // 2
                        center_y = (TOP_PADDING + 50) + col * SQUARE_SIZE + SQUARE_SIZE // 2
                        if state == 1: #miss
                            pygame.draw.circle(self.win, BLACK, (center_x, center_y), SQUARE_SIZE // 4)
                        elif state == 2: #hit
                            pygame.draw.circle(self.win, RED, (center_x, center_y), SQUARE_SIZE // 4)
                        #else: #for testing
                        #   pygame.draw.circle(self.win, WHITE, (center_x, center_y), SQUARE_SIZE // 4)

    def hit_ship(self, player, row, col):
        #hits and misses against player 0 are in player_hits_misses[0]
        if player == 0:
            other_player = 1
        else:
            other_player = 0
        for ship in self.player_ships[other_player]:
            for tuple in ship.locations:
                if row == tuple[0] and col == tuple[1]:
                    ship.mark_hit(row,col)
                    self.player_hits_misses[other_player][row][col] = 2
                    print(f'(PLAYER {player}) Successful attack at: ({row}, {col})')
                    return True
        self.player_hits_misses[other_player][row][col] = 1
        print(f'(PLAYER {player}) Missed attack at : ({row}, {col})')
        return False
        '''
        if player == 0:
            for ship in self.player_ships[1]:
                for tuple in ship.locations:
                    if row == tuple[0] and col == tuple[1]:
                        ship.mark_hit(row,col)
                        self.player_hits_misses[1][row][col] = 2
                        print(f'(PLAYER 0) Successful attack at: ({row}, {col})')
                        return True
            self.player_hits_misses[1][row][col] = 1
            print(f'(PLAYER 0) Missed attack at: ({row}, {col})')
            return False
        else:
            for ship in self.player_ships[0]:
                for tuple in ship.locations:
                    if row == tuple[0] and col == tuple[1]:
                        ship.mark_hit(row, col)
                        self.player_hits_misses[0][row][col] = 2
                        print(f'(PLAYER 1) Hit/Miss List: {self.player_hits_misses[0]}')
                        print(f'(PLAYER 1) Successful attack at: ({row}, {col})')
                        return True
            self.player_hits_misses[0][row][col] = 1
            print(f'(PLAYER 1) Hit/Miss List: {self.player_hits_misses[0]}')
            print(f'(PLAYER 1) Missed attack at: ({row}, {col})')
            return False
        '''

    def update(self):
        pygame.display.update()  

    def info(self):
        print(f'Player 0 ships: {self.player0ships.ship}')
        print(f'Player 0 hit/misses: {self.p0_hit_misses}')
        print(f'Player 1 ships: {self.player1ships.ship}')
        print(f'Player 1 hit/misses: {self.p1_hit_misses}')
