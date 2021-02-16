#	Author: Jacob Wagner
#	Date: 2021.02.13

#this is a test for github. This is test part3
import pygame
from battleship.constants import WIDTH, HEIGHT
from battleship.board import *

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Battleship')

pygame.init()
def main():
    running = True
    clock = pygame.time.Clock()
    board = Board(WIN)
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        pygame.display.update()

    pygame.quit()

main()