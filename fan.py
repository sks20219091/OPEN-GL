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
	glPointSize(2.0)


def pp():
	global angle
	
	glClear(GL_COLOR_BUFFER_BIT)
	glColor3f(0,0.7,0.6)
	angle+=0
	glBegin(GL_POLYGON)
	glVertex2f(0,0)
	glVertex2f(300*cos(radians(angle+20)),300*sin(radians(angle+20)))
	glVertex2f(300*cos(radians(angle-20)),300*sin(radians(angle-20)))
	glEnd()	
	
	angle=angle+120
	
	glBegin(GL_POLYGON)
	glVertex2f(0,0)
	glVertex2f(300*cos(radians(angle+20)),300*sin(radians(angle+20)))
	glVertex2f(300*cos(radians(angle-20)),300*sin(radians(angle-20)))
	glEnd()	
	angle+=120
	
	glBegin(GL_POLYGON)
	glVertex2f(0,0)
	glVertex2f(300*cos(radians(angle+20)),300*sin(radians(angle+20)))
	glVertex2f(300*cos(radians(angle-20)),300*sin(radians(angle-20)))
	glEnd()	
	
	
	glLineWidth(10.0)
	glColor3f(0.9,0.1,1)
	glBegin(GL_LINES)
	glVertex2f(0,0)
	glVertex2f(0,1000)
	glEnd()
	
	glutSwapBuffers()



def redraw(x):
	global angle
	angle+=10
	glutPostRedisplay()
	glutTimerFunc(int(1000/60),redraw,0)





def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_RGB)
	glutInitWindowPosition(50,50)
	glutInitWindowSize(1000,1000)
	
	glutCreateWindow("panka")
	glutDisplayFunc(pp)
	glutTimerFunc(0,redraw,0)
	init()
	glutMainLoop()
main()
