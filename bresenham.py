from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def init():
	glClearColor(0,0,0,0)
	gluOrtho2D(-500,500,-500,500)
	
def Bresenham():
		
	
	
	
	
	
	
		
		
		
			
		
	
def pp():
	glClear(GL_COLOR_BUFFER_BIT)
	glColor3f(0,0,1)
	glPointSize(10.0)
	glBegin(GL_POINTS)
	glVertex2f(0,0)
	glEnd()
	glFlush()
	
	
def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_RGB|GLUT_SINGLE)
	glutInitWindowPosition(50,50)
	glutInitWindowSize(500,500)
	glutCreateWindow("sumit")
	glutDisplayFunc(pp)
	init()
	glutMainLoop()
main()
	
