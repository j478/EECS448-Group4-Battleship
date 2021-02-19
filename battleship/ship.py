#	Author: 
#	Date: 
import pygame

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
            self.size = abs(self.end_c - self.start_c) 
        else:
            self.size = abs(self.end_r - self.start_r)
    
        #fill ship array
        for i in range(self.size):
            if self.horizontal:
                self.ship.append(tuple((self.start_r, self.start_c + i, False)))
            else:
                self.ship.append(tuple(self.start_r + i, self.start_c, False))

    def draw(self, win):
        square = SQUARE_SIZE
        pygame.draw.ellipse(win, WHITE, (self.start_c*square, self.start_r*square, self.end_c * square, self.end_r*square))

    def mark_hit(self, row, col):
        for i in range(self.size):
            part = self.ship[i]
            part_list = list(part)
            if (part_list[0] == row and part_list[1] == col):
                part_list[2] = True
                part = tuple(part_list)
                self.ship[i] = part

    def get_x_y(self):
        x = (self.end_c*SQUARE_SIZE - self.start_r*SQUARE_SIZE)//2
        y = (self.end_r*SQUARE_SIZE - self.start_r*SQUARE_SIZE)//2
        return x,y   
                
        