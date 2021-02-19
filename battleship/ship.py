#	Author: 
#	Date: 
import pygame
from .constants import *

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
            self.size = abs(self.end_c - self.start_c) + 1
        else:
            self.size = abs(self.end_r - self.start_r) + 1
    
        #fill ship array
        for i in range(self.size):
            if self.horizontal:
                self.ship.append(tuple((self.start_r, self.start_c + i, False)))
            else:
                self.ship.append(tuple((self.start_r + i, self.start_c, False)))

    def draw(self, right, win): #right is a boolean which if True means draw on the right 
        #pygame.draw.rect(self.win, GRAY, (LEFT_PADDING, TOP_PADDING, GRID_WIDTH, GRID_HEIGHT))
        if right:
            if self.horizontal:
                pygame.draw.ellipse(win, BLACK, ( (WIDTH - RIGHT_PADDING - GRID_WIDTH + 50) + min(self.start_c, self.end_c) * SQUARE_SIZE, 
                                   (TOP_PADDING + 50) + min(self.start_r, self.end_r) * SQUARE_SIZE, self.size * SQUARE_SIZE, SQUARE_SIZE))
                pygame.draw.ellipse(win, DGRAY, ( (WIDTH - RIGHT_PADDING - GRID_WIDTH + 50) + min(self.start_c, self.end_c) * SQUARE_SIZE + SQUARE_SIZE // 15, 
                                   (TOP_PADDING + 50) + min(self.start_r, self.end_r) * SQUARE_SIZE + SQUARE_SIZE // 15, self.size * SQUARE_SIZE - SQUARE_SIZE // 3, SQUARE_SIZE - SQUARE_SIZE // (self.size * 3)))
            else:
                pygame.draw.ellipse(win, BLACK, ( (WIDTH - RIGHT_PADDING - GRID_WIDTH + 50) + min(self.start_c, self.end_c) * SQUARE_SIZE + SQUARE_SIZE, 
                                   (TOP_PADDING + 50) + min(self.start_r, self.end_r) * SQUARE_SIZE, SQUARE_SIZE, self.size * SQUARE_SIZE))
                pygame.draw.ellipse(win, DGRAY, ( (WIDTH - RIGHT_PADDING - GRID_WIDTH + 50) + min(self.start_c, self.end_c) * SQUARE_SIZE + SQUARE_SIZE + SQUARE_SIZE //15, 
                                   (TOP_PADDING + 50) + min(self.start_r, self.end_r) * SQUARE_SIZE + SQUARE_SIZE // 15, SQUARE_SIZE - SQUARE_SIZE // (self.size * 3), self.size * SQUARE_SIZE - SQUARE_SIZE// 3))
        else:
                if self.horizontal:
                    pygame.draw.ellipse(win, BLACK, ( (LEFT_PADDING + 50) + min(self.start_c, self.end_c) * SQUARE_SIZE, 
                                       (TOP_PADDING + 50) + min(self.start_r, self.end_r) * SQUARE_SIZE, self.size * SQUARE_SIZE, SQUARE_SIZE))
                else:
                    pygame.draw.ellipse(win, BLACK, ( (LEFT_PADDING + 50) + min(self.start_c, self.end_c) * SQUARE_SIZE, 
                                       (TOP_PADDING + 50) + min(self.start_r, self.end_r) * SQUARE_SIZE, SQUARE_SIZE, self.size * SQUARE_SIZE))

    def mark_hit(self, row, col):
        for i in range(self.size):
            part = self.ship[i]
            part_list = list(part)
            if (part_list[0] == row and part_list[1] == col):
                part_list[2] = True
                part = tuple(part_list)
                self.ship[i] = part

    def get_x_y(self): ##NOT Necessary anymore
        x = (self.end_c*SQUARE_SIZE - self.start_r*SQUARE_SIZE)//2
        y = (self.end_r*SQUARE_SIZE - self.start_r*SQUARE_SIZE)//2
        return x,y   

    def is_destroyed(self):
        for loc in self.ship:
            if loc[2] == False
            return False
        return True

                
    