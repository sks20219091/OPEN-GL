from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import *
import sys
angle=0
def init():
	glClearColor(0,0,0,0)
	gluOrtho2D(-1000,1000,-1000,1000)
	glColor3f(0,0,1)
	glPointSize(10.0)


def pp():
	global angle
	i=0
	glClear(GL_COLOR_BUFFER_BIT)
	glColor3f(0,0,1)
	glBegin(GL_POINTS)
	while i<=360:
		glVertex2f(200*cos(radians(i)),200*sin(radians(i)))
		i=i+30
		
	glEnd()
	
	
	glColor3f(1,1,0)
	glLineWidth(10.0)
	glBegin(GL_LINES)
	glVertex2f(0,0)
	glVertex(180*cos(radians(angle)),180*sin(radians(angle)))
	glEnd()
	
	glutSwapBuffers()
	
	
	
	
	
	
	
def redraw(e):
	global angle
	angle-=6
	glutPostRedisplay()
	glutTimerFunc(int(60000/60),redraw,0)
	


def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_RGB|GLUT_DOUBLE)
	glutInitWindowPosition(50,50)
	glutInitWindowSize(1000,1000)
	
	glutCreateWindow("sumit")
	glutDisplayFunc(pp)
	glutTimerFunc(0,redraw,0)
	init()
	glutMainLoop()
main()
