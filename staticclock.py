from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import *


radius=50

def init():
	glClearColor(0,0,0,1)
	gluOrtho2D(-100,100,-100,100)
	
def printHands():
	glLineWidth(10.0)
	glColor3f(0.5,0.6,0.7)
	
	glBegin(GL_LINES)
	glVertex2f(0,0)
	glVertex2f(0,radius)
	glEnd()
	
	glColor3f(1.0,1.0,0.7)
	
	glBegin(GL_LINES)
	glVertex2f(0,0)
	glVertex2f(-radius,0)
	glEnd()
	
	
	
def drawCircle():
	i=0
	while i<=360:
		#step1 : convert degree to radians
		toRadians = radians(i)
		x_coord=radius*cos(toRadians)
		y_coord=radius*sin(toRadians)
		
		glBegin(GL_POINTS)
		glVertex2f(x_coord,y_coord)
		glEnd()
		
		i=i+30
		
	printHands()

		
		
		
	
def plotpoints():
	glClear(GL_COLOR_BUFFER_BIT)
	glPointSize(5.0)
	glColor3f(0,0,1)


	'''glBegin(GL_LINES)
	glVertex2f(200,0)
	glVertex2f(0,0)
	glEnd()'''
	drawCircle()
	glFlush()

def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_RGB)
	glutInitWindowPosition(500,50)
	glutInitWindowSize(500,500)
	glutCreateWindow("PLOT POINTS")
	glutDisplayFunc(plotpoints)
	init()
	glutMainLoop()
main()



