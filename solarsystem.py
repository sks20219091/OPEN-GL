from OpenGL.GL import*
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import *
angle=0
def init():
	glClearColor(0,0,0,0)
	gluOrtho2D(-1000,1000,-1000,1000)
	glColor3f(0,0,1)
	glPointSize(2.0)
	
def circle():
	global angle
	i=0
	radius=50
	xradius=250
	yradius=150
	glColor3f(1,0,1)
	glBegin(GL_POINTS)
	
	while i<=360:
		radian=(3.14*i)/180
		x=xradius*cos(radian)
		y=yradius*sin(radian)
		
		glVertex2f(x,y)
		
		i=i+1
	glEnd()	
	glColor3f(1,1,0)
	glBegin(GL_TRIANGLE_FAN)
	for i in range(1,361):
		glVertex2f(radius*cos(radians(i)),radius*sin(radians(i)))
	glEnd()
	
	glColor3f(0.3,1,0.3)
	glBegin(GL_TRIANGLE_FAN)
	for i in range(1,361):
		glVertex2f((250*cos(radians(angle)))+radius*cos(radians(i)),150*sin(radians(angle))+radius*sin(radians(i)))
	glEnd()


def redraw(x):
	global angle
	angle+=10
	
	glutPostRedisplay()
	glutTimerFunc(int(1000/60),redraw,0)
	
	
	
		
	
	
	
def pp():
	glClear(GL_COLOR_BUFFER_BIT)
	
	glBegin(GL_POINTS)
	glVertex2f(0,0)
	glEnd()
	circle()
	glutSwapBuffers()
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
