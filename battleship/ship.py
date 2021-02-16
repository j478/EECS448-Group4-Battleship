#	Author: 
#	Date: 
import pygame
from .constants import SQUARE_SIZE
WHITE = (255,255,255)
class Ship:

    def __init__(self, start_r, start_c, end_r, end_c):
        self.ship = []
        self.start_r = start_r
        self.start_c = start_c
        self.end_r = end_r
        self.end_c = end_c
        self.destroyed = False
        
        #determine if horizontal or vertical
        if self.start_r == self.end_r:
            self.horizontal = True
        else:
            self.horizontal = False
        
        #determine size of ship
        if self.horizontal:
            self.size = abs((self.end_c + 1) - self.start_c) 
        else:
            self.size = abs((self.end_r + 1) - self.start_r)
    
        #fill ship array
        for i in range(self.size):
            if self.horizontal:
                self.ship.append(tuple((self.start_r, self.start_c + i, False)))
            else:
                self.ship.append(tuple((self.start_r + i, self.start_c, False)))


    def draw(self, win):
        square = SQUARE_SIZE
        pygame.draw.rect(win, WHITE,(100,100,SQUARE_SIZE,SQUARE_SIZE))

    def mark_hit(self, row, col):
        for i in range(self.size):
            part = self.ship[i]
            part_list = list(part)
            if (part_list[0] == row and part_list[1] == col):
                part_list[2] = True
                part = tuple(part_list)
                self.ship[i] = part

        