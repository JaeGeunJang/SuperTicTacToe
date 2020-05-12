import pygame

WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0,0,255)

pad_width = 900
pad_height = 900

def runGame() :
    global gamepad, clock

    crashed = False
    while not crashed :
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                crashed = True
        gamepad.fill(BLUE)
        pygame.display.update()
        gamepad.fill(RED)
        pygame.display.update()
        gamepad.fill(WHITE)
        pygame.display.update()
        if event.type == pygame.KEYUP :
            crashed = True
        clock.tick(30)
    pygame.quit()

def initGame() :
    global gamepad, clock
    pygame.init()
    gamepad = pygame.display.set_mode((pad_width, pad_height))
    pygame.display.set_caption('Super TicTacToe')

    clock = pygame.time.Clock()
    runGame()

initGame()
