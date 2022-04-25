

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import * 
import sys
from math import log10,ceil

def init():
 glClearColor(1.0,1.0,1.0,1.0)
 glColor3f(1.0,0.0,0.0)
 glPointSize(2.0) 
 gluOrtho2D(0,500,0,500)

def plotpoints(xcoordinate,ycoordinate):
 glBegin(GL_POINTS)
 glVertex2i(xcoordinate,ycoordinate)
 glEnd()
 glFlush()

def ROUND(a):
 return int(a + 0.5)

def find_e(m):
 n = ceil(log10(m)/log10(2))
 return 2**(-n)

def lineDDA(x1,y1,x2,y2):
 dx = x2-x1
 dy = y2-y1
 m = max(abs(dx),abs(dy))
 e = find_e(m)
 Xinc = float(dx*e)
 Yinc = float(dy*e)
 x,y=x1,y1
 plotpoints(ROUND(x),ROUND(y))
 while round(x)!=x2 or round(y)!=y2: 
  x+=Xinc
  y+=Yinc
  plotpoints(ROUND(x),ROUND(y)) 
 plotpoints(ROUND(x),ROUND(y))

def display():
 glClear(GL_COLOR_BUFFER_BIT)
 lineDDA(x1,y1,x2,y2)


x1 = int(input("\nEnter first coordinate:\n\tx: "))
y1 = int(input("\n\ty: "))
x2 = int(input("\nEnter second coordinate:\n\tx: "))
y2 = int(input("\n\ty: "))
glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
glutInitWindowSize(500,500) 
glutInitWindowPosition(200,200)
glutCreateWindow("DDA Line Algorithm") 
init()
glutDisplayFunc(display)
#glutMainLoop()

