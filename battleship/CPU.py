import pygame
from .constants import *
from random import randint

# When placing ships, randomly generate rows and columns.
# CPU should have a %age of a chance that it will place a ship horizontially
# CPU will recieve a difficulty level upon initialization
# CPU will then select shots based on that difficulty level

# member variables:
# needs to track if a previous shot was a hit or not
# needs to track if a ship has been sunk or not
# needs to be able to see the other player's ship locations(hard mode)

class MyAI:
  def __init__(self, difficulty):
    self.difficulty = difficulty
    self.switcher = {
      1: self.easy_AI,
      2: self.mid_AI,
      3: self.hard_AI
    }
    self.last_shot = False
    self.current_ship_status = False
    self.current_ship_direction = 0
    self.last_hit = []
    self.stored_coord = []
    self.dir = []
    self.dir_counter = 1
    self.ship_count = 0
  
  def place_ships(self):
    vert = False;
    if randint(0,1) == 0:
      vert = True
    row = randint(0,9)
    col = randint(0,9)
    return(row,col,vert)

  def CPU_update(self,hm,row,col):
    self.last_shot = hm
    self.stored_coord[0] = self.last_hit[0]
    self.stored_coord[1] = self.last_hit[1]
    self.last_hit[0]= row
    self.last_hit[1] = col
    if hm:
      self.dir[0] = max(self.last_hit[0],self.stored_coord[0]) - min(self.last_hit[0],self.stored_coord[0])
      self.dir[1] = max(self.last_hit[1],self.stored_coord[1]) - min(self.last_hit[1],self.stored_coord[1])
    # check for if current ship has been sunk

  def easy_AI(self):
    row = randint(0,9)
    col = randint(0,9)
    #compare row and col to ensure it is not a repeated staticmethod
    return(row,col)

  def mid_AI(self):
    if self.last_shot and self.current_ship_status:
      if self.current_ship_direction:
        row = self.last_hit[0] + self.dir[0]
        col = self.last_hit[1] + self.dir[1]
      else:
        if self.dir_counter == 1:
          row = self.last_hit[0] + 1
          col = self.last_hit[1]
        if self.dir_counter == 2:
          row = self.last_hit[0]
          col = self.last_hit[1] + 1
        if self.dir_counter == 3:
          row = self.last_hit[0] - 1
          col = self.last_hit[1]
        if self.dir_counter == 4:
          row = self.last_hit[0]
          col = self.last_hit[1] - 1
      self.dir_counter += self.dir_counter
    else:
      row = randint(0,9)
      col = randint(0,9)
    return(row,col)
      
  def hard_AI(self):
    print("Hard Shot")
      
  def take_shot(self):
    return self.switcher[self.difficulty]()
