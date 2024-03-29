from gameConstants import *
import random
import sys
import time

'''
Function to check if the bird collides with the sky or the ground or the pipes.
'''
def hasCollided(playerX, playerY, upperPipes, lowerPipes):
    if(playerY > GROUND_Y -25 or playerY < 0):
        GAME_SOUND['hit'].play()
        time.sleep(2)
        return True

    for pipe in upperPipes:
        pipeHeight = GAME_SPRITES['pipe'][0].get_height()
        if(playerY < pipeHeight + pipe['y'] and abs((playerX-15) - pipe['x']) <= GAME_SPRITES['pipe'][0].get_width()):
            GAME_SOUND['hit'].play()
            time.sleep(2)
            return True

    for pipe in lowerPipes:
        if(playerY + GAME_SPRITES['player'].get_height() > pipe['y'] and abs((playerX -15) - pipe['x']) < GAME_SPRITES['pipe'][0].get_width()):
            GAME_SOUND['hit'].play()
            time.sleep(2)
            return True

    return False

'''
Function to generate random pipes.
'''
def getRandomPipe():
    pipeHeight = GAME_SPRITES['pipe'][0].get_height()
    offSet = SCREEN_HEIGHT/4
    y2 = offSet + random.randrange(0, int(SCREEN_HEIGHT - GAME_SPRITES['base'].get_height() - 1.2 * offSet))
    pipeX = SCREEN_WIDTH + 10
    y1 = pipeHeight - y2 + offSet
    pipe = [
        {'x': pipeX, 'y': -y1}, #upper pipe
        {'x': pipeX, 'y': y2} #lower pipe
    ]
    return pipe

def mainGame(SCREEN, FPSCLOCK):
    score = 0
    playerX = int(SCREEN_WIDTH/5)
    playerY = int(SCREEN_HEIGHT/2)

    baseX = 0

    newPipe1 = getRandomPipe()
    newPipe2 = getRandomPipe()

    #list of upper pipes
    upperPipes = [
        {'x': SCREEN_WIDTH + 200, 'y': newPipe1[0]['y']},
        {'x': SCREEN_WIDTH + 200 + (SCREEN_WIDTH/2), 'y': newPipe2[0]['y']},
    ]
    #list of lower pipes
    lowerPipes = [
        {'x': SCREEN_WIDTH + 200, 'y': newPipe1[1]['y']},
        {'x': SCREEN_WIDTH + 200 + (SCREEN_WIDTH/2), 'y': newPipe2[1]['y']},
    ]

    pipeVelocityX = -4

    playerVelocityY = -9

    playerMaxVelocityY = 10
    playerMinVelocityY = -8

    playerAccY = 1

    playerFlapVelocity = -8
    playerFlapped = False

    while True:
        for event in pygame.event.get():
            if(event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE)):
                pygame.quit()
                sys.exit()
            elif(event.type == KEYDOWN and (event.key == K_UP or event.key == K_SPACE)):
                if(playerY > 0):
                    playerVelocityY = playerFlapVelocity
                    playerFlapped = True
                    GAME_SOUND['wing'].play()
            
        #Crash test is variable that checks if the player has collided with any of the pipe or not    
        crashTest = hasCollided(playerX, playerY, upperPipes, lowerPipes)

        #Check if player crashed, return the game
        if(crashTest):
            return
        
        #Check for score
        playerMidPos = playerX + GAME_SPRITES['player'].get_width()/2
        for pipe in upperPipes:
            pipeMidPos = pipe['x'] + GAME_SPRITES['pipe'][0].get_width()/2
            if(pipeMidPos <= playerMidPos < pipeMidPos + 4):
                score += 1
                print(f"Your score is: {score}")
                GAME_SOUND['point'].play()
            
        if(playerVelocityY < playerMaxVelocityY and not playerFlapped):
            playerVelocityY += playerAccY

        if(playerFlapped):
            playerFlapped = False

        playerHeight = GAME_SPRITES['player'].get_height()
        playerY = playerY + min(playerVelocityY, GROUND_Y - playerY - playerHeight)

        # move pipe to the left
        for upperPipe, lowerPipe in zip(upperPipes, lowerPipes):
            upperPipe['x'] += pipeVelocityX
            lowerPipe['x'] += pipeVelocityX

        # add a new pipe when the first pipe is about to cross the screen
        if(0 < upperPipes[0]['x'] < 5):
            newPipe = getRandomPipe()
            upperPipes.append(newPipe[0])
            lowerPipes.append(newPipe[1])


        # if the pipe is out of the screen remove it
        if(upperPipes[0]['x'] < -GAME_SPRITES['pipe'][0].get_width()):
            upperPipes.pop(0)
            lowerPipes.pop(0)


        #Lets blit our sprites now
        SCREEN.blit(GAME_SPRITES['background'],(0,0))
        for upperPipe, lowerPipe in zip(upperPipes, lowerPipes):
            SCREEN.blit(GAME_SPRITES['pipe'][0],(upperPipe['x'], upperPipe['y']))
            SCREEN.blit(GAME_SPRITES['pipe'][1],(lowerPipe['x'], lowerPipe['y']))

        SCREEN.blit(GAME_SPRITES['base'],(baseX, GROUND_Y))
        SCREEN.blit(GAME_SPRITES['player'],(playerX, playerY))

        myDigits = [int(x) for x in list(str(score))]
        width = 0
        for digit in myDigits:
            width += GAME_SPRITES['numbers'][digit].get_width()
        
        xOffSet = (SCREEN_WIDTH - width)/2

        for digit in myDigits:
            SCREEN.blit(GAME_SPRITES['numbers'][digit], (xOffSet, SCREEN_HEIGHT * 0.12))
            xOffSet += GAME_SPRITES['numbers'][digit].get_width()
        
        pygame.display.update()
        FPSCLOCK.tick(FPS)

