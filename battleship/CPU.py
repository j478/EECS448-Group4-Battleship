import pygame
from .constants import *
import random
from .ship import Ship
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
    # @pre - AI mode is activated, player selected level of difficulty
    # @param - AI mode difficulty
    # @post - AI mode is initialized
    # @return - none
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
        self.active = False
        self.vert =[]
        self.row =[]
        self.col =[]
        self.other_ships = []

    # @pre - AI mode is activated
    # @param - none
    # @post - AI ships placed on game board
    # @return - none
    def place_ship(self,index,counter):
        vert = False
        if random.randint(0, 1) == 0:
            vert=True

        row = random.randint(0, 9)
        col = random.randint(0, 9)
        while ((row+self.ship_count-index)>9 and vert==False):
            row=random.randint(0,9)
        while ((col+self.ship_count-index)>9 and vert == True):
            col=random.randint(0,9)

        if counter==0:
            self.vert.append(vert)
            self.row.append(row)
            self.col.append(col)
        else:
            self.col[index]=col
            self.row[index]=row
            self.vert[index]=vert
        print("Demo mode: CPU placed ship at row ", row, ", col ", col, "i= ", index, "  Vert: ", vert)

    # @pre - AI mode is activated
    # @param - first hit, last hit
    # @post - the direction of medium hit is set
    # @return - direction of ship
    def find_direction(self,first_hit,last_hit):
        if (first_hit - last_hit) < 0:
            direction = 1
        elif (first_hit - last_hit) > 0:
            direction = -1
        else:
            direction = 0
        return direction

    # @pre - AI mode is activated
    # @param - hit/miss, row, column, is destroyed (true false)
    # @post - Update the player on AI status
    # @return - none
    def CPU_update(self, hm, row, col, is_destroyed):
        self.last_shot = hm
        self.current_ship_status = is_destroyed
        if hm:
            if self.found_ship == False:
                # print("we found a ship!")
                self.found_ship = True
                self.first_hit = [row, col]
                self.last_hit = [row, col]
            if self.current_ship_status:
                # print("The ship was sunk!")
                self.found_direction = False
                self.found_ship = False
                self.current_ship_status = False
                self.last_shot = False
                self.direction_counter = 1
                self.ship_direction = [0,0]
                self.last_hit = [0,0]
                self.first_hit = [0,0]
            if self.found_ship and self.current_ship_status is False:
                #print("looking for direction!")
                self.last_hit = [row, col]
                self.ship_direction[0] = self.find_direction(self.first_hit[0], self.last_hit[0])
                self.ship_direction[1] = self.find_direction(self.first_hit[1], self.last_hit[1])
                if self.ship_direction[0] != 0 or self.ship_direction[1] != 0:
                    self.found_direction = True

    # @pre - AI mode is activated, player selected level of difficulty
    # @param - self
    # @post - AI fires at the player's board
    # @return - the location of where the cpu will fire at
    def easy_AI(self):
        row = random.randint(0, 9)
        col = random.randint(0, 9)
        return (row, col)

    # @pre - AI mode is activated, player selected level of difficulty
    # @param - self
    # @post - AI fires at the player's board
    # @return - the location of where cpu will fire at
    def mid_AI(self):
        if self.found_ship and self.current_ship_status is False:
            if self.last_shot and self.found_direction:
                # print("razing ship")
                row = self.last_hit[0] + self.ship_direction[0]
                col = self.last_hit[1] + self.ship_direction[1]
                if (row < 0 or row > 9) or (col < 0 or col > 9):
				    row = self.first_hit[0] + self.ship_direction[0] * (-1)
					col = self.first_hit[1] + self.ship_direction[1] * (-1)
            elif self.found_direction:
                # print("trying other direction")
                row = self.first_hit[0] + self.ship_direction[0] * (-1)
                col = self.first_hit[1] + self.ship_direction[1] * (-1)
            else:
                if self.direction_counter == 1 and self.last_hit[0] is not 0:
                    # print("checking UP")
                    row = self.last_hit[0] - 1
                    col = self.last_hit[1]
                if self.direction_counter == 2 and self.last_hit[1] is not 9:
                    # print("checking RIGHT")
                    row = self.last_hit[0]
                    col = self.last_hit[1] + 1
                if self.direction_counter == 3 and self.last_hit[0] is not 9:
                    # print("checking DOWN")
                    row = self.last_hit[0] + 1
                    col = self.last_hit[1]
                if self.direction_counter == 4 and self.last_hit[1] is not 0:
                    # print("checking LEFT")
                    row = self.last_hit[0]
                    col = self.last_hit[1] - 1
            self.direction_counter += 1
        else:
            row = random.randint(0, 9)
            col = random.randint(0, 9)
        return row, col

    # @pre - AI mode is activated, player selected level of difficulty
    # @param - self
    # @post - AI fires at the player's board
    # @return - none
    def hard_AI(self):
        # print("Hard Shot")
        for ship in self.other_ships:
            for coord in ship.locations:
                if coord[2] != True:
                    return coord[0],coord[1]

    # @pre - AI mode is activated
    # @param - self
    # @post -
    # @return -
    def take_shot(self):
        return self.switcher[self.difficulty]()

# Note that the below lines broke the game when they were uncommented.
# bot = CPU(2)
# bot.take_shot()
# code.interact(local=locals())
