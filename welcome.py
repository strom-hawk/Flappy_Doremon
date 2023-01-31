from gameConstants import *
import sys

def welcomeScreen(SCREEN, FPSCLOCK):
    playerX = int(SCREEN_WIDTH/5)
    playerY = int((SCREEN_HEIGHT - GAME_SPRITES['player'].get_height())/2)
    
    messageX = int((SCREEN_WIDTH - GAME_SPRITES['message'].get_width())/2)
    messageY = int(SCREEN_HEIGHT * 0.13)

    baseX = 0

    while True:
        for event in pygame.event.get():
            if(event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE)):
                pygame.quit()
                sys.exit()
            elif(event.type == KEYDOWN and (event.key == K_UP or event.key == K_SPACE)):
                print("game yet to be started")
                pass
            else:
                SCREEN.blit(GAME_SPRITES['background'],(0,0))
                SCREEN.blit(GAME_SPRITES['player'],(playerX, playerY))
                SCREEN.blit(GAME_SPRITES['message'],(messageX, messageY))
                SCREEN.blit(GAME_SPRITES['base'],(baseX, GROUND_Y))

                pygame.display.update()
                FPSCLOCK.tick(FPS)