#	Author: Jacob Wagner
#	Date: 2021.02.13

#this is a test for github. This is test part3
import pygame
from battleship.constants import WIDTH, HEIGHT
from battleship.board import *
from battleship.initialize import *

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Battleship')

initial = Initialize(WIN)
board = Board(WIN)

# random test points
test = Board(WIN)
test.hit_ship(1, 1, enemy=False)
test.draw_background(WIN)
test.hit_ship(0, 0, enemy=True)
test.draw_background(WIN)
test.hit_ship(9, 9, enemy=True)
test.draw_background(WIN)
test.hit_ship(5, 5, enemy=True)
test.draw_background(WIN)
test.hit_ship(4, 4, enemy=True)
test.draw_background(WIN)
test.hit_ship(4, 4, enemy=False)
test.draw_background(WIN)
test.hit_ship(0, 8, enemy=False)
test.draw_background(WIN)
test.hit_ship(4, 5, enemy=False)
test.draw_background(WIN)
pygame.display.update()


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
