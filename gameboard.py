import pygame as pg
import TicTecToe as ttt
from TicTecToe import *

pg.init()
width, height = 900,900

WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)
RED = (255,0,0)
BACKGROUND = (20, 190, 170)
LINES = (15, 160, 145)
BLINE = (10, 100, 100)

pos = []
for j in range(3) :
    for i in range(3) :
        pos.append([width*i/3,height*j/3,width/3,height/3])

minipos = []
for j in range(3) :
    for i in range(3) :
        minipos.append([width*i/9,height*j/9])

linewidth = int(height/100)
halfwidth = int(height/200)
markwidth = int(width/24)

prenposi = 4
nposi = 4
miniposi = 4
player = 1

screen = pg.display.set_mode((width, height))
done = True
pg.display.set_caption("Python Super TicTacToe")
clock = pg.time.Clock()

def draw_background(screen, num) :
    for i in range (1,9) :
        if i%3 != 0  :
            pg.draw.line(screen, LINES, [width*i/9,0],[width*i/9, height],halfwidth)
            pg.draw.line(screen, LINES, [0,height*i/9],[width, height*i/9],halfwidth)
    for i in range (1,3) :
        pg.draw.line(screen, BLINE, [width*i/3,0],[width*i/3, height],linewidth)
        pg.draw.line(screen, BLINE, [0,height*i/3],[width, height*i/3],linewidth)
    pg.draw.rect(screen, RED,pos[num],linewidth)

def drawO(screen, x, y) :
    x = int(x)
    y = int(y)
    pg.draw.circle(screen, BLUE, [x,y],markwidth , linewidth)

def drawX(screen,x,y) :
    pg.draw.line(screen, RED, [x-markwidth,y-markwidth],[x+markwidth,y+markwidth],linewidth*2)
    pg.draw.line(screen, RED, [x+markwidth,y-markwidth],[x-markwidth,y+markwidth],linewidth*2)

def judgeIn(screen, posi) :
    if pos[nposi][0] < posi[0] < pos[nposi][0]+pos[nposi][2] and pos[nposi][1] < posi[1] < pos[nposi][1]+pos[nposi][3] :
        return True
    else :
        return False

def drawMsqure(screen, posi) :
    global miniposi
    if judgeIn(screen, posi) :
        for i in range (9) :
            if pos[nposi][0]+minipos[i][0] < posi[0] < pos[nposi][0]+minipos[i][0]+pos[nposi][2]/3 :
                if pos[nposi][1]+minipos[i][1] < posi[1] < pos[nposi][1]+minipos[i][1]+pos[nposi][3]/3 :
                    repos = [pos[nposi][0]+minipos[i][0], pos[nposi][1]+minipos[i][1] ,
                            pos[nposi][2]/3, pos[nposi][3]/3]
                    miniposi = i
                    pg.draw.rect(screen, BLUE, repos, linewidth)

def drawGameboard(screen, board) :
    for i in range (9) :
        for j in range(9) :
            if board[i][j] == 1 :
                drawO(screen,pos[i][0]+minipos[j][0]+width/18,pos[i][1]+minipos[j][1]+height/18)
            if board[i][j] == -1 :
                drawX(screen,pos[i][0]+minipos[j][0]+width/18,pos[i][1]+minipos[j][1]+height/18)

while done :
    screen.fill(BACKGROUND)
    clock.tick(10)
    posi = pg.mouse.get_pos()
    for event in pg.event.get() :
        if event.type == pg.QUIT :
            done = False
        if event.type == pg.MOUSEBUTTONUP :
            if judgeIn(screen, posi) :
                board[nposi][miniposi] = player
                player *= -1
                prenposi = nposi
                nposi = miniposi

    draw_background(screen, nposi)
    drawMsqure(screen, posi)
    drawGameboard(screen,board)

    if ttt.winGame(board,prenposi) == 1 :
        print("Player 1 win")
        done = False
    elif ttt.winGame(board, prenposi) == -1 :
        print("Player 2 win")
        done = False

    pg.display.flip()

pg.quit()
