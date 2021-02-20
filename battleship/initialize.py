import pygame, sys

from .button import Button
from .constants import *
from .ship import Ship
class Initialize():

    def __init__(self, win):
        self.gameSizeSelected = False
        self.win = win
        self.shipsSelected = 0
        self.shipCount = 0
        self.shipList = []

        self.b1 = Button((0,250,0), 0, 0, 500, 99, '1 Ship')
        self.b2 = Button((0,250,0), 0, 100, 500, 99, '2 Ship')
        self.b3 = Button((0,250,0), 0, 200, 500, 99, '3 Ship')
        self.b4 = Button((0,250,0), 0, 300, 500, 99, '4 Ship')
        self.b5 = Button((0,250,0), 0, 400, 500, 99, '5 Ship')
        self.b6 = Button((0,250,0), 0, 500, 500, 99, '6 Ship')

        
        self.placed1 = False
        self.placed2 = False
        self.placed3 = False
        self.placed4 = False
        self.placed5 = False
        self.placed6 = False

        self.s1 = Button((0,250,0), 0, 0, 100, 50, '1x1')
        self.s2 = Button((0,250,0), 0, 100, 200, 50, '1x2')
        self.s3 = Button((0,250,0), 0, 200, 300, 50, '1x3')
        self.s4 = Button((0,250,0), 0, 300, 400, 50, '1x4')
        self.s5 = Button((0,250,0), 0, 400, 500, 50, '1x5')
        self.s6 = Button((0,250,0), 0, 500, 600, 50, '1x6')

        self.shipArray =[[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
        self.gameSize()
                            
    def gameSize(self):
        while self.gameSizeSelected == False:
            pygame.display.update()
            self.b1.draw(self.win)
            self.b2.draw(self.win)
            self.b3.draw(self.win)
            self.b4.draw(self.win)
            self.b5.draw(self.win)
            self.b6.draw(self.win)
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

    def pickShips (self, shipCount):
        
        pygame.draw.rect(self.win,(0,0,0),(0,0,1300, 800),0)
        self.drawPlayerBoard()
        self.shipCount = shipCount
        for i in range(self.shipCount+1):
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

        while self.shipsSelected < self.shipCount:
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if self.s1.hover(pos) == True and self.shipCount >= 1 and self.placed1 == False:
                        self.s1 = Button((64,64,64), 0, 0, 100, 50, '1x1')
                        self.s1.draw(self.win)
                        pygame.display.update()
                        self.placeShip(1)
                        self.placed1 = True
                        self.shipsSelected += 1

                    if self.s2.hover(pos) == True and self.shipCount >= 2 and self.placed2 is False:
                        self.s2 = Button((64,64,64), 0, 100, 200, 50, '1x2')
                        self.s2.draw(self.win)
                        pygame.display.update()
                        self.placeShip(2)
                        self.placed2 = True
                        self.shipsSelected += 1

                    if self.s3.hover(pos) == True and self.shipCount >= 3 and self.placed3 is False:
                        self.s3 = Button((64,64,64), 0, 200, 300, 50, '1x3')
                        self.s3.draw(self.win)
                        pygame.display.update()
                        self.placeShip(3)
                        self.placed3 = True
                        self.shipsSelected += 1


                    if self.s4.hover(pos) == True and self.shipCount >= 4 and self.placed4 is False:
                        self.s4 = Button((64,64,64), 0, 300, 400, 50, '1x4')
                        self.s4.draw(self.win)
                        pygame.display.update()
                        self.placeShip(4)
                        self.placed4 = True
                        self.shipsSelected += 1


                    if self.s5.hover(pos) == True and self.shipCount >= 5 and self.placed5 is False:
                        self.s5 = Button((64,64,64), 0, 400, 500, 50, '1x5')
                        self.s5.draw(self.win)
                        pygame.display.update()
                        self.placeShip(5)
                        self.placed5 = True
                        self.shipsSelected += 1


                    if self.s6.hover(pos) == True and self.shipCount is 6 and self.placed6 is False:
                        self.s6 = Button((64,64,64), 0, 500, 600, 50, '1x6')
                        self.s6.draw(self.win)
                        pygame.display.update()
                        self.placeShip(6)
                        self.placed6 = True
                        self.shipsSelected += 1

    def placeShip (self, shipNum):
        self.shipPlaced = False
        vertical = False
        while self.shipPlaced is False:
            for event in pygame.event.get():
                pos = pygame.mouse.get_pos()
                if vertical is False:
                    pygame.draw.rect(self.win,(70, 70, 70),(pos[0]-25,pos[1]-25,50*shipNum, 50))
                if vertical is True:
                    pygame.draw.rect(self.win,(70, 70, 70),(pos[0]-25,pos[1]-25,50, 50*shipNum))
                pygame.display.update()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    ##Left click
                    if event.button == 1 and self.isValid(pos,vertical, shipNum):
                        if vertical:
                            self.shipList.append(Ship(self.row, self.column, self.row+shipNum-1, self.column)) 
                        if not vertical:
                            self.shipList.append(Ship(self.row, self.column, self.row, self.column+shipNum-1))
                        print('placed')
                        self.shipPlaced = True
                    ##Right click
                    if event.button == 3:
                        print('rotated')
                        vertical = not vertical
                self.drawPlayerBoard()
                for i in range(self.shipCount+1):
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

    def isValid(self,pos, vertical, shipNum):
        validColumn = False
        validRow = False
        self.column=0
        self.row=0
        for i in range(10):
            if pos[0] >= (LEFT_PADDING+GRID_WIDTH+MIDDLE_PADDING+(i+1)*SQUARE_SIZE) and pos[0] < (LEFT_PADDING+GRID_WIDTH+MIDDLE_PADDING+(i+2)*SQUARE_SIZE):
                validColumn = True
                self.column = i
                print('column'+str(i))
        for j in range(10):
            if pos[1] >=(TOP_PADDING+(j+1)*SQUARE_SIZE) and pos[1] <(TOP_PADDING+(j+2)*SQUARE_SIZE):
                validRow = True 
                self.row = j
                print('row'+str(j))

        #vertical check past bottom of board
        if vertical == True and shipNum + self.row > 10:
            validRow = False

        #horizontal check past side of board
        if vertical == False and shipNum + self.column > 10:
            validColumn = False

        #check if vertical ship is going to overlap
        if vertical == True:
            for i in range(10):
                if i >= self.row and i<self.row+shipNum:
                    if self.shipArray[i][self.column]== 1:
                        validColumn = False
        #check if Horizontal ship is going to overlap
        if vertical == False:
            for i in range(10):
                if i >= self.column and i<self.column+shipNum:
                    if self.shipArray[self.row][i] ==1:
                        validRow = False
        
        if validColumn and validRow:
            
            if vertical == True:
                for i in range(10):
                    if i >= self.row and i<self.row+shipNum:
                        self.shipArray[i][self.column]=1
            if vertical == False:
                for i in range(10):
                    if i >= self.column and i<self.column+shipNum:
                        self.shipArray[self.row][i]=1

            for r in self.shipArray:
                for c in r:
                    print(c, end = " ")
                print()

            return True
        else:
            return False

    def drawPlayerBoard (self):
        self.win.fill(BLACK)
        pygame.draw.rect(self.win, BLUE, (LEFT_PADDING + GRID_WIDTH + MIDDLE_PADDING, TOP_PADDING, GRID_WIDTH, GRID_HEIGHT))  
        for i in range(11):
            # (win, color, (start X, start Y) , (end X, end Y))
            #horizontals
            pygame.draw.line(self.win, WHITE, (WIDTH - RIGHT_PADDING - GRID_WIDTH, TOP_PADDING + i * SQUARE_SIZE + 50),
                                              (WIDTH - RIGHT_PADDING, TOP_PADDING + i * SQUARE_SIZE + 50))
            #verticals
            pygame.draw.line(self.win, WHITE, (WIDTH - RIGHT_PADDING - GRID_WIDTH + i * SQUARE_SIZE + 50, TOP_PADDING),
                                              (WIDTH - RIGHT_PADDING - GRID_WIDTH + i * SQUARE_SIZE + 50, HEIGHT - BOTTOM_PADDING))

            if i != 0:
                font = pygame.font.Font('freesansbold.ttf', 32)
                txt = "" + str(i)
                text = font.render(txt, True, BLACK, BLUE)
                textRect = text.get_rect()
                
                #numbers in top row
                textRect.center = (LEFT_PADDING + GRID_WIDTH + MIDDLE_PADDING + i * SQUARE_SIZE + SQUARE_SIZE // 2, TOP_PADDING + SQUARE_SIZE // 2)
                self.win.blit(text, textRect)

                #letters on leftmost column
                txt = chr(64 + i)
                text = font.render(txt, True, BLACK, BLUE)
                textRect.center = (LEFT_PADDING + GRID_WIDTH + MIDDLE_PADDING + SQUARE_SIZE // 2, TOP_PADDING + i * SQUARE_SIZE + SQUARE_SIZE // 2)
                self.win.blit(text, textRect)
                #65 - 74 65 = A, 74 = J from https://stackoverflow.com/questions/4528982/convert-alphabet-letters-to-number-in-python

        for i in self.shipList:
            i.draw(True,self.win)


    def returnShip(self):
        return self.shipList