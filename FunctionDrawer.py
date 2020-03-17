"""
FunctionDrawer
By lzexmpoane
My Website -->  https://lzexmpoane.github.io/opensourcecode/
My Github -->  https://github.com/lzexmpoane
It's published on GitHub and My Website
I use "Sublime Text" to write is code
And it maybe has many bugs, you can tell me
I will use my best efforts to change the bugs
If you find the bus or you can give me any recommend
this is my email:
1929973351@qq.com or huloubo123@gmail.com
And if you're Chinese or you can speak Chinese(easy communicate)
and you want with me together to make Website(https://lzexmpoane.github.io/opensourcecode/)
you can tell me with an email
:)
--2020/3/17 from China
"""
import pygame,sys,ctypes,time,information
from math import *
import math
pygame.init()
h=information.draw_information.h
w=information.draw_information.w
l=information.draw_information.l
out=information.draw_information.out
f=information.draw_information.f
sf=information.draw_information.sf
sleeptime=information.draw_information.sleeptime
size=information.draw_information.size
#RGB
pencolor=information.draw_information.c1
h+=out
w+=out
defofbgc=information.draw_information.defofbgc
if defofbgc == 1:
    backgrcolor=information.draw_information.nightbgc
elif defofbgc == 0:
    backgrcolor=information.draw_information.backgrcolor
screen = pygame.display.set_mode([w,h])
screen.fill(backgrcolor)
fxAnimate = information.draw_information.fxAnimate
fxprintvalue = information.draw_information.fxprintvalue
def drawline():
    pygame.draw.lines(screen,[0,0,0],False,[[0,h/2],[w,h/2]],1);
    pygame.draw.lines(screen,[0,0,0],False,[[w/2,0],[w/2,h]],1);
    font=pygame.font.Font(None,30)
    pygame.display.flip()
    j=0-int(w/l)/2
    for i in range(0,int(w/l)+1):
        if j!=0:
            pygame.draw.lines(screen,[0,0,0],False,[[i*l+out/2,0],[i*l+out/2,h]],1);
            surf=font.render(str(int(j)),1,(0,0,0))
            pos=[i*l,h/2]
            screen.blit(surf,pos)
            #pygame.display.flip()
        j+=1
    j=0+int(h/l)/2
    for i in range(0,int(h/l)+1):
        pygame.draw.lines(screen,[0,0,0],False,[[0,i*l+out/2],[w,i*l+out/2]],1);
        surf=font.render(str(int(j)),1,(0,0,0))
        pos=[w/2,i*l]
        screen.blit(surf,pos)
        #pygame.display.flip()
        j-=1
    pygame.display.flip()
global x,y
def f1():
    global y
    global x
    y=information.draw_information.f1(x)
    return information.draw_information.f1name
def f2():
    global y
    global x
    y=information.draw_information.f2(x)
    return information.draw_information.f2name
def f3():
    global y
    global x
    y=information.draw_information.f3(x)
    return information.draw_information.f3name
def f4():
    global y
    global x
    y=information.draw_information.f4(x)
    return information.draw_information.f4name
def f5():
    global y
    global x
    y=information.draw_information.f5(x)
    return information.draw_information.f5name
def f6():
    global y
    global x
    y=information.draw_information.f6(x)
    return information.draw_information.f6name
def f7():
    global y
    global x
    y=information.draw_information.f7(x)
    return information.draw_information.f7name
def f8():
    global y
    global x
    y=information.draw_information.f8(x)
    return information.draw_information.f8name
def f9():
    global y
    global x
    y=information.draw_information.f9(x)
    return information.draw_information.f9name

global chfun
chfun=1
def tryy():
    global y
    global x
    global OverflowErrorVar
    global ZeroDivisionErrorVar
    global ValueErrorVar
    global tmp
    x=0
    y=0
    OverflowErrorVar=0
    ZeroDivisionErrorVar=0
    ValueErrorVar=0
    try:
        if chfun==1:
            f1()
        elif chfun==2:
            f2()
        elif chfun==3:
            f3()
        elif chfun==4:
            f4()
        elif chfun==5:
            f5()
        elif chfun==6:
            f6()
        elif chfun==7:
            f7()
        elif chfun==8:
            f8()
        elif chfun==9:
            f9()
    except ValueError:
        ValueErrorVar=1
        x=f
        y=f
    except OverflowError:
        OverflowErrorVar=1
    except ZeroDivisionError:
        ZeroDivisionErrorVar=1
    x=-1
    y=-1
    try:
        if chfun==1:
            f1()
        elif chfun==2:
            f2()
        elif chfun==3:
            f3()
        elif chfun==4:
            f4()
        elif chfun==5:
            f5()
        elif chfun==6:
            f6()
        elif chfun==7:
            f7()
        elif chfun==8:
            f8()
        elif chfun==9:
            f9()
    except ValueError:
        ValueErrorVar=1
        x=f
        y=f
    except OverflowError:
        OverflowErrorVar=1
    except ZeroDivisionError:
        ZeroDivisionErrorVar=1
    if ValueErrorVar==0:
        x=-((w+out)/(2*l))
        y=-((w+out)/(2*l))
    tmp=y
def funtry():
    global x
    global y
    tmp=y
    try:
        if chfun==1:
            f1()
        elif chfun==2:
            f2()
        elif chfun==3:
            f3()
        elif chfun==4:
            f4()
        elif chfun==5:
            f5()
        elif chfun==6:
            f6()
        elif chfun==7:
            f7()
        elif chfun==8:
            f8()
        elif chfun==9:
            f9()
    except ValueError:
        y=tmp
        return False
    except OverflowError:
        y=tmp
        return False
    except ZeroDivisionError:
        y=tmp
        return False
global funstr
def get_funreturnvaulex():
    global funstr
    if chfun==1:
        funstr=f1()
    elif chfun==2:
        funstr=f2()
    elif chfun==3:
        funstr=f3()
    elif chfun==4:
        funstr=f4()
    elif chfun==5:
        funstr=f5()
    elif chfun==6:
        funstr=f6()
    elif chfun==7:
        funstr=f7()
    elif chfun==8:
        funstr=f8()
    elif chfun==9:
        funstr=f9()
def drawfx():
    global y
    global x
    global OverflowErrorVar
    global ZeroDivisionErrorVar
    global ValueErrorVar
    global tmp
    global fix
    global fiy
    global sf
    global screen
    global w
    global h
    global l
    global strfx
    global sleeptime
    global fxAnimate
    global out
    tryy()
    font=pygame.font.Font(None,30)
    for i in range(0,int(w/(l/int(1/f))+out)):
        #print(i)
        if funtry()==False:
            x+=f
            #print("x=",x)
            continue
        if (OverflowErrorVar==1 or ZeroDivisionErrorVar==1 )and -(f*2)<=x and x<f:
            x=f
        y=tmp
        get_funreturnvaulex()
        fix=(w/2+x*l)
        fiy=(h/2-y*l)
        if(fxprintvalue == True):
            pygame.draw.rect(screen,backgrcolor,[0,0,w,out],0)
            strfx=funstr+"  fxAnimate = "+str(fxAnimate)+"   Accuracy = "+str(f)+"   i="+str(i)
            surf=font.render(strfx,1,(255,0,0))
            pos=[0,0]
            screen.blit(surf,pos)
        #screen.set_at([int(fix),int(fiy)],[101,87,210])
        pygame.draw.circle(screen,pencolor,[int(fix),int(fiy)],1,0)
        if fxAnimate == True:
            pygame.display.flip()
        time.sleep(sleeptime/1000)
        x+=f
        tmp+=f
    pygame.display.flip()
    pygame.draw.rect(screen,backgrcolor,[0,0,w,out],0)
    strfx=funstr+"  fxAnimate = "+str(fxAnimate)+"   Accuracy = "+str(f)+"   i="+str(i)
    surf=font.render(strfx,1,(0,255,0))
    pos=[0,0]
    screen.blit(surf,pos)
    pygame.display.flip()
def drawpoint():
    global tmx
    global tmy
    global size
    lmx=tmx
    lmy=tmy
    tmx , tmy = pygame.mouse.get_pos()
    pygame.draw.line(screen,[255,0,0],[lmx,lmy],[tmx,tmy],size*2)
    pygame.draw.line(screen,[255,0,0],[tmx,tmy],[tmx,tmy],size*2)
    pygame.display.flip()
running = True
drawline()
ifd=False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_d:
                drawfx()
            if event.key == pygame.K_1:
                chfun=1
                pencolor=information.draw_information.c1
            if event.key == pygame.K_2:
                chfun=2
                pencolor=information.draw_information.c2
            if event.key == pygame.K_3:
                chfun=3
                pencolor=information.draw_information.c3
            if event.key == pygame.K_4:
                chfun=4
                pencolor=information.draw_information.c4
            if event.key == pygame.K_5:
                chfun=5
                pencolor=information.draw_information.c5
            if event.key == pygame.K_6:
                chfun=6
                pencolor=information.draw_information.c6
            if event.key == pygame.K_7:
                chfun=7
                pencolor=information.draw_information.c7
            if event.key == pygame.K_8:
                chfun=8
                pencolor=information.draw_information.c8
            if event.key == pygame.K_9:
                chfun=9
                pencolor=information.draw_information.c9
            if event.key == pygame.K_c:
                pygame.draw.rect(screen,backgrcolor,[0,0,w,h],0)
                drawline()
                pygame.display.flip()
            if event.key == pygame.K_n:
                if defofbgc == 1:
                    backgrcolor=information.draw_information.backgrcolor
                    defofbgc=0
                elif defofbgc == 0:
                    backgrcolor=information.draw_information.nightbgc
                    defofbgc=1
                screen.fill(backgrcolor)
                drawline()
                pygame.display.flip()
        if event.type == pygame.MOUSEMOTION:
            if ifd:
                drawpoint()
        if event.type == pygame.MOUSEBUTTONDOWN:
            tmx , tmy = pygame.mouse.get_pos()
            pygame.draw.line(screen,[255,0,0],[tmx,tmy-1],[tmx,tmy+1],size*2)
            pygame.display.flip()
            ifd=True
        if event.type == pygame.MOUSEBUTTONUP:
            ifd=False
pygame.quit();
