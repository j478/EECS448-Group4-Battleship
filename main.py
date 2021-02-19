#	Author: Jacob Wagner
#	Date: 2021.02.13

# this is a test for github. This is test part3
import pygame
from battleship.constants import WIDTH, HEIGHT
from battleship.board import *
from battleship.ship import Ship


FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Battleship')

pygame.init()

def main():
    running = True
    clock = pygame.time.Clock()
    p0ships = [Ship(0, 0, 0, 3), Ship(5, 5, 7, 5), Ship(1, 1, 1, 4)] 
    p1ships = [Ship(2, 2, 2, 5), Ship(4, 3, 4 ,5), Ship(8, 8, 6, 8)]
    board = Board(WIN, p0ships, p1ships)
    board.hit_ship(0, 2, 2)
    board.hit_ship(0, 3, 4)
    board.hit_ship(0, 6, 6)
    board.hit_ship(0, 7, 8)
    board.hit_ship(1, 5, 5)
    board.hit_ship(1, 4, 4,)
    board.hit_ship(1, 1, 3)
    board.draw(0)
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        board.update()

    pygame.quit()


main()
