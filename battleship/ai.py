import pygame
import random #random library
import .ship import Ship
#random number generator: random.randint(1, 10)
#random choice generator (used for rotation): random.choice(['h', 'v'])

class AI:
    # @pre -
    # @param -
    # @post -
    # @return -
    # return true if hit, false if not
    def is_hit():
    # @pre -
    # @param -
    # @post -
    # @return -
    # return true if hit, false if not
    def is_placed(rot,row,col):
    # @pre -
    # @param -
    # @post -
    # @return -
    #take row from random number_generator
    #take col from random number_generator
    #take rotation from random random_rotation
    # fire at that position
    def easy_mode():
    # @pre -
    # @param -
    # @post -
    # @return -
    # do what easy_mode does until a spot is hit
    def med_mode():
    # @pre -
    # @param -
    # @post -
    # @return -
    # read the player's board and attak
    def hard_mode():
    def is_valid():
    # @pre -
    # @param -
    # @post -
    # @return -
    # AI place ship at the begining of the game
    def place_ship(self, shipNum):
    rot = random.choice(['h', 'v'])
    row = random.randint(1, 10)
    col = random.randint(1, 10)
    while (is_valid(rot, row, col)==false):
        rot = random.choice(['h', 'v'])
        row = random.randint(1, 10)
        col = random.randint(1, 10)
    if rot=='v':
        Ship(row, column, row + shipNum - 1, column))
    else:
        Ship(row, column, row, column + shipNum - 1))
      
        
