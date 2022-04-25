from OpenGL.Gl import *
from OPenGL.GLU import *
from OPenGL.GLUT import *

def init() :
	glClearColor(R,G,B,1.0)
	gluOrtho2D(-1.0,1.0,-1.0,1.0)

def plotPoints():
	glClear(GL_COLOR_BUFFER_BIT)
	GlColor3f(R,G,B,1.0)
	glPointSize(10.0)
	glBegin(GL_POINTS)
	glVertex2f(0.0)
	glEnd()
	glflush()

def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE|GLUR_RGB)
	glutInitWindowSize(500,500)
	glutInitWindowPosition(50,50)
	glutCreateWindow("poitn Plotting")
	glutDisplayFunc(plotpoint)
	init()
	glutMainLoop()
main()
