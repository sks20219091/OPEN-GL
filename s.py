from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math
x=0
r=True
def init():
	glClearColor(0,0,0,0) #set background color
	gluOrtho2D(0,1024,1024,0)
	
def plotpoints():
	glClear(GL_COLOR_BUFFER_BIT)
	glColor3f(0.9,1,0)
	glPointSize(50.0)
	glBegin(GL_POINTS)
	glVertex2f(512,x)
	glEnd()
	glutSwapBuffers()
	
def redraw(y):
	global x
	global r
	if r==True:
		if x<974:
			x+=10
		else:	
			glColor3f(math.cos(random.randrange(0,50)),0,0)
			glColor3f(0,0,1)
			r=False
	else:
		if x > 50:
			x-=10
		else:	
			glColor3f(1,0,0)
			r=True
	glutPostRedisplay()
	glutTimerFunc(int(1000/60),redraw,0)
	
def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_DOUBLE|GLUT_RGB)
	glutInitWindowPosition(250,250)
	glutInitWindowSize(1024,768)
	
	glutCreateWindow("point")
	glutDisplayFunc(plotpoints)
	glutTimerFunc(0,redraw,0)
	init()
	glutMainLoop()
	
main()
