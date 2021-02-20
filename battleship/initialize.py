import pygame

from .button import Button

def __init__(self, window)
    self.win = window
    self.gameSizeSelected = False
    b1 = Button((0,250,0), 0, 0, 100, 100, text='1 Ship')
    b2 = Button((0,250,0), 0, 100, 100, 100, text='2 Ship')
    b3 = Button((0,250,0), 0, 200, 100, 100, text='3 Ship')
    b4 = Button((0,250,0), 0, 300, 100, 100, text='4 Ship')
    b5 = Button((0,250,0), 0, 400, 100, 100, text='5 Ship')
    b6 = Button((0,250,0), 0, 500, 100, 100, text='6 Ship')
    while (gameSizeSelected = False)
        ev = pygame.event.get()
        b1.draw(win)
        b2.draw(win)
        b3.draw(win)
        b4.draw(win)
        b5.draw(win)
        b6.draw(win)
        if event.type == pygame.MOUSEBUTTONDOWN
            gamesizeSelected = True