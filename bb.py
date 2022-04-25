from OpenGL.GL import *
from OpenGL.GLU  import *
from OpenGL.GLUT import *
from math import *
import sys
right=False
left=False
top=False
bottom=True
x=-1000
y=1000
def init():
	glClearColor(0,1,0,1)
	gluOrtho2D(-1000,1000,-1000,1000)

def pp():
	glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
	glutSolidSphere(3,20,20)
	glPointSize(5.0)
	glColor3f(0,0,1)
	glLineWidth(10.0)
	glBegin(GL_LINES)
	glVertex2f(-1000,0)
	glVertex2f(1000,0)
	glEnd()
	circle()
	
	glutSwapBuffers()
	
def circle():
	global x,y
	global left,right ,top,bottom
	i=0
	glColor3f(1,1,0)
	glBegin(GL_TRIANGLE_FAN)
	for i in range(1,361):
		glVertex2f(x+100*cos(radians(i)),y+100*sin(radians(i)))
	glEnd()


def redraw(u):
	global x,y
	global right,left,top,bottom
	if right==True:
		if x<=900:
			x+=20
		else:
			right=False
			
	elif left==True:
		if x>=-900:
			x-=20
		else:
			
			left=False
			
	elif top==True:
		if y<=900:
			y+=20
		else:
			top=False
			
		
	elif bottom==True:
		if y>=100:
			y=y-20
		else:
			
			bottom=False
		
		
		
		
	glutPostRedisplay()
	glutTimerFunc(int(1000/60),redraw,0)

	
def control(key,u,v):
	global x,y
	global left,right,top,bottom
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


def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
	glutInitWindowSize(1000,1000)
	glutInitWindowPosition(50,50)
	
	glutCreateWindow("GEND")
	glutDisplayFunc(pp)
	glutTimerFunc(0,redraw,0)
	glutKeyboardFunc(control)
	init()
	glutMainLoop()
main()




