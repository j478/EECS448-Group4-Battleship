import pygame, sys

from .button import Button
from .constants import *

class Initialize():

    def __init__(self, win):
        self.gameSizeSelected = False
        self.win = win

        b1 = Button((0,250,0), 0, 0, 500, 99, '1 Ship')
        b2 = Button((0,250,0), 0, 100, 500, 99, '2 Ship')
        b3 = Button((0,250,0), 0, 200, 500, 99, '3 Ship')
        b4 = Button((0,250,0), 0, 300, 500, 99, '4 Ship')
        b5 = Button((0,250,0), 0, 400, 500, 99, '5 Ship')
        b6 = Button((0,250,0), 0, 500, 500, 99, '6 Ship')

        
        self.placed1 = False
        self.placed2 = False
        self.placed3 = False
        self.placed4 = False
        self.placed5 = False
        self.placed6 = False


        
        while self.gameSizeSelected == False:
            pygame.display.update()
            b1.draw(win)
            b2.draw(win)
            b3.draw(win)
            b4.draw(win)
            b5.draw(win)
            b6.draw(win)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if b1.hover(pos) == True:
                        self.pickShips(1,win)
                        self.gameSizeSelected = True
                    if b2.hover(pos) == True:
                        self.pickShips(2,win)
                        self.gameSizeSelected = True
                    if b3.hover(pos) == True:
                        self.pickShips(3,win)
                        self.gameSizeSelected = True
                    if b4.hover(pos) == True:
                        self.pickShips(4,win)
                        self.gameSizeSelected = True
                    if b5.hover(pos) == True:
                        self.pickShips(5,win)
                        self.gameSizeSelected = True
                    if b6.hover(pos) == True:
                        self.pickShips(6,win)
                        self.gameSizeSelected = True
                        
                    print('mouse clicked')
                    
                    

    def pickShips (self, shipCount,win):
        self.shipsSelected = 0
        self.shipCount = shipCount
        self.s1 = Button((0,250,0), 0, 0, 100, 50, '1x1')
        self.s2 = Button((0,250,0), 0, 100, 200, 50, '1x2')
        self.s3 = Button((0,250,0), 0, 200, 300, 50, '1x3')
        self.s4 = Button((0,250,0), 0, 300, 400, 50, '1x4')
        self.s5 = Button((0,250,0), 0, 400, 500, 50, '1x5')
        self.s6 = Button((0,250,0), 0, 500, 600, 50, '1x6')
        pygame.draw.rect(win,(0,0,0),(0,0,1300, 800),0)
        self.drawPlayerBoard(win)
        
        for i in range(self.shipCount+1):
            if i == 1: 
                self.s1.draw(win)
                
            if i == 2:
                self.s2.draw(win)

            if i == 3:
                self.s3.draw(win)

            if i == 4: 
                self.s4.draw(win)

            if i == 5: 
                self.s5.draw(win)

            if i == 6:
                self.s6.draw(win)

        while self.shipsSelected < self.shipCount:
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if self.s1.hover(pos) == True and self.shipCount >= 1 and self.placed1 == False:
                        self.s1 = Button((64,64,64), 0, 0, 100, 50, '1x1')
                        self.s1.draw(win)
                        pygame.display.update()
                        self.placeShip(1,win)
                        self.placed1 = True
                        self.shipsSelected += 1

                    if self.s2.hover(pos) == True and self.shipCount >= 2 and self.placed2 is False:
                        self.s2 = Button((64,64,64), 0, 100, 200, 50, '1x2')
                        self.s2.draw(win)
                        pygame.display.update()
                        self.placeShip(2,win)
                        self.placed2 = True
                        self.shipsSelected += 1

                    if self.s3.hover(pos) == True and self.shipCount >= 3 and self.placed3 is False:
                        self.s3 = Button((64,64,64), 0, 200, 300, 50, '1x3')
                        self.s3.draw(win)
                        pygame.display.update()
                        self.placeShip(3,win)
                        self.placed3 = True
                        self.shipsSelected += 1


                    if self.s4.hover(pos) == True and self.shipCount >= 4 and self.placed4 is False:
                        self.s4 = Button((64,64,64), 0, 300, 400, 50, '1x4')
                        self.s4.draw(win)
                        pygame.display.update()
                        self.placeShip(4,win)
                        self.placed4 = True
                        self.shipsSelected += 1


                    if self.s5.hover(pos) == True and self.shipCount >= 5 and self.placed5 is False:
                        self.s5 = Button((64,64,64), 0, 400, 500, 50, '1x5')
                        self.s5.draw(win)
                        pygame.display.update()
                        self.placeShip(5,win)
                        self.placed5 = True
                        self.shipsSelected += 1


                    if self.s6.hover(pos) == True and self.shipCount is 6 and self.placed6 is False:
                        self.s6 = Button((64,64,64), 0, 500, 600, 50, '1x6')
                        self.s6.draw(win)
                        pygame.display.update()
                        self.placeShip(6,win)
                        self.placed6 = True
                        self.shipsSelected += 1

    def placeShip (self, shipNum,win):
        self.shipPlaced = False
        toggled = False
        while self.shipPlaced is False:
            for event in pygame.event.get():
                pos = pygame.mouse.get_pos()
                if toggled is False:
                    pygame.draw.rect(win,(70, 70, 70),(pos[0]-25,pos[1]-25,50*shipNum, 50))
                if toggled is True:
                    pygame.draw.rect(win,(70, 70, 70),(pos[0]-25,pos[1]-25,50, 50*shipNum))
                pygame.display.update()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    ##Left click
                    if event.button == 1:
                        print('placed')
                        self.shipPlaced = True
                    ##Right click
                    if event.button == 3:
                        print('rotated')
                        toggled = not toggled
                self.drawPlayerBoard(win)
                for i in range(self.shipCount+1):
                    if i == 1: 
                        self.s1.draw(win)
                
                    if i == 2:
                        self.s2.draw(win)

                    if i == 3:
                        self.s3.draw(win)

                    if i == 4: 
                        self.s4.draw(win)

                    if i == 5: 
                        self.s5.draw(win)

                    if i == 6:
                        self.s6.draw(win)


    def drawPlayerBoard (self,win):
        self.win.fill(BLACK)
        #pygame.draw.rect(self.win, BLUE, (LEFT_PADDING, TOP_PADDING, GRID_WIDTH, GRID_HEIGHT))
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


