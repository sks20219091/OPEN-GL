from OpenGL.GL import *
from OpenGL.GLU  import *
from OpenGL.GLUT import *
from math import *
right=True
left=False
top=False
bottom=False
x=0
y=100
def init():
	glClearColor(0,0,0,1)
	gluOrtho2D(-1000,1000,-1000,1000)

def pp():
	glClear(GL_COLOR_BUFFER_BIT)
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
			left=True
			top=False
			bottom=False
	elif left==True:
		if x>=-900:
			x-=20
		else:
			right=True
			left=False
			top=False
			bottom=False
	elif top==True:
		if y<=900:
			y+=20
		else:
			right=False
			left=False
			top=False
			bottom=True
		
	elif bottom==True:
		if y>=100:
			y=y-20
		else:
			right=False
			left=False
			top=True
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
	glutInitDisplayMode(GLUT_RGB|GLUT_DOUBLE)
	glutInitWindowSize(1000,1000)
	glutInitWindowPosition(50,50)
	
	glutCreateWindow("GEND")
	glutDisplayFunc(pp)
	glutTimerFunc(0,redraw,0)
	glutKeyboardFunc(control)
	init()
	glutMainLoop()
main()




