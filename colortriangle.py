from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def init():
	glClearColor(0,0,0,0) 			#set background color
	gluOrtho2D(-500,500,-500,500)
	
def plotpoints():
	glClear(GL_COLOR_BUFFER_BIT)
	glColor3f(0,0,1)
	
	glBegin(GL_POLYGON)
	glVertex2f(-100,100)
	glVertex2f(-100,-100)
	glVertex2f(100,-100)
	glVertex2f(100,100)
	glEnd()
	
	glColor3f(0,0,0)
	glBegin(GL_LINES)
	glVertex2f(-100,100)
	glVertex2f(100,-100)
	glEnd()
	glColor3f(0,0,0)
	glBegin(GL_LINES)
	glVertex2f(100,100)
	glVertex2f(-100,-100)	
	glEnd()
	
	glColor3f(0,1,1)
	
	glBegin(GL_POLYGON)
	glVertex2f(-100,100)
	glVertex2f(0,200)
	
	glVertex2f(100,100)
	glEnd()
	
	glColor3f(1,0.4,1)
	
	glBegin(GL_POLYGON)
	
	glVertex2f(200,0)
	glVertex2f(100,-100)
	glVertex2f(100,100)
	glEnd()
	
	glColor3f(0.3,0,0.5)
	
	glBegin(GL_POLYGON)
	
	glVertex2f(-100,-100)
	glVertex2f(100,-100)
	glVertex2f(0,-200)
	glEnd()
	
	glColor3f(0.2,0.4,0.4)
	
	glBegin(GL_POLYGON)
	
	glVertex2f(-200,0)
	glVertex2f(-100,-100)
	glVertex2f(-100,100)
	glEnd()
		
	glutSwapBuffers()
	
def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
	glutInitWindowPosition(0,0)
	glutInitWindowSize(1024,768)
	
	glutCreateWindow("point")
	glutDisplayFunc(plotpoints)
	glutTimerFunc(0,timer,0)
	init()
	glutMainLoop()
	
main()
