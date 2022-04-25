from OpenGL.GL import*
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import *
import sys

angle=0
angle2=0
def init():
	glClearColor(0,0,0,0)
	gluOrtho2D(-1000,1000,-1000,1000)
	glColor3f(0,0,1)
	glPointSize(2.0)

def pp():
	glClear(GL_COLOR_BUFFER_BIT)
	global angle,angle2
	i=0
	glColor3f(1,0.5,1)
	glBegin(GL_POINTS)
	for i in range(1,361):
		glVertex2f(300*cos(radians(i)),150*sin(radians(i)))
	glEnd()		
	
	
	glColor3f(0.3,0.7,0.8)
	glBegin(GL_POINTS)
	for i in range(1,361):
		glVertex2f(500*cos(radians(i)),250*sin(radians(i)))
		
	glEnd()
	
	
	glColor3f(0.4,0.5,1)
	glBegin(GL_TRIANGLE_FAN)
	for i in range(1,361):
		glVertex2f(300*cos(radians(angle))+50*cos(radians(i)),150*sin(radians(angle))+50*sin(radians(i)))
	
	glEnd()
	
	glColor3f(0,0.5,0.4)
	glBegin(GL_TRIANGLE_FAN)
	for i in range(1,361):
		glVertex2f(500*cos(radians(angle2))+69*cos(radians(i)),250*sin(radians(angle2))+69*sin(radians(i)))
	
	glEnd()
	glColor3f(1,1,0)
	glBegin(GL_TRIANGLE_FAN)
	for i in range (1,361):
		glVertex2f(50*cos(radians(i)),50*sin(radians(i)))
	glEnd()
	glutSwapBuffers()
	
def redraw(x):
	
	global angle,angle2
	angle+=5
	angle2+=8
	
	glutPostRedisplay()
	glutTimerFunc(int(1000/60),redraw,int (0))


def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_RGB|GLUT_DOUBLE)
	glutInitWindowSize(1000,1000)
	glutInitWindowPosition(50,50)
	
	glutCreateWindow("Vayumandal")
	glutDisplayFunc(pp)
	glutTimerFunc(0,redraw,0)
	
	
	init()
	glutMainLoop()
main()
