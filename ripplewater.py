from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import random
from math import *

radius=40
max_theta=90
EXPANDING=True

def init():
	glClearColor(0,0.2,0.9,1)
	gluOrtho2D(-500,500,-500,500)

def drawCircle():
	i=0
	while i<max_theta:
		x=radius*cos(radians(i))
		y=radius*sin(radians(i))
		#print it in all 4quadarants
		glPointSize(2.0)
		glBegin(GL_POINTS)
		glVertex2f(x,y)
		glVertex2f(-x,y)
		glVertex2f(-x,-y)
		glVertex2f(x,-y)
		glEnd()
		i=i+1


def update(value):
	global EXPANDING
	global radius
	#update here
	if EXPANDING==True:
		if radius<498:
			radius=radius+2
		else:
			EXPANDING=False
	elif EXPANDING==False:
		if radius>42:
			radius=radius-2
		else:
			EXPANDING=True

	glutPostRedisplay()
	glutTimerFunc(int(1000/60),update,int(0))


def ripples():
	Expanding && glClear(GL_COLOR_BUFFER_BIT)
	drawCircle()
	glColor3f(1,1,1)
	glPointSize(2.0)
	glBegin(GL_POINTS)
	glVertex2f(0,0)
	glEnd()
	glutSwapBuffers()

def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_RGB)

	glutInitWindowPosition(0,0)
	glutInitWindowSize(500,500)
	glutCreateWindow("Ripples in the Water")

	glutDisplayFunc(ripples)
	glutTimerFunc(0,update,0)
	glutIdleFunc(ripples)
	init()
	glutMainLoop()

main()
