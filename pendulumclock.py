from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
from math import *
import datetime 
import pytz 

current_time = datetime.datetime.now(pytz.timezone('Asia/Kolkata')) 

CURR_HOUR=current_time.hour%12
CURR_MINUTE=current_time.minute
CURR_SECOND=current_time.second

print(CURR_HOUR)

CLOCK_DIAL=180
NUMBER_RADIUS=float(CLOCK_DIAL-15)
MINUTES=90-CURR_MINUTE*6
HOURS=90-(CURR_HOUR*30+(CURR_MINUTE/60)*30)
SECONDS=6*CURR_SECOND

MINUTES_RADIUS=150
HOURS_RADIUS=100
SECONDS_RADIUS=150


ANGLE_MIN=-120
ANGLE_MAX=-60
ANGLE=-60
INCREASING=True
BOB_RADIUS=40

def init():
	gluOrtho2D(-500,500,-600,400)
	glClearColor(0,0,0,1)


def drawDial():
	i=0
	glColor3f(0,0.5,0.5)
	glPointSize(2.5)
	glBegin(GL_POINTS)
	while i<=360:
		glVertex2f(CLOCK_DIAL*cos(radians(i)),CLOCK_DIAL*sin(radians(i)))
		i=i+0.5
	glEnd()

def drawNumbers():
	glColor3f(1,0.5,0)
	i=0
	glPointSize(6.5)
	glBegin(GL_POINTS)
	while i<=360:
		glVertex2f(NUMBER_RADIUS*cos(radians(i)),NUMBER_RADIUS*sin(radians(i)))
		i=i+30
	glEnd()

def drawBox():
	glColor3f(1,0,0.5)
	glBegin(GL_POLYGON)
	glVertex2f(CLOCK_DIAL*cos(radians(330)),CLOCK_DIAL*sin(radians(330)))
	glVertex2f(CLOCK_DIAL*cos(radians(210)),CLOCK_DIAL*sin(radians(210)))
	glVertex2f(CLOCK_DIAL*cos(radians(210)),-500)
	glVertex2f(CLOCK_DIAL*cos(radians(330)),-500)
	glEnd()

def drawHands():
	#FOR HOURS
	glColor3f(0,float(204/255),0)
	glLineWidth(7.5)
	glBegin(GL_LINES)
	glVertex2f(0,0)
	glVertex2f(HOURS_RADIUS*cos(radians(HOURS)),HOURS_RADIUS*sin(radians(HOURS)))
	glEnd()

	#FOR MINUTES
	glColor3f(float(51/255),float(255/255),float(255/255))
	glLineWidth(7.5)
	glBegin(GL_LINES)
	glVertex2f(0,0)
	glVertex2f(MINUTES_RADIUS*cos(radians(MINUTES)),MINUTES_RADIUS*sin(radians(MINUTES)))
	glEnd()

	#FOR SECONDS
	glColor3f(float(78/255),float(104/255),float(200/255))
	glLineWidth(7.5)
	glBegin(GL_LINES)
	glVertex2f(0,0)
	glVertex2f(SECONDS_RADIUS*cos(radians(SECONDS)),SECONDS_RADIUS*sin(radians(SECONDS)))
	glEnd()

def drawPendulum():

	glBegin(GL_LINES)
	glVertex2f(0,0)
	glVertex2f(500*cos(radians(ANGLE)),500*sin(radians(ANGLE)))
	glEnd()

	glColor3f(0,0,0)
	glLineWidth(10.0)
	glBegin(GL_LINES)
	glVertex2f(0,0)
	glVertex2f(CLOCK_DIAL*cos(radians(ANGLE)),(CLOCK_DIAL-1)*sin(radians(ANGLE)))
	glEnd()


	#drawing bob
	glColor3f(1,1,0)
	glBegin(GL_TRIANGLE_FAN)
	glVertex2f((500+BOB_RADIUS)*cos(radians(ANGLE)),(500+BOB_RADIUS)*sin(radians(ANGLE)))
	i=0
	while i<=360:
		glVertex2f((500+BOB_RADIUS)*cos(radians(ANGLE))+(BOB_RADIUS)*cos(radians(i)),(500+BOB_RADIUS)*sin(radians(ANGLE))+(BOB_RADIUS)*sin(radians(i)))
		i=i+1
	glEnd()




def plot():
	glClear(GL_COLOR_BUFFER_BIT)
	#drawBox()

	drawDial()
	drawNumbers()
	drawHands()
	drawPendulum()

	glPointSize(5.0)
	glBegin(GL_POINTS)
	glVertex2f(0,0)
	glEnd()
	glutSwapBuffers()


def update(x):
	global SECONDS,MINUTES,HOURS,ANGLE,INCREASING
	SECONDS=(SECONDS-6)%360
	MINUTES=((MINUTES-float(1/12)))
	HOURS=HOURS-float(30/3600)

	if INCREASING==True:
		if ANGLE>ANGLE_MIN:
			ANGLE=ANGLE-30
		else:
			INCREASING=False
	else:
		if ANGLE<ANGLE_MAX:
			ANGLE=ANGLE+30
		else:
			INCREASING=True
	glutPostRedisplay()
	glutTimerFunc(int(61000/60),update,int(0))


def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_RGBA)
	glutInitWindowSize(800,800)
	glutInitWindowPosition(0,0)
	glutCreateWindow("Clock")
	glutDisplayFunc(plot)
	glutTimerFunc(0,update,0)
	glutIdleFunc(plot)
	init()
	glutMainLoop()
main()
