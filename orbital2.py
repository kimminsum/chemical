import pygame,sys,random, numpy
from pygame.locals import *
 
pygame.init()
mainClock = pygame.time.Clock()
 
WINDOWWIDTH = 900
WINDOWHEIGHT= 900
 
windowSurface = pygame.display.set_mode( (WINDOWWIDTH, WINDOWHEIGHT), 0, 32 )
pygame.display.set_caption('화학 오비탈')

# COLOR 
REALBLACK = (0, 0, 0)
BLACK = (100,100,100)
GREEN = (0,255,0)
WHITE = (255,255,255)
BLUE = (0, 0, 230)
RED = (255, 0, 0)

s_counter = 0
p_x_counter = 0
p_y_counter = 0
p_z_counter = 0

# TIMER
NEW = 0
FOODSIZE = 3

s_orbital = []
p_x_orbital = []
p_y_orbital = []
p_z_orbital = []

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    # S오비탈
    s_counter += 1
    if s_counter >= NEW:
        s_counter = 0
        ticket = random.randrange(1,27)
        if ticket <= 5:
            s_r = random.randrange(1,30)
            s_nanut = random.randrange(1, 1000) / 17
            s_seta = numpy.pi*random.randrange(1,1000)/ s_nanut
            s_px_x = WINDOWWIDTH/2 + s_r*numpy.cos(s_seta)
            s_px_y = WINDOWHEIGHT/2 + s_r*numpy.sin(s_seta)
            s_orbital.append(pygame.Rect(s_px_x, s_px_y, FOODSIZE, FOODSIZE))
        elif ticket >= 6 and ticket <= 22:
            s_r = random.randrange(35,75)
            s_nanut = random.randrange(1, 1000)/17
            s_seta = numpy.pi*random.randrange(1,1000)/ s_nanut
            s_px_x = WINDOWWIDTH/2 + s_r*numpy.cos(s_seta)
            s_px_y = WINDOWHEIGHT/2 + s_r*numpy.sin(s_seta)
            s_orbital.append(pygame.Rect(s_px_x, s_px_y, FOODSIZE, FOODSIZE))
        elif ticket >= 23 and ticket <= 25:
            s_r = random.randrange(100, 200)
            s_nanut = random.randrange(1, 1000)/ 17
            s_seta = numpy.pi*random.randrange(1,1000)/ s_nanut
            s_px_x = WINDOWWIDTH/2 + s_r*numpy.cos(s_seta)
            s_px_y = WINDOWHEIGHT/2 + s_r*numpy.sin(s_seta)
            s_orbital.append(pygame.Rect(s_px_x, s_px_y, FOODSIZE, FOODSIZE))
        else:
            s_r = random.randrange(201,400)
            s_nanut = random.randrange(1, 1000)/ 17
            s_seta = numpy.pi*random.randrange(1,1000)/ s_nanut
            s_px_x = WINDOWWIDTH/2 + s_r*numpy.cos(s_seta)
            s_px_y = WINDOWHEIGHT/2 + s_r*numpy.sin(s_seta)
            s_orbital.append(pygame.Rect(s_px_x, s_px_y, FOODSIZE, FOODSIZE))

    # P_X오비탈 
    # 왼쪽
    p_x_counter += 1
    if p_x_counter >= NEW:
        p_x_counter = 0
        p_x_ticket = random.randrange(1,27)
        if p_x_ticket <= 2:
            p_x_r = random.randrange(1,30)
            p_x_nanut = random.randrange(1, 1000) / 17
            p_x_seta = numpy.pi*random.randrange(1,1000)/ p_x_nanut
            p_x_px_x = WINDOWWIDTH*(2/5) + p_x_r*numpy.cos(p_x_seta)
            p_x_px_y = WINDOWHEIGHT/2 + p_x_r*numpy.sin(p_x_seta)
            p_x_orbital.append(pygame.Rect(p_x_px_x, p_x_px_y, FOODSIZE, FOODSIZE))
        elif p_x_ticket >= 3 and p_x_ticket <= 22:
            p_x_r = random.randrange(1,75)
            p_x_nanut = random.randrange(1, 1000)/17
            p_x_seta = numpy.pi*random.randrange(1,1000)/ p_x_nanut
            p_x_px_x = WINDOWWIDTH*(4/13) + p_x_r*numpy.cos(p_x_seta)
            p_x_px_y = WINDOWHEIGHT/2 + p_x_r*numpy.sin(p_x_seta)
            p_x_orbital.append(pygame.Rect(p_x_px_x, p_x_px_y, FOODSIZE, FOODSIZE))
        elif p_x_ticket >=23 and p_x_ticket < 27:
            p_x_r = random.randrange(1,200)
            p_x_nanut = random.randrange(1, 1000)/ 17
            p_x_seta = numpy.pi*random.randrange(1,1000)/ p_x_nanut
            p_x_px_x = WINDOWWIDTH*(1/4) + p_x_r*numpy.cos(p_x_seta)
            p_x_px_y = WINDOWHEIGHT/2 + p_x_r*numpy.sin(p_x_seta)
            p_x_orbital.append(pygame.Rect(p_x_px_x, p_x_px_y, FOODSIZE, FOODSIZE))
    # 오른쪽
        if p_x_ticket <= 2:
            p_x_r = random.randrange(1,30)
            p_x_nanut = random.randrange(1, 1000) / 17
            p_x_seta = numpy.pi*random.randrange(1,1000)/ p_x_nanut
            p_x_px_x = WINDOWWIDTH*(3/5) + p_x_r*numpy.cos(p_x_seta)
            p_x_px_y = WINDOWHEIGHT/2 + p_x_r*numpy.sin(p_x_seta)
            p_x_orbital.append(pygame.Rect(p_x_px_x, p_x_px_y, FOODSIZE, FOODSIZE))
        elif p_x_ticket >= 3 and p_x_ticket <= 22:
            p_x_r = random.randrange(1,75)
            p_x_nanut = random.randrange(1, 1000)/17
            p_x_seta = numpy.pi*random.randrange(1,1000)/ p_x_nanut
            p_x_px_x = WINDOWWIDTH*(9/13) + p_x_r*numpy.cos(p_x_seta)
            p_x_px_y = WINDOWHEIGHT/2 + p_x_r*numpy.sin(p_x_seta)
            p_x_orbital.append(pygame.Rect(p_x_px_x, p_x_px_y, FOODSIZE, FOODSIZE))
        elif p_x_ticket >=23 and p_x_ticket < 27:
            p_x_r = random.randrange(1,200)
            p_x_nanut = random.randrange(1, 1000)/ 17
            p_x_seta = numpy.pi*random.randrange(1,1000)/ p_x_nanut
            p_x_px_x = WINDOWWIDTH*(3/4) + p_x_r*numpy.cos(p_x_seta)
            p_x_px_y = WINDOWHEIGHT/2 + p_x_r*numpy.sin(p_x_seta)
            p_x_orbital.append(pygame.Rect(p_x_px_x, p_x_px_y, FOODSIZE, FOODSIZE))

    # P_Y 오비탈 
    # 대각 앞
    p_y_counter += 1
    if p_y_counter >= NEW:
        p_y_counter = 0
        p_y_ticket = random.randrange(1,27)
        if p_y_ticket <= 2:
            p_y_r = random.randrange(1,30)
            p_y_nanut = random.randrange(1, 1000) / 17
            p_y_seta = numpy.pi*random.randrange(1,1000)/ p_y_nanut
            p_y_px_x = WINDOWWIDTH*(5/11) + p_y_r*numpy.cos(p_y_seta)
            p_y_px_y = WINDOWHEIGHT*(6/11) + p_y_r*numpy.sin(p_y_seta)
            p_y_orbital.append(pygame.Rect(p_y_px_x, p_y_px_y, FOODSIZE, FOODSIZE))
        elif p_y_ticket >= 3 and p_y_ticket <= 22:
            p_y_r = random.randrange(1,75)
            p_y_nanut = random.randrange(1, 1000)/17
            p_y_seta = numpy.pi*random.randrange(1,1000)/ p_y_nanut
            p_y_px_x = WINDOWWIDTH*(8/13) + p_y_r*numpy.cos(p_y_seta)
            p_y_px_y = WINDOWHEIGHT*(5/13) + p_y_r*numpy.sin(p_y_seta)
            p_y_orbital.append(pygame.Rect(p_y_px_x, p_y_px_y, FOODSIZE, FOODSIZE))
        elif p_y_ticket >=23 and p_y_ticket < 27:
            p_y_r = random.randrange(1,200)
            p_y_nanut = random.randrange(1, 1000)/ 17
            p_y_seta = numpy.pi*random.randrange(1,1000)/ p_y_nanut
            p_y_px_x = WINDOWWIDTH*(8/11) + p_y_r*numpy.cos(p_y_seta)
            p_y_px_y = WINDOWHEIGHT*(3/11) + p_y_r*numpy.sin(p_y_seta)
            p_y_orbital.append(pygame.Rect(p_y_px_x, p_y_px_y, FOODSIZE, FOODSIZE))
        # 대각 뒤 
        if p_y_ticket <= 2:
            p_y_r = random.randrange(1,30)
            p_y_nanut = random.randrange(1, 1000) / 17
            p_y_seta = numpy.pi*random.randrange(1,1000)/ p_y_nanut
            p_y_px_x = WINDOWWIDTH*(6/11) + p_y_r*numpy.cos(p_y_seta)
            p_y_px_y = WINDOWHEIGHT*(5/11) + p_y_r*numpy.sin(p_y_seta)
            p_y_orbital.append(pygame.Rect(p_y_px_x, p_y_px_y, FOODSIZE, FOODSIZE))
        elif p_y_ticket >= 3 and p_y_ticket <= 22:
            p_y_r = random.randrange(1,75)
            p_y_nanut = random.randrange(1, 1000)/17
            p_y_seta = numpy.pi*random.randrange(1,1000)/ p_y_nanut
            p_y_px_x = WINDOWWIDTH*(5/13) + p_y_r*numpy.cos(p_y_seta)
            p_y_px_y = WINDOWHEIGHT*(8/13) + p_y_r*numpy.sin(p_y_seta)
            p_y_orbital.append(pygame.Rect(p_y_px_x, p_y_px_y, FOODSIZE, FOODSIZE))
        elif p_y_ticket >=23 and p_y_ticket < 27:
            p_y_r = random.randrange(1,200)
            p_y_nanut = random.randrange(1, 1000)/ 17
            p_y_seta = numpy.pi*random.randrange(1,1000)/ p_y_nanut
            p_y_px_x = WINDOWWIDTH*(3/11) + p_y_r*numpy.cos(p_y_seta)
            p_y_px_y = WINDOWHEIGHT*(8/11) + p_y_r*numpy.sin(p_y_seta)
            p_y_orbital.append(pygame.Rect(p_y_px_x, p_y_px_y, FOODSIZE, FOODSIZE))

    # P_Z오비탈 
    # 위
    p_z_counter += 1
    if p_z_counter >= NEW:
        p_z_counter = 0
        p_z_ticket = random.randrange(1,27)
        if p_z_ticket <= 2:
            p_z_r = random.randrange(1,30)
            p_z_nanut = random.randrange(1, 1000) / 17
            p_z_seta = numpy.pi*random.randrange(1,1000)/ p_z_nanut
            p_z_px_x = WINDOWWIDTH/2 + p_z_r*numpy.cos(p_z_seta)
            p_z_px_y = WINDOWHEIGHT*(2/5) + p_z_r*numpy.sin(p_z_seta)
            p_z_orbital.append(pygame.Rect(p_z_px_x, p_z_px_y, FOODSIZE, FOODSIZE))
        elif p_z_ticket >= 3 and p_z_ticket <= 22:
            p_z_r = random.randrange(1,75)
            p_z_nanut = random.randrange(1, 1000)/17
            p_z_seta = numpy.pi*random.randrange(1,1000)/ p_z_nanut
            p_z_px_x = WINDOWWIDTH/2 + p_z_r*numpy.cos(p_z_seta)
            p_z_px_y = WINDOWHEIGHT*(4/13) + p_z_r*numpy.sin(p_z_seta)
            p_z_orbital.append(pygame.Rect(p_z_px_x, p_z_px_y, FOODSIZE, FOODSIZE))
        elif p_z_ticket >=23 and p_z_ticket < 27:
            p_z_r = random.randrange(1,200)
            p_z_nanut = random.randrange(1, 1000)/ 17
            p_z_seta = numpy.pi*random.randrange(1,1000)/ p_z_nanut
            p_z_px_x = WINDOWWIDTH/2 + p_z_r*numpy.cos(p_z_seta)
            p_z_px_y = WINDOWHEIGHT*(1/4) + p_z_r*numpy.sin(p_z_seta)
            p_z_orbital.append(pygame.Rect(p_z_px_x, p_z_px_y, FOODSIZE, FOODSIZE))
        # 아래
        if p_z_ticket <= 2:
            p_z_r = random.randrange(1,30)
            p_z_nanut = random.randrange(1, 1000) / 17
            p_z_seta = numpy.pi*random.randrange(1,1000)/ p_z_nanut
            p_z_px_x = WINDOWWIDTH/2 + p_z_r*numpy.cos(p_z_seta)
            p_z_px_y = WINDOWHEIGHT*(3/5) + p_z_r*numpy.sin(p_z_seta)
            p_z_orbital.append(pygame.Rect(p_z_px_x, p_z_px_y, FOODSIZE, FOODSIZE))
        elif p_z_ticket >= 3 and p_z_ticket <= 22:
            p_z_r = random.randrange(1,75)
            p_z_nanut = random.randrange(1, 1000)/17
            p_z_seta = numpy.pi*random.randrange(1,1000)/ p_z_nanut
            p_z_px_x = WINDOWWIDTH/2 + p_z_r*numpy.cos(p_z_seta)
            p_z_px_y = WINDOWHEIGHT*(9/13) + p_z_r*numpy.sin(p_z_seta)
            p_z_orbital.append(pygame.Rect(p_z_px_x, p_z_px_y, FOODSIZE, FOODSIZE))
        elif p_z_ticket >=23 and p_z_ticket < 27:
            p_z_r = random.randrange(1,200)
            p_z_nanut = random.randrange(1, 1000)/ 17
            p_z_seta = numpy.pi*random.randrange(1,1000)/ p_z_nanut
            p_z_px_x = WINDOWWIDTH/2 + p_z_r*numpy.cos(p_z_seta)
            p_z_px_y = WINDOWHEIGHT*(3/4) + p_z_r*numpy.sin(p_z_seta)
            p_z_orbital.append(pygame.Rect(p_z_px_x, p_z_px_y, FOODSIZE, FOODSIZE))

    windowSurface.fill(WHITE)
    # S오비탈
    for i in range(len(s_orbital)):
        pygame.draw.rect(windowSurface, BLACK, s_orbital[i])
    # P_X오비탈
    for p_x in range(len(p_x_orbital)):
        pygame.draw.rect(windowSurface, BLUE, p_x_orbital[p_x])
    # P_Y오비탈     
    for p_y in range(len(p_y_orbital)):
        pygame.draw.rect(windowSurface, RED, p_y_orbital[p_y])
    # P_Z오비탈
    for p_z in range(len(p_z_orbital)):
        pygame.draw.rect(windowSurface, GREEN, p_z_orbital[p_z])
    pygame.draw.line(windowSurface, REALBLACK, [0,900], [900,0],2)
    pygame.draw.line(windowSurface, REALBLACK, [0,450], [900,450],2)
    pygame.draw.line(windowSurface, REALBLACK, [450,0], [450,900],2)

    pygame.display.update()