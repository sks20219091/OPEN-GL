from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import *

def init():
	glClearColor(0,1,1,0)
	gluOrtho2D(-100,100,-100,100)
	
	
	
def circle():
	r=50
	i=0
	while i<=360:
		rad = radians(i)
		x=r*cos(rad)
		y=r*sin(rad)
		glBegin(GL_POINTS)
		glVertex(x,y)
		glEnd()
		
		i=i+90
	glBegin(GL_LINES)
	glVertex2f(0,0)
	glVertex(0,r)
	glEnd()

	glBegin(GL_LINES)
	glVertex2f(0,0)
	glVertex(r,0)
	glEnd()	
	
	
	
	
	
	
		
	
	
	
def pp():
	
	glClear(GL_COLOR_BUFFER_BIT)
	glColor3f(1,0.5,0)
	
	glPointSize(10.0)
	glBegin(GL_POINTS)
	glVertex2f(0,0)
	glEnd()
	glColor3f(1,0.5,0)
	
	glPointSize(4.0)
	
	circle()
	glFlush()
	
	
	
	
	
	
	
def main():


	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
	glutInitWindowPosition(500,20)
	glutInitWindowSize(500,500)
	
	glutCreateWindow("porn")
	glutDisplayFunc(pp)
	init()
	glutMainLoop()
main()
