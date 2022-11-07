import random
import sys
import pygame
from pygame.locals import *

# GLOBAL VARIABLES
FPS = 32
SCREEN_WIDTH = 289
SCREEN_HEIGHT = 511
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
GROUND_Y = SCREEN_HEIGHT * 0.8
GAME_SPRITES = {}
GAME_SOUND = {}
PLAYER = 'resources/sprites/bird.png'
BACKGROUND = 'resources/sprites/background.png'
PIPE = 'resources/sprites/pipe.png'


if __name__ == "__main__":
    # This will be the main function from where game will start
    pygame.init()
    pygame.display.set_caption("Py Game")
    FPSCLOCK = pygame.time.Clock()
    GAME_SPRITES['numbers'] = {
        pygame.image.load('resources/sprites/0.png').convert_alpha(),
        pygame.image.load('resources/sprites/1.png').convert_alpha(),
        pygame.image.load('resources/sprites/2.png').convert_alpha(),
        pygame.image.load('resources/sprites/3.png').convert_alpha(),
        pygame.image.load('resources/sprites/4.png').convert_alpha(),
        pygame.image.load('resources/sprites/5.png').convert_alpha(),
        pygame.image.load('resources/sprites/6.png').convert_alpha(),
        pygame.image.load('resources/sprites/7.png').convert_alpha(),
        pygame.image.load('resources/sprites/8.png').convert_alpha(),
        pygame.image.load('resources/sprites/9.png').convert_alpha(),
    }

    GAME_SPRITES['message'] = pygame.image.load('resources/sprites/message.png').convert_alpha()
    GAME_SPRITES['base'] = pygame.image.load('resources/sprites/base.png').convert_alpha()
    GAME_SPRITES['pipe'] = (
        pygame.transform.rotate(pygame.image.load(PIPE).convert_alpha(), 180),
        pygame.image.load(PIPE).convert_alpha()
    )

    GAME_SPRITES['background'] = pygame.image.load(BACKGROUND).convert()
    GAME_SPRITES['player'] = pygame.image.load(PLAYER).convert_alpha()

    GAME_SOUND['die'] = pygame.mixer.Sound('resources/audio/die.wav')
    GAME_SOUND['hit'] = pygame.mixer.Sound('resources/audio/hit.wav')
    GAME_SOUND['point'] = pygame.mixer.Sound('resources/audio/point.wav')
    GAME_SOUND['swoosh'] = pygame.mixer.Sound('resources/audio/swoosh.wav')
    GAME_SOUND['wing'] = pygame.mixer.Sound('resources/audio/wing.wav')

    while True:
        pass

