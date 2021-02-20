#	Author: Jacob Wagner
#	Date: 2021.02.13

import pygame
from battleship.constants import WIDTH, HEIGHT
from battleship.board import *
from battleship.initialize import *
from battleship.ship import Ship
from battleship.game import Game


FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Battleship')


pygame.init()

def winner(game):

    if game.player_0_ships == 0: 
        player = 1
    else:
        player = 0
    WIN.fill(BLACK)
        
    font = pygame.font.Font('freesansbold.ttf', 50)  # https://www.geeksforgeeks.org/python-display-text-to-pygame-window/
    text = font.render(f'Player {player +1} WON!', True, WHITE, RED)
    textRect = text.get_rect()
    textRect.center = (WIDTH // 2, HEIGHT // 2)
    WIN.blit(text, textRect)
    pygame.display.update()
    time.sleep(10)

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

   # board = Board(WIN, p0ships, p1ships)
    game = Game(WIN, p0ships, p1ships)
    
    
    while running:
        clock.tick(FPS)


        if game.game_over():
            winner(game)
            running = False



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                game.select(pos)

        game.update()

        

    pygame.quit()


main()


