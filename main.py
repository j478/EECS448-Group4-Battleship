#	Author: Jacob Wagner
#	Date: 2021.02.13

import pygame
from battleship.constants import WIDTH, HEIGHT
from battleship.board import *
from battleship.initialize import *
from battleship.ship import Ship


FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Battleship')


pygame.init()

def main():
    running = True
    clock = pygame.time.Clock()

    
    initial1 = Initialize(WIN, True, 0)

    initial2 = Initialize(WIN, False, initial1.shipCount)

    p0ships = initial1.returnShip() 
    p1ships = initial2.returnShip()
    
    board = Board(WIN, p0ships, p1ships)
    board.hit_ship(0, 2, 2)
    board.hit_ship(0, 3, 4)
    board.hit_ship(0, 6, 6)
    board.hit_ship(0, 7, 8)
    board.hit_ship(0, 0, 0)
    board.hit_ship(0, 4, 4)
    board.hit_ship(1, 5, 5)
    board.hit_ship(1, 4, 4)
    board.hit_ship(1, 1, 3)
    board.hit_ship(1, 6, 6)
    board.hit_ship(1, 2, 2)
    board.hit_ship(1, 0, 1)
    board.draw(0)

    
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        board.update(0)

    pygame.quit()


main()


