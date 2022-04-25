from OpenGL.GL import *
from OpenGL.GLU import *     #opengl utility library
from OpenGL.GLUT import *    #opengl utility toolkit
import sys
import math
import random
xcor=0
right=True
left=False
top=False
bottom=False
ycor=0
step=5
def init():
	glClearColor(0.0,0.0,0.0,1.0)
	glColor3f(0.9,1,0)
	gluOrtho2D(-1024,1024,-1024,1024)		#set the range of coordinate system

def plotpoints():
	global xcor
	global ycor
	glClear(GL_COLOR_BUFFER_BIT)  	#clear the entire window to the background color
			
	glPointSize(100.0)		
	glBegin(GL_POINTS)
	glVertex2f(xcor,ycor)			#plot the vertex
	glEnd()
	glutSwapBuffers()
	
def redraw(x):
	global xcor
	global right
	global step
	global ycor
	global top,bottom,left
	if right==True:
		glColor3f(math.cos(random.randrange(0,90)),math.cos(random.randrange(0,90)),
			math.cos(random.randrange(0,90)))
		if xcor<974:
			xcor+=step
		else:
			left=True
			right=False
			top=False
			bottom=False
	elif left==True:
		glColor3f(math.cos(random.randrange(0,90)),math.cos(random.randrange(0,90)),
			math.cos(random.randrange(0,90)))
		if xcor>-1100:
			xcor=xcor-step
		else:	
			
			right=True
			left=False
			top=False
			bottom=False
	elif bottom==True:
		glColor3f(math.cos(random.randrange(0,90)),math.cos(random.randrange(0,90)),
			math.cos(random.randrange(0,90)))
		if ycor>-1100:
			ycor=ycor-step
		else:	
			
			right=False
			left=False
			top=True
			bottom=False
	elif top==True:
		glColor3f(math.cos(random.randrange(0,90)),math.cos(random.randrange(0,90)),
			math.cos(random.randrange(0,90)))
		if ycor<1100:
			ycor=ycor+step
		else:	
			
			right=False
			left=False
			top=False
			bottom=True
	
			
	glutPostRedisplay()
	glutTimerFunc(int(1000/60),redraw,0)
	
	
def control(key,x,y):
	global right,left,top,bottom
	global step
	if key==b"d":
		right=True
		left=False
		top=False
		bottom=False
	elif key==b"a":
		right=False
		left=True
		top=False
		bottom=False
	elif key==b"w":
		right=False
		left=False
		top=True
		bottom=False
	elif key==b"s":
		right=False
		left=False
		top=False
		bottom=True
	elif key==b"f":
		step+=5
	elif key==b"l":
		step-=5
		if step<=0:
			step=0
		
	
	
	
				

def main():
	glutInit(sys.argv)			#initialize toolkit
	glutInitDisplayMode(GLUT_DOUBLE |GLUT_RGB)	#set display mode
	glutInitWindowPosition(250,250)		#set window position
	glutInitWindowSize(1024,768)		#set window size
	
	glutCreateWindow("Plot Orign")	#create a window with given name
	glutDisplayFunc(plotpoints)
	glutKeyboardFunc(control)
	glutTimerFunc(0,redraw,0)
			#register redraw function
	init()					
	glutMainLoop()				#call back loop 

main()

