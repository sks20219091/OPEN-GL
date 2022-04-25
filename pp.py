from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import *

angle=0.0

def init():
	glClearColor(0,0,0,0)
	gluOrtho2D(-500,500,-500,500)
	glColor3f(1,1,0)
	glPointSize(2.0)

def redraw(x):
	global angle
	glutPostRedisplay()
	glutTimerFunc(int(1000/60),redraw,0)
	angle+=5
	

def circle():
	global angle
	rx=200
	ry=150
	
	i=0
	while i<=360:
		rad = (3.14*i)/180
		x=rx*cos(rad)
		y=ry*sin(rad)
		glColor3f(1,0,0)
		glBegin(GL_POINTS)
		glVertex2f(x,y)
		glEnd()
		i=i+1
	
	
	glColor3f(0.5,0.5,0.8)
	glBegin(GL_TRIANGLE_FAN)
	
	i=0
	r=50
	while i<=360:
		rad = (3.14*i)/180
		x=r*cos(rad)
		y=r*sin(rad)
		glVertex2f(x+200*cos(radians(angle)),y+150*sin(radians(angle)))
		i=i+1
	glEnd()
	
	
	
	
	glColor3f(1,1,0)
	glBegin(GL_TRIANGLE_FAN)
	
	i=0
	r=100
	while i<=360:
		rad = (3.14*i)/180
		x=r*cos(rad)
		y=r*sin(rad)
		glVertex2f(x,y)
		i=i+1
	glEnd()

	
		
		

def pandaal():
	glLineWidth(2.0)	
	i=400
	j=400
	while i >= -400:
		glBegin(GL_LINES)
		glVertex2f(-500,i)
		glVertex2f(500,i)
		glEnd()
		i=i-100
		
	while j >= -400:
		glBegin(GL_LINES)
		glVertex2f(j,500)
		glVertex2f(j,-500)
		glEnd()
		j=j-100
	
	
	
def pp():
	glClear(GL_COLOR_BUFFER_BIT)
	#pandaal()
	circle()
	glutSwapBuffers()

def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_DOUBLE|GLUT_RGB)
	glutInitWindowPosition(10,50)
	glutInitWindowSize(500,500)
	glutCreateWindow("sumit")
	glutDisplayFunc(pp)
	glutTimerFunc(0,redraw,0)
	init()
	glutMainLoop()
main()	
	
	
