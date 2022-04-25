from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *



def init():
    glClearColor(0, 0, 0, 1.0)
    glColor3f(0,0,1)
    glPointSize(2.0)
    gluOrtho2D(0,1600,0,900)

def plotpoints(x,y):
    """
    Method to plot point on the screen
    """
    glBegin(GL_POINTS)
    glVertex2i(x,y)
    glEnd()
    glFlush()


def display(xc,yc,r):
    glClear(GL_COLOR_BUFFER_BIT)
    plot_circle(xc,yc,r)

def plot_circle(xc,yc,r):
    x = 0
    y = r
    di = 2*(1-r)
    limit = 0
    def mh(x,y,di):
        x = x+1
        di = di + 2*x + 1
        return(x,y,di)

    def md(x,y,di):
        x = x+1
        y = y-1
        di = di + 2*x - 2*y + 2
        return(x,y,di)

    def mv(x,y,di):
        y = y-1
        di = di - 2*y + 1
        return(x,y,di)

    while(y>limit):
        plotpoints(xc+x,yc+y)
        plotpoints(xc+x,yc-y)
        plotpoints(xc-x,yc-y)
        plotpoints(xc-x,yc+y)

        if di<0:
            d = 2*di+2*y-1
            if d<=0:
                (x,y,di) = mh(x,y,di)
            else:
                (x,y,di) = md(x,y,di)
        elif di>0:
            d = 2*di-2*x-1
            if d<=0:
                (x,y,di) = md(x,y,di)
            else:
                (x,y,di) = mv(x,y,di)
        elif di==0:
            (x,y,di) = md(x,y,di)
    
def main():

	xc = int(input("\nEnter x coordinate of centre:\n\tx: "))
	yc = int(input("\nEnter y coordinate of centre:\n\ty: "))
	r = int(input("\nEnter radius of circle:\n\tr: "))
	glutInit()
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)   
	glutInitWindowSize(1600, 900)
	glutInitWindowPosition(200, 200)
	glutCreateWindow("Bresenham Circle")
	init()
	glutDisplayFunc(lambda: display(xc,yc,r))
	glutMainLoop()
	
main()
