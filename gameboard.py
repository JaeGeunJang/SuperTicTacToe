import pygame as pg
pg.init()
width, height = 900,900

WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)
RED = (255,0,0)
BACKGROUND = (20, 190, 170)
LINES = (15, 160, 145)
BLINE = (10, 100, 100)
pos = [[0,0,width/3,height/3],[width/3,0,width/3,height/3],[width*2/3,0,width/3,height/3],
       [0,height/3,width/3,height/3],[width/3,height/3,width/3,height/3],
       [width*2/3,height/3,width/3,height/3],[0,height*2/3,width/3,height/3],
       [width/3,height*2/3,width/3,height/3],[width*2/3,height*2/3,width/3,height/3]]
minipos = [[0,0],[width/9,0],[width*2/9,0],
           [0,height/9], [width/9,height/9],[width*2/9,height/9],
           [0,height*2/9], [width/9, height*2/9],[width*2/9,height*2/9]]


linewidth = int(height/100)
halfwidth = int(height/200)

markwidth = int(width/24)

nposi = 5

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
    pg.draw.rect(screen, RED,pos[num-1],linewidth)

def drawX(screen,x,y) :
    pg.draw.line(screen, RED, [x-markwidth,y-markwidth],[x+markwidth,y+markwidth],linewidth*2)
    pg.draw.line(screen, RED, [x+markwidth,y-markwidth],[x-markwidth,y+markwidth],linewidth*2)


def drawO(screen, x, y) :
    x = int(x)
    y = int(y)
    pg.draw.circle(screen, BLUE, [x,y],markwidth , linewidth)

while done :
    screen.fill(BACKGROUND)
    clock.tick(10)
    posi = pg.mouse.get_pos()
    for i in range(9) :
        if pos[i][0] < posi[0] < pos[i][0]+pos[i][2] and pos[i][1] < posi[1] < pos[i][1]+pos[i][3] :
            nposi = i+1


    for event in pg.event.get() :
        if event.type == pg.QUIT :
            done = False
        if event.type== pg.KEYUP :
            done = False
    draw_background(screen, nposi)

    pg.display.flip()

pg.quit()
