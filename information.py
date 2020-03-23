import pygame,sys,ctypes,time
from math import *
class draw_information(object):
    """docstring for draw_information"""

    #HIGH_OF_THE_SCREEN
    h=600
    #WIDTH_OF_THE_SCREEN
    w=800

    #Pixels in a grid(1<=l<=100)
    l=50
    #Off-screen character display
    out=20

    #Accuracy
    f=0.001
    sf=1000

    #Intervals(ms)
    sleeptime=0

    #DEFAULT_BACKGROUND_COLOR
    defofbgc=0

    #Brush size
    size=2
    #BACKGROUND_COLOR
    backgrcolor=[255,255,255]
    #NIGHT_BACKGROUND_COLOR
    nightbgc=[50,50,50]

    #Show function drawing process
    fxAnimate = True
    #Show value
    fxprintvalue = True

    #COLOR_OF_DRAWING_FUNCTION
    c1=[100,100,255]
    c2=[255,100,100]
    c3=[50,255,50]
    c4=[238,118,0]
    c5=[191,62,255]
    c6=[56,142,142]
    c7=[135,206,235]
    c8=[0,139,139]
    c9=[0,0,0]

    def __init__(self):
        pass

    #FUNCTION
    f1name="y=x"
    def f1(x):
        y=x
        return y

    f2name="y=x^2"
    def f2(x):
        y=x**2
        return y

    f3name="y=1/x"
    def f3(x):
        y=1/x
        return y

    f4name="y=sin(x)"
    def f4(x):
        y=sin(x)
        return y

    f5name="y=cos(x)"
    def f5(x):
        y=cos(x)
        return y

    f6name="y=tan(x)"
    def f6(x):
        y=tan(x)
        return y

    f7name="y=log(x,10)"
    def f7(x):
        y=log(x,10)
        return y

    f8name="y=sqrt(x)"
    def f8(x):
        y=sqrt(x)
        return y

    f9name="y=sin(1/x)"
    def f9(x):
        y=sin(1/x)
        return y

    def printinf(self):
        informationstr="This is information of FunctionDrawer.\nHIGH_OF_THE_SCREEN="+str(self.h)+"px.\n\
WIDTH_OF_THE_SCREEN="+str(self.w)+"px.\nPixels in a grid(1<=l<=100)="+str(self.l)+"px.\n\
Off-screen character display="+str(self.out)+"px.\nAccuracy="+str(self.f)+".\nIntervals(ms)="+str(self.sleeptime)+"ms.\n\
Brush size="+str(self.size)+"px.\nBACKGROUND_COLOR="+str(self.backgrcolor)+".\nNIGHT_BACKGROUND_COLOR="+str(self.nightbgc)+".\n\
Show function drawing process="+str(self.fxAnimate)+".\nShow value="+str(self.fxprintvalue)+".\n\
COLOR_OF_DRAWING_FUNCTION=\n{\n    c1="+str(self.c1)+";\n    c2="+str(self.c2)+";\n    c3="+str(self.c3)+";\n    c4="+str(self.c4)+";\n\
    c5="+str(self.c5)+";\n    c6="+str(self.c6)+";\n    c7="+str(self.c7)+";\n    c8="+str(self.c8)+";\n    c9="+str(self.c9)+"\n}\nFunction1: "+str(self.f1name)+"\n\
Function2: "+str(self.f2name)+"\nFunction3: "+str(self.f3name)+"\nFunction4: "+str(self.f4name)+"\nFunction5: "+str(self.f5name)+"\n\
Function6: "+str(self.f6name)+"\nFunction7: "+str(self.f7name)+"\nFunction8: "+str(self.f8name)+"\nFunction9: "+str(self.f9name)+"\n"
        return informationstr
