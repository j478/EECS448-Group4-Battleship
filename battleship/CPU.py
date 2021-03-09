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

class CPU:
  def __init__(self, difficulty):
    self.difficulty = difficulty
    self.switcher = {
      1: self.easy_AI,
      2: self.mid_AI,
      3: self.hard_AI
    }
    self.last_shot = False
    self.last_row = 0
    self.last_col = 0

  def easy_AI(self):
    row = randint(0,9)
    col = randint(0,9)
    return(row,col)

  def mid_AI(self):
    print("Med Shot")
      
  def hard_AI(self):
    print("Hard Shot")
      
  def take_shot(self):
    return self.switcher[self.difficulty]()
