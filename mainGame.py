from gameConstants import *
import random

def getRandomPipe():
    pipeHeight = GAME_SPRITES['pipe'][0].get_height()
    offSet = SCREEN_HEIGHT/3
    y2 = offSet * random.randrange(0, int(SCREEN_HEIGHT - GAME_SPRITES['base'].get_height() - 1.2 * offSet))
    pipeX = SCREEN_WIDTH + 10
    y1 = pipeHeight - y2 + offSet
    pipe = [
        {'x': pipeX, 'y': -y1}, #upper pipe
        {'x': pipeX, 'y': y2} #lower pipe
    ]
    return pipe

def mainGame():
    score = 0
    playerX = int(SCREEN_WIDTH/5)
    playerY = int(SCREEN_HEIGHT/2)

    baseX = 0

    newPipe1 = getRandomPipe()
    newPipe2 = getRandomPipe()

    #list of upper pipes
    upperPipes = [
        {'x': SCREEN_WIDTH + 200, 'y': newPipe1[0]['y']},
        {'x': SCREEN_WIDTH + 200 + (SCREEN_WIDTH/2), 'y': newPipe2[1]['y']},
    ]
    #list of lower pipes
    lowerPipes = [
        {'x': SCREEN_WIDTH + 200, 'y': newPipe1[0]['y']},
        {'x': SCREEN_WIDTH + 200 + (SCREEN_WIDTH/2), 'y': newPipe2[1]['y']},
    ]

    print(upperPipes)
    print(lowerPipes)


    pipeVelocityX = 4

