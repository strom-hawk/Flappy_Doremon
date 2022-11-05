import random
import sys
import pygame
import pygame.locals 
# import *

# GLOBAL VARIABLES
FPS = 32
SCREEN_WIDTH = 289
SCREEN_HEIGHT = 511
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
GROUND_Y = SCREEN_HEIGHT * 0.8
GAME_SPRITES = {}
GAME_SOUND = {}
PLAYER = '/resources/sprites/bird.png'
BACKGROUND = '/resources/sprites/background.png'
PIPE = '/resources/sprites/pipe.png'

if __name__ == "__main__":
    # This will be the main function from where game will start
    pygame.init()
    pygame.display.set_caption("Py Game")
    FPSCLOCK = pygame.time.Clock()
    GAME_SPRITES['numbers'] = {
        pygame.image.load('/resources/sprites/0.png').convert_alpha(),
        pygame.image.load('/resources/sprites/1.png').convert_alpha(),
        pygame.image.load('/resources/sprites/2.png').convert_alpha(),
        pygame.image.load('/resources/sprites/3.png').convert_alpha(),
        pygame.image.load('/resources/sprites/4.png').convert_alpha(),
        pygame.image.load('/resources/sprites/5.png').convert_alpha(),
        pygame.image.load('/resources/sprites/6.png').convert_alpha(),
        pygame.image.load('/resources/sprites/7.png').convert_alpha(),
        pygame.image.load('/resources/sprites/8.png').convert_alpha(),
        pygame.image.load('/resources/sprites/9.png').convert_alpha(),
    }