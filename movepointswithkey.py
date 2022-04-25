from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math
import random

x=0
y=0
right=True
left=False
top=False
bottom=False

def init():
	glClearColor(0,0,0,0)
	gluOrtho2D(-500,500,-500,500)
	glColor3f(0,0,1)
	
def pp():
	global x,y
	glClear(GL_COLOR_BUFFER_BIT)
	
	glPointSize(100.0)
	glBegin(GL_POINTS)
	glVertex2f(x,y)
	glEnd()
	glutSwapBuffers()

def Redraw(w):
	global x,y
	global right,left,bottom,top
	if right==True:
		if x<450:
			
			x=x+10
		else:	
			glColor3f(math.cos(random.randrange(0,90)),math.cos(random.randrange(0,90)),
			math.cos(random.randrange(0,90)))
			right=False
			left=True
			top=True
			bottom=True
	elif left==True:
		if x>-450:
			
			x=x-10
		else:	
			glColor3f(math.cos(random.randrange(0,90)),math.cos(random.randrange(0,90)),
			math.cos(random.randrange(0,90)))
			left=False
			Top=True
			bottom=True
			right=True
	elif bottom==True:
		if y>-450:
			
			y=y-10
		else:
			bottom=False
			top=True
			left=True
			right=True
			
	elif top==True:
		if y<450:
			y=y+10
		else:
			top=False
			right=True
			left=True
			bottom=True
	
			
	
	glutPostRedisplay()
	glutTimerFunc(int(1000/60),Redraw,0)

def Control(key,w,m):
	global x,y
	global right,left,bottom,top
	
	if key==b"d":
		right=True
		left=False
		top=False
		bottom=False
	elif key==b"a":
		right=False
		left=True
		top=False
		bottom=False
	elif key==b"w":
		right=False
		left=False
		top=True
		bottom=False
	elif key==b"x":
		right=False
		left=False
		top=False
		bottom=True
	elif key==b"s":
		x=x+100
	elif key==b"l":
		x=x-100


def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_RGB|GLUT_DOUBLE)
	glutInitWindowPosition(50,50)
	glutInitWindowSize(1024,768)
	
	glutCreateWindow("vkpp")
	glutDisplayFunc(pp)
	glutKeyboardFunc(Control)
	glutTimerFunc(0,Redraw,0)
	init()
	glutMainLoop()
main()
