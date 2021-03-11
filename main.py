# Author: Jacob Wagner
# Date: 2021.02.13

import pygame
from battleship.constants import WIDTH, HEIGHT
from battleship.board import *
from battleship.initialize import *
from battleship.ship import Ship
from battleship.game import Game
from battleship.CPU import CPU

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Battleship')
pygame.init()


# @pre - will print to the screen the winner of the game if the proper stipulations are met
# @param - Game class
# @post - prints to the screen the winner and ends the game
# @return - None
def winner(game):
    if game.player_0_ships == 0:
        player = 1
    else:
        player = 0
    WIN.fill(BLACK)

    font = pygame.font.Font('freesansbold.ttf',
                            50)  # https://www.geeksforgeeks.org/python-display-text-to-pygame-window/
    text = font.render(f'Player {player + 1} WON!', True, WHITE, RED)
    textRect = text.get_rect()
    textRect.center = (WIDTH // 2, HEIGHT // 2)
    WIN.blit(text, textRect)
    pygame.display.update()
    time.sleep(4)


# @pre - starts the game loop of updating the model and rendering the screen
# @param - None
# @post - determines if the game should be over. If one of the players has 0 ships left, game ends
# @return - None
def main():
    running = True
    clock = pygame.time.Clock()


    ai=CPU(None)
    initial1 = Initialize(WIN, True, 0,None, ai)
    initial2 = Initialize(WIN, False, initial1.shipCount, None, ai)

    if initial1.active==True
        initial2.active=True

    p0ships = initial1.returnShip()
    p1ships = initial2.returnShip()
    #this can be left unchanged as long as we allow the CPU to change the shiplist
    
    game = Game(WIN, p0ships, p1ships, initial1.active, ai)
    game.switch_players()
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
