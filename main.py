import random
import sys
import pygame
import pygame.locals 
# import *


FPS = 32
SCREEN_WIDTH = 289
SCREEN_HEIGHT = 511
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
GROUND_Y = SCREEN_HEIGHT * 0.8
GAME_IMAGES = {}
GAME_SOUND = {}
PLAYER = '/resources/images/bird.png'
BACKGROUND = '/resources/images/background.png'
PIPE = '/resources/images/pipe.png'

running = True

# if __name__ == "__main__":
#     # This will be the main function from where game will start
#     pygame.init()
#     pygame.display.set_caption("Py Game")
#     while(running):
#         pass
#     pygame.quit()

pygame.init()
pygame.display.set_caption("Py Game")
while(running):
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

pygame.quit()