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
                    if b1.hover == True:
                        pickShips(1)
                    if b2.hover == True:
                        pickShips(2)
                    if b3.hover == True:
                        pickShips(3)
                    if b4.hover == True:
                        pickShips(4)
                    if b5.hover == True:
                        pickShips(5)
                    if b6.hover == True:
                        pickShips(6)
                    print('mouse clicked')
                    self.gameSizeSelected = True

    def pickShips (self, shipCount):
        print (shipCount)