import pygame

from .button import Button
from .constants import *
from .ship import Ship


class Initialize:

    # @pre - needs a game size if choose gamesize is false
    # @param - the window/surface, a boolean of whether the gamesize is already decided and a game size that only
    # matters if choosegamesize is false
    # @post - defines variables and either calls gameSize() or skips to pickShips()
    # @return - none
    def __init__(self, win, ChooseGameSize, GameSize):
        self.gameSizeSelected = False  # boolean used in the while loop of gamesize selected
        self.win = win  # window
        self.shipsSelected = 0  # amount of ships in the game
        self.shipList = []  # list that will be appended later and passed to the board

        self.b1 = Button((0, 250, 0), 0, 0, 500, 99, '1 Ship')  # first set of buttons definition
        self.b2 = Button((0, 250, 0), 0, 100, 500, 99, '2 Ship')
        self.b3 = Button((0, 250, 0), 0, 200, 500, 99, '3 Ship')
        self.b4 = Button((0, 250, 0), 0, 300, 500, 99, '4 Ship')
        self.b5 = Button((0, 250, 0), 0, 400, 500, 99, '5 Ship')
        self.b6 = Button((0, 250, 0), 0, 500, 500, 99, '6 Ship')

        self.placed1 = False  # booleans for if each ship has been placed used in pick ships
        self.placed2 = False
        self.placed3 = False
        self.placed4 = False
        self.placed5 = False
        self.placed6 = False

        self.s1 = Button((0, 250, 0), 0, 0, 100, 50,
                         '1x1')  # definitions for second set of buttons used to drag the ships
        self.s2 = Button((0, 250, 0), 0, 100, 200, 50, '1x2')
        self.s3 = Button((0, 250, 0), 0, 200, 300, 50, '1x3')
        self.s4 = Button((0, 250, 0), 0, 300, 400, 50, '1x4')
        self.s5 = Button((0, 250, 0), 0, 400, 500, 50, '1x5')
        self.s6 = Button((0, 250, 0), 0, 500, 600, 50, '1x6')

        # Ship array used locally to make sure ships dont overlap
        self.shipArray = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        # player 1 will take this path
        if ChooseGameSize:
            self.shipCount = 0
            self.gameSize()
            # player 2 will take this path (this is when the gameSize is needed)
        else:
            self.shipCount = GameSize
            self.pickShips(self.shipCount)

    # @pre - none
    # @param - none
    # @post - draws the first set of buttons to determine ship count and checks when theyve been clicked
    # @return - none
    def gameSize(self):
        while self.gameSizeSelected == False:
            pygame.display.update()
            # draws the game size selection buttons
            self.b1.draw(self.win)
            self.b2.draw(self.win)
            self.b3.draw(self.win)
            self.b4.draw(self.win)
            self.b5.draw(self.win)
            self.b6.draw(self.win)
            # checks if the mouse was over buttons if they were clicked and if so, chooses the right amount of ships
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if self.b1.hover(pos) == True:
                        self.pickShips(1)
                        self.gameSizeSelected = True
                    if self.b2.hover(pos) == True:
                        self.pickShips(2)
                        self.gameSizeSelected = True
                    if self.b3.hover(pos) == True:
                        self.pickShips(3)
                        self.gameSizeSelected = True
                    if self.b4.hover(pos) == True:
                        self.pickShips(4)
                        self.gameSizeSelected = True
                    if self.b5.hover(pos) == True:
                        self.pickShips(5)
                        self.gameSizeSelected = True
                    if self.b6.hover(pos) == True:
                        self.pickShips(6)
                        self.gameSizeSelected = True

                    print('mouse clicked')

    # @pre - needs to have the amount of ships already decided
    # @param - amount of ships in the game
    # @post - clears the window then draws the correct amount of buttons then when a button is selected calls the place
    # ship function and grays-out and disables the button until all buttons have been selected
    # @return - none

    def pickShips(self, shipCount):
        # clears window by drawing new rectangle
        pygame.draw.rect(self.win, (0, 0, 0), (0, 0, 1300, 800), 0)
        # draws the board
        self.drawPlayerBoard()
        self.shipCount = shipCount
        # draws the right amount of ship selection buttons on the screen
        for i in range(self.shipCount + 1):
            if i == 1:
                self.s1.draw(self.win)

            if i == 2:
                self.s2.draw(self.win)

            if i == 3:
                self.s3.draw(self.win)

            if i == 4:
                self.s4.draw(self.win)

            if i == 5:
                self.s5.draw(self.win)

            if i == 6:
                self.s6.draw(self.win)
        # loop goes until all ships have been selected and disables buttons after being pressed
        while self.shipsSelected < self.shipCount:
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if self.s1.hover(pos) == True and self.shipCount >= 1 and self.placed1 == False:
                        self.s1 = Button((64, 64, 64), 0, 0, 100, 50, '1x1')
                        self.s1.draw(self.win)
                        pygame.display.update()
                        self.placeShip(1)
                        self.placed1 = True
                        self.shipsSelected += 1

                    if self.s2.hover(pos) == True and self.shipCount >= 2 and self.placed2 is False:
                        self.s2 = Button((64, 64, 64), 0, 100, 200, 50, '1x2')
                        self.s2.draw(self.win)
                        pygame.display.update()
                        self.placeShip(2)
                        self.placed2 = True
                        self.shipsSelected += 1

                    if self.s3.hover(pos) == True and self.shipCount >= 3 and self.placed3 is False:
                        self.s3 = Button((64, 64, 64), 0, 200, 300, 50, '1x3')
                        self.s3.draw(self.win)
                        pygame.display.update()
                        self.placeShip(3)
                        self.placed3 = True
                        self.shipsSelected += 1

                    if self.s4.hover(pos) == True and self.shipCount >= 4 and self.placed4 is False:
                        self.s4 = Button((64, 64, 64), 0, 300, 400, 50, '1x4')
                        self.s4.draw(self.win)
                        pygame.display.update()
                        self.placeShip(4)
                        self.placed4 = True
                        self.shipsSelected += 1

                    if self.s5.hover(pos) == True and self.shipCount >= 5 and self.placed5 is False:
                        self.s5 = Button((64, 64, 64), 0, 400, 500, 50, '1x5')
                        self.s5.draw(self.win)
                        pygame.display.update()
                        self.placeShip(5)
                        self.placed5 = True
                        self.shipsSelected += 1

                    if self.s6.hover(pos) == True and self.shipCount is 6 and self.placed6 is False:
                        self.s6 = Button((64, 64, 64), 0, 500, 600, 50, '1x6')
                        self.s6.draw(self.win)
                        pygame.display.update()
                        self.placeShip(6)
                        self.placed6 = True
                        self.shipsSelected += 1

    # @pre - needs a ship to have already been selected
    # @param - ship length
    # @post - continuously draws a the ship on the cursor and the ship buttons and allows the user to rotate it until a
    # valid position is clicked on
    # @return - none
    def placeShip(self, shipNum):
        self.shipPlaced = False
        # boolean used to toggle between ship orientation
        vertical = False
        while self.shipPlaced is False:
            for event in pygame.event.get():
                pos = pygame.mouse.get_pos()
                # two if statements that draw the ship on the cursor each frame based on orientation
                if vertical is False:
                    pygame.draw.rect(self.win, (70, 70, 70), (pos[0] - 25, pos[1] - 25, 50 * shipNum, 50))
                if vertical is True:
                    pygame.draw.rect(self.win, (70, 70, 70), (pos[0] - 25, pos[1] - 25, 50, 50 * shipNum))
                pygame.display.update()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Left click: checks if valid placement then if so adds the ship to the list in that location
                    # JAKE D: We will need to add a condition here for passing in the CPUs ship selectment
                    if event.button == 1 and self.isValid(pos, vertical, shipNum):
                        if vertical:
                            self.shipList.append(Ship(self.row, self.column, self.row + shipNum - 1, self.column))
                        if not vertical:
                            self.shipList.append(Ship(self.row, self.column, self.row, self.column + shipNum - 1))
                        # print('placed')
                        self.shipPlaced = True
                    # Right click: rotates ship
                    if event.button == 3:
                        # print('rotated')
                        vertical = not vertical
                # redraws the buttons after the board has been refreshed. the board needs to refresh every frame
                # otherwise the ship following the cursor turns into a paint brush
                self.drawPlayerBoard()
                for i in range(self.shipCount + 1):
                    if i == 1:
                        self.s1.draw(self.win)

                    if i == 2:
                        self.s2.draw(self.win)

                    if i == 3:
                        self.s3.draw(self.win)

                    if i == 4:
                        self.s4.draw(self.win)

                    if i == 5:
                        self.s5.draw(self.win)

                    if i == 6:
                        self.s6.draw(self.win)

    # @pre - requires that the board is drawn correctly
    # @param - mouse position, a boolean of whether the ship is placed vertically and the size of the specific ship
    # @post - using the parameters given, this function decides if the user can place a piece there
    # @return - boolean of whether location is valid
    def isValid(self, pos, vertical, shipNum):
        validColumn = False
        validRow = False
        self.column = 0
        self.row = 0
        # checks if the cursor is on the board
        for i in range(10):
            if pos[0] >= (LEFT_PADDING + GRID_WIDTH + MIDDLE_PADDING + (i + 1) * SQUARE_SIZE) and pos[0] < (
                    LEFT_PADDING + GRID_WIDTH + MIDDLE_PADDING + (i + 2) * SQUARE_SIZE):
                validColumn = True
                self.column = i
                # print('column'+str(i))
        for j in range(10):
            if pos[1] >= (TOP_PADDING + (j + 1) * SQUARE_SIZE) and pos[1] < (TOP_PADDING + (j + 2) * SQUARE_SIZE):
                validRow = True
                self.row = j
                # print('row'+str(j))

        # checks if the part of the boat on different squares go past the bottom
        if vertical == True and shipNum + self.row > 10:
            validRow = False

        # checks if the part of the boat on different squares go past the side of the board
        if vertical == False and shipNum + self.column > 10:
            validColumn = False

        # check if vertical ship is going to overlap
        if vertical == True:
            for i in range(10):
                if i >= self.row and i < self.row + shipNum:
                    if self.shipArray[i][self.column] == 1:
                        validColumn = False
        # check if Horizontal ship is going to overlap
        if vertical == False:
            for i in range(10):
                if i >= self.column and i < self.column + shipNum:
                    if self.shipArray[self.row][i] == 1:
                        validRow = False

        if validColumn and validRow:
            # adds the valid ship to the array so future ships can be checked off of it and sends back a true
            if vertical == True:
                for i in range(10):
                    if i >= self.row and i < self.row + shipNum:
                        self.shipArray[i][self.column] = 1
            if vertical == False:
                for i in range(10):
                    if i >= self.column and i < self.column + shipNum:
                        self.shipArray[self.row][i] = 1

            for r in self.shipArray:
                for c in r:
                    pass
                    # print(c, end = " ")
                # print()

            return True
        else:
            return False

    # @pre - needs window to be defined and
    # @param - none
    # @post - Redraws the screen starting with a black fill, then the text, grid, then the ships on the board
    # @return - none
    def drawPlayerBoard(self):
        # whole method is a modified method from board that draws one board instead of two
        self.win.fill(BLACK)
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render("Right Click to Rotate", True, WHITE, RED)
        textRect = text.get_rect()
        textRect.center = ((WIDTH // 4) * 3, TOP_PADDING // 2)
        self.win.blit(text, textRect)
        pygame.draw.rect(self.win, BLUE,
                         (LEFT_PADDING + GRID_WIDTH + MIDDLE_PADDING, TOP_PADDING, GRID_WIDTH, GRID_HEIGHT))
        for i in range(11):
            # (win, color, (start X, start Y) , (end X, end Y))
            # horizontals
            pygame.draw.line(self.win, WHITE, (WIDTH - RIGHT_PADDING - GRID_WIDTH, TOP_PADDING + i * SQUARE_SIZE + 50),
                             (WIDTH - RIGHT_PADDING, TOP_PADDING + i * SQUARE_SIZE + 50))
            # verticals
            pygame.draw.line(self.win, WHITE, (WIDTH - RIGHT_PADDING - GRID_WIDTH + i * SQUARE_SIZE + 50, TOP_PADDING),
                             (WIDTH - RIGHT_PADDING - GRID_WIDTH + i * SQUARE_SIZE + 50, HEIGHT - BOTTOM_PADDING))

            if i != 0:
                font = pygame.font.Font('freesansbold.ttf', 32)
                txt = "" + str(i)
                text = font.render(txt, True, BLACK, BLUE)
                textRect = text.get_rect()

                # numbers in top row
                textRect.center = (LEFT_PADDING + GRID_WIDTH + MIDDLE_PADDING + i * SQUARE_SIZE + SQUARE_SIZE // 2,
                                   TOP_PADDING + SQUARE_SIZE // 2)
                self.win.blit(text, textRect)

                # letters on leftmost column
                txt = chr(64 + i)
                text = font.render(txt, True, BLACK, BLUE)
                textRect.center = (LEFT_PADDING + GRID_WIDTH + MIDDLE_PADDING + SQUARE_SIZE // 2,
                                   TOP_PADDING + i * SQUARE_SIZE + SQUARE_SIZE // 2)
                self.win.blit(text, textRect)
        # draws the placed ship objects
        for i in self.shipList:
            i.draw(True, self.win)

    # @pre - needs a list of ships
    # @param - no param
    # @post - returns the array of ship objects
    # @return - Returns list of ships
    def returnShip(self):
        return self.shipList
