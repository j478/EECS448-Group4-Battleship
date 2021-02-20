import pygame, sys

from .button import Button

class Initialize():

    def __init__(self, win):
        self.gameSizeSelected = False
        
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
        s1 = Button((0,250,0), 0, 0, 100, 50, 'Jet ski')
        s2 = Button((0,250,0), 0, 100, 200, 50, 'Destroyer')
        s3 = Button((0,250,0), 0, 200, 300, 50, 'Submarine')
        s4 = Button((0,250,0), 0, 300, 400, 50, 'Cruiser')
        s5 = Button((0,250,0), 0, 400, 500, 50, 'Battle Ship')
        s6 = Button((0,250,0), 0, 500, 600, 50, 'Carrier')
        pygame.draw.rect(win,(0,0,0),(0,0,1300, 800),0)
        
        for i in range(shipCount+1):
            if i is 1: 
                s1.draw(win)
            
            if i is 2:
                s2.draw(win)

            if i is 3:
                s3.draw(win)

            if i is 4: 
                s4.draw(win)

            if i is 5: 
                s5.draw(win)

            if i is 6:
                s6.draw(win)

        while self.shipsSelected < shipCount:
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if s1.hover(pos) == True and shipCount >= 1 and self.placed1 is False:
                        s1 = Button((64,64,64), 0, 0, 100, 50, 'Jet ski')
                        s1.draw(win)
                        pygame.display.update()
                        self.placed1 = True
                        self.shipsSelected += 1

                    if s2.hover(pos) == True and shipCount >= 2 and self.placed2 is False:
                        s2 = Button((64,64,64), 0, 100, 200, 50, 'Destroyer')
                        s2.draw(win)
                        pygame.display.update()
                        self.placed2 = True
                        self.shipsSelected += 1

                    if s3.hover(pos) == True and shipCount >= 3 and self.placed3 is False:
                        s3 = Button((64,64,64), 0, 200, 300, 50, 'Submarine')
                        s3.draw(win)
                        pygame.display.update()
                        self.placed3 = True
                        self.shipsSelected += 1


                    if s4.hover(pos) == True and shipCount >= 4 and self.placed4 is False:
                        s4 = Button((64,64,64), 0, 300, 400, 50, 'Cruiser')
                        s4.draw(win)
                        pygame.display.update()
                        self.placed4 = True
                        self.shipsSelected += 1


                    if s5.hover(pos) == True and shipCount >= 5 and self.placed5 is False:
                        s5 = Button((64,64,64), 0, 400, 500, 50, 'Battle Ship')
                        s5.draw(win)
                        pygame.display.update()
                        self.placed5 = True
                        self.shipsSelected += 1


                    if s6.hover(pos) == True and shipCount is 6 and self.placed6 is False:
                        s6 = Button((64,64,64), 0, 500, 600, 50, 'Carrier')
                        s6.draw(win)
                        pygame.display.update()
                        self.placed6 = True
                        self.shipsSelected += 1

                    