from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from dda_import import *
import sys

INSIDE=0 # 0000
TOP=8 #1000
BOTTOM=4 # 0100
RIGHT=2 #0010
LEFT=1 #0001



def init():
	glClearColor(1.0,1.0,1.0,0.0)
	glColor3f(1.0,0.0,0.0)
	glPointSize(3.0)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluOrtho2D(0.0,600.0,0.0,600.0)
	
def getinput():
	while True:
		x1=input("\nEnter x1 of line : ")
		y1=input("Enter y1 of line : ")
		x2=input("Enter x2 of line : ")
		y2=input("Enter y2 of line : ")
		cohensutherland(x1,y1,x2,y2)
		print("Enter any number to continue : ")
		n=int(input("Enter number 0 to exit : "))
		if n==0:
			break
		else:
			pass
		
	
def getwindow():
	global xw_min,yw_min,xw_max,yw_max
	xw_min=input("Enter xw_min of window : ")
	yw_min=input("Enter yw_min of window : ")
	xw_max=input("Enter xw_max of window : ")
	yw_max=input("Enter yw_max of window : ")
	
		
def getcode(x,y):
	code=INSIDE
	if x<xw_min:
		code=code|LEFT
	elif x>xw_max:
		code=code|RIGHT
	if y<yw_min:
		code=code|BOTTOM
	elif y>yw_max:
		code=code|TOP
	return code
	
def display():
	glClear(GL_COLOR_BUFFER_BIT)
	lineDDA(xw_min,yw_min,xw_max,yw_min)
	lineDDA(xw_min,yw_min,xw_min,yw_max)
	
	lineDDA(xw_max,yw_min,xw_max,yw_max)
	lineDDA(xw_min,yw_max,xw_max,yw_max)
	
	getinput()
	
def cohensutherland(x1,y1,x2,y2):
	code1=getcode(x1,y1)
	code2=getcode(x2,y2)
	accept=False
	while True:
		if code1==0 and code2==0:
			accept=True
			break
		elif(code1 & code2)!=0:
			break
		else:
			x=0.0
			y=0.0
			dx=x2-x1
			dy=y2-y1
			if dx!=0:
				m=dy/dx
			if code1!=0:
				code_out=code1
			else:
				code_out=code2
			
			if code_out & TOP:
				y=yw_max
				if dx==0:
					x=x1
				else:
					x=x1+(yw_max-y1)/m
					
			elif code_out & BOTTOM :
				y=yw_min
				if dx==0:
					x=x1
				else:
					x=x1+(yw_min-y1)/m
					
			elif code_out & RIGHT:
				x=xw_max
				y=y1+(xw_max-x1)*m
			elif code_out & LEFT :
				x=xw_min
				y=y1+(xw_min-x1)*m
			if code_out==code1:
				x1=x
				y1=y
				code1=getcode(x1,y1)
			else:
				x2=x
				y2=y
				code2=getcode(x2,y2)
	if accept:
	
		lineDDA(ROUND(x1),ROUND(y1),ROUND(x2),ROUND(y2))
	else:
		print(" Line is out of window ")
		
	
def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
	glutInitWindowSize(600,600)
	glutInitWindowPosition(50,50)
	glutCreateWindow("LINE CLIP ")
	getwindow()
	glutDisplayFunc(display)
	init()
	glutMainLoop()
