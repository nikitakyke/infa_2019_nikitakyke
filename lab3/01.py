from graph import *
import math
windowSize(500, 600)
def eye(x, y, r, what):
	brushColor(200, 0, 0)
	circle(x, y, r)
	brushColor(0, 0, 0)
	circle(x, y, r/3)
	
	h=5; l=150
	x=x+what*5/4*r
	y=y-r/2*math.cos(math.pi/6)
	v2=(x+what*h/2, y-h*math.cos(math.pi/6))
	v3=(x+what*h/2-what*l*math.cos(math.pi/6), y-h*math.cos(math.pi/6)-l/2)
	v4=(x-what*l*math.cos(math.pi/6), y-l/2)
	polygon([(x, y), v2, v3, v4])
	
brushColor(150, 150, 150)
rectangle(0, 0, 500, 600)

penSize(2)
brushColor('yellow')
circle(250, 300, 200)

eye(180, 240, 35, 1)
eye (320, 240, 30, -1)

x=150; y=350
rectangle(x, y, x+200, y+40)

run()
