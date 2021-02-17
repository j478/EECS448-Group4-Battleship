#	Author: Jacob Wagner
#	Date: 2021.02.13

# this is a test for github. This is test part3
import pygame
from battleship.constants import WIDTH, HEIGHT
from battleship.board import *


FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Battleship')

pygame.init()

board = Board(WIN)

user_ship = Ship(0, 1, 0, 3)
enemy_ship = Ship(1, 1, 1, 3)

# 0 hitting 1
board.hit_ship(0, 0, 1, user_ship)

# 1 hitting 0
board.hit_ship(1, 1, 1, enemy_ship)

# 0 attempt to hit 1 but missed
board.hit_ship(0, 0, 8, user_ship)

# 1 attempt to hit 0 but missed
board.hit_ship(1, 1, 9, enemy_ship)



def main():
    running = True
    clock = pygame.time.Clock()

    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()

    pygame.quit()


main()
