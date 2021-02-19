import pygame
import sys

WIDTH, HEIGHT = 1200, 650

#SQUARE_SIZE = 50

WIDTH, HEIGHT = 1300, 800

ROWS, COLS = 10, 10
SQUARE_SIZE = WIDTH//COLS

# COLORS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GRAY = (128, 128, 128)
BLUE = (0, 0, 204)

# BOARD
BOARD_LAYOUT = "battleship/board_layout.txt"
BOARD_LAYOUT_test = "../board_layout.txt"

BLACK = (0, 0, 0)           # Background color
GRAY = (128, 128, 128)      # Default color of tile
DGRAY = (64, 64, 64)
RED = (255, 0, 0)           # Missed an attack
BLUE = (0, 170, 204)          
WHITE = (255, 255, 255)     # Grid line colors
GREEN = (0, 128, 0)         # Successfully hit enemy's ship

#printing constants
LEFT_PADDING = 25
RIGHT_PADDING = 25
MIDDLE_PADDING = 50 
TOP_PADDING = 75
BOTTOM_PADDING = 25
GRID_WIDTH = 550
GRID_HEIGHT = 550
