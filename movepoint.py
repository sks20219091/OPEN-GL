from OpenGL.GL import *
from OpenGL.GLU import *     #opengl utility library
from OpenGL.GLUT import *    #opengl utility toolkit
import sys
import math

def init():
	glClearColor(0.0,0.0,0.0,1.0)		#set background color
	gluOrtho2D(-1.0,1.0,-1.0,1.0)		#set the range of coordinate system

def plotpoints():
	glClear(GL_COLOR_BUFFER_BIT)  	#clear the entire window to the background color
	glColor3f(1.0,1.0,0.0)			#set color of drawing
	glPointSize(10.0)			#set pixel size
	glBegin(GL_POINTS)
	glVertex2f(0.0,0.0)			#plot the vertex
	glEnd()
	glFlush()				#push the pixels to display

def main():
	glutInit(sys.argv)			#initialize toolkit
	glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)	#set display mode
	glutInitWindowPosition(250,250)		#set window position
	glutInitWindowSize(500,500)		#set window size
	
	glutCreateWindow("Plot Orign")	#create a window with given name
	glutDisplayFunc(plotpoints)		#register redraw function
	init()					#additionalinitilizations
	glutMainLoop()				#call back loop 

main()

