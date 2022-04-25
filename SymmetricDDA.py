

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

def lineDDA(x0,y0,xEnd,yEnd):
	delta_x=xEnd-x0
	delta_y=yEnd-y0
	dx=abs(xEnd-x0)
	dy=abs(yEnd-y0)
	x,y=x0,y0
	steps=dx if dx>dy else dy
	if steps !=0:
		change_x=dx/float(steps)
		change_y=dy/float(steps)
	else:
		change_x=0
		change_y=0
	setPixel(ROUND(x),ROUND(y))
	
	for k in range(steps):
		if delta_x >= 0:  
			x+=change_x
		else:
			x-=change_x
		if delta_y >= 0:
			y+=change_y
		else:
			y-=change_y
		setPixel(ROUND(x),ROUND(y))

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
glutMainLoop()

