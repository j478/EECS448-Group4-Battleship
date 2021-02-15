#	Author: 
#	Date: 
import pygame

class Ship:

    def __init__(self, start_x, start_y, end_x, end_y):
        self.ship = []
        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y
        self.destroyed = False
        
        #determine if horizontal or vertical
        if self.start_x == self.end_x:
            self.horizontal = False
        elif self.start_y == self.end_y:
            self.horizontal = True
        
        #determine size of ship
        if self.horizontal:
            self.size = (self.end_x + 1) - self.start_x
        else:
            self.size = (self.end_y + 1) - self.start_y
    
        #fill ship array
        if self.horizontal == True:
            for col in range(self.size):
                self.ship.append(tuple((self.start_y,self.start_x + col,False)))
        elif self.horizontal == False:
            for row in range(self.size):
                self.ship.append(tuple((self.start_y + row, start_x, False)))
                
        