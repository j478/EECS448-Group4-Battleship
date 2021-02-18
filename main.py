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


#player 0 = user, player 1 = enemy
board = Board(WIN)
u_ship = Ship(7, 1, 7, 3)   # Player 0
e_ship = Ship(1, 1, 1, 3)   # Player 1

# Player 0 turn to attack Player 1. Draws Player 0 ships (LEFT)
board.draw(0, u_ship)
# Player 0 picks coordinate to attack Player 1. Green success, red miss (GREEN)
board.hit_ship(0, 1, 1, e_ship)
# Player 0 board cleared. Player 1 turn next.
board.clear_ships(0, u_ship)
# Player 1 turn to attack Player 0. Draws Player 1 ships (RIGHT)
board.draw(1, e_ship)
# Player 1 picks coordinate to attack Player 0. Green success, red miss (GREEN)
board.hit_ship(1, 7, 1, u_ship)
# Player 1 board cleared. Player 0 turn next.
board.clear_ships(1, e_ship)
# Player 0 turn to attack Player 1. Draws Player 0 ships (LEFT)
board.draw(0, u_ship)
# Player 0 picks coordinate to attack Player 1. Green success, red miss (RED)
board.hit_ship(0, 8, 8, e_ship)
# Player 0 board cleared. Player 1 turn next.
board.clear_ships(0, u_ship)
# Player 1 turn to attack Player 0. Draws Player 1 ships (RIGHT)
board.draw(1, e_ship)
# Player 1 picks coordinate to attack Player 0. Green success, red miss (RED)
board.hit_ship(1, 0, 2, u_ship)

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
