import pygame
from .constants import *
from random import randint
import code

# When placing ships, randomly generate rows and columns.
# CPU should have a %age of a chance that it will place a ship horizontially
# CPU will recieve a difficulty level upon initialization
# CPU will then select shots based on that difficulty level

# member variables:
# needs to track if a previous shot was a hit or not
# needs to track if a ship has been sunk or not
# needs to be able to see the other player's ship locations(hard mode)

class CPU:
  def __init__(self, difficulty):
    self.difficulty = difficulty
    self.switcher = {
      1: self.easy_AI,
      2: self.mid_AI,
      3: self.hard_AI
    }
    self.last_shot = False
    self.current_ship_status = False
    self.found_ship = False
    self.found_direction = False
    self.last_hit = [0,0]
    self.first_hit = [0,0]
    self.ship_direction = [0,0]
    self.direction_counter = 1
    self.ship_count = 0
  
  def place_ships(self):
    vert = False;
    if randint(0,1) == 0:
      vert = True
    row = randint(0,9)
    col = randint(0,9)
    return(row,col,vert)

  def find_direction(self,first_hit,last_hit):
    if (first_hit - last_hit) < 0:
      direction = 1
    elif (first_hit - last_hit) > 0:
      direction = -1
    else:
      direction = 0
    return direction

  def CPU_update(self,hm,row,col):
    self.last_shot = hm
    if hm:
      if self.found_ship == False:
        print("we found a ship!")
        self.found_ship = True
        self.first_hit = [row,col]
        self.last_hit = [row,col]
        # self.current_ship_status = ship_status(this will be a parameter)
      #if self.current_ship_status == False:
        #print("The ship was sunk!")
        #self.found_direction = False
        #self.found_ship = False
        #self.ship_direction = [0,0]
        #self.last_hit = [0,0]
        #self.first_hit = [0,0]
      else:
        print("looking for direction!")
        self.last_hit = [row,col]
        self.ship_direction[0] = self.find_direction(self.first_hit[0],self.last_hit[0])
        self.ship_direction[1] = self.find_direction(self.first_hit[1],self.last_hit[1])
        if self.ship_direction[0] != 0 or self.ship_direction[1] != 0:
          self.found_direction = True

  def easy_AI(self):
    row = randint(0,9)
    col = randint(0,9)
    return(row,col)

  def mid_AI(self):
    if self.found_ship and self.current_ship_status:
      if self.last_shot and self.found_direction:
        print("razing ship")
        row = self.last_hit[0] + self.ship_direction[0]
        col = self.last_hit[1] + self.ship_direction[1]
      elif self.found_direction:
        print("trying other direction")
        row = self.first_hit[0] + self.ship_direction[0](-1)
        col = self.first_hit[1] + self.ship_direction[1]*(-1)
      else:
        if self.direction_counter == 1:
          print("checking UP")
          row = self.last_hit[0] + 1
          col = self.last_hit[1]
        if self.direction_counter == 2:
          print("checking RIGHT")
          row = self.last_hit[0]
          col = self.last_hit[1] + 1
        if self.direction_counter == 3:
          print("checking DOWN")
          row = self.last_hit[0] - 1
          col = self.last_hit[1]
        if self.direction_counter == 4:
          print("checking LEFT")
          row = self.last_hit[0]
          col = self.last_hit[1] - 1
      self.direction_counter += 1
    else:
      print("guessing random")
      row = randint(0,9)
      col = randint(0,9)
    return(row,col)
      
  def hard_AI(self):
    print("Hard Shot")
      
  def take_shot(self):
    return self.switcher[self.difficulty]()


bot = CPU(2)
bot.take_shot()
code.interact(local=locals())
