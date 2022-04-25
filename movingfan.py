from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import *
import sys
import numpy

x1=100
y1=0
x2=0
angle=0

def init():
	glClearColor(0,0,0,1)
	gluOrtho2D(-500,500,-500,500)

def plotAfterRotation(x,y,angl):
	
	x_new = x*cos(radians(angl)) - y*sin(radians(angl))
	y_new = x*sin(radians(angl)) + y*cos(radians(angl))

	#onw will be 0,0
	x1=x_new*cos(radians(10)) - y_new*sin(radians(10))
	y1=x_new*sin(radians(10)) + y_new*cos(radians(10))

	x2=x_new*cos(radians(-10)) - y_new*sin(radians(-10))
	y2=x_new*sin(radians(-10)) + y_new*cos(radians(-10))
	glColor3f(0.5,0.7,0.8)
	glLineWidth(15.0)
	glBegin(GL_POLYGON)
	glVertex2f(0,0)
	glVertex2f(x1,y1)
	glVertex2f(x2,y2)
	glEnd()






def drawBlades():
	global angle
	glColor3f(0.5,0.7,0.8)
	glLineWidth(8.0)
	
	
	plotAfterRotation(200,0,angle+0)
	
	plotAfterRotation(200,0,angle+120)
	plotAfterRotation(200,0,angle+240)

def redraw(value):
	#update here
	global angle
	angle=angle+0.5
	glutPostRedisplay()
	glutTimerFunc(int(1000/60),redraw,int(0))



def plotAxes():
	
	glLineWidth(0.002)
	glColor3f(1,0,1)
	start = -500
	while start<=500:
		glBegin(GL_LINES)
		
		glVertex2f(start,500)
		glVertex2f(start,-500)
		glEnd()
		start = start + 50
	start=-500
	while start<=500:
		glBegin(GL_LINES)
		#glLineWidth(2.0)
		glVertex2f(500,start)
		glVertex2f(-500,start)
		glEnd()
		start = start + 50



def drawFan():
	glClear(GL_COLOR_BUFFER_BIT)
	#plotAxes()
	glPointSize(10.0)
	glColor3f(0,0,1)
	glBegin(GL_POINTS)
	glVertex2f(0,0)
	glEnd()
	drawBlades()
	glutSwapBuffers()
	glFlush()

def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_RGB)

	glutInitWindowPosition(0,0)
	glutInitWindowSize(500,500)
	glutCreateWindow("Moving Fan")
	
	glutDisplayFunc(drawFan)
	glutTimerFunc(0,redraw,0)
	glutIdleFunc(drawFan)
	init()
	glutMainLoop()
main()
