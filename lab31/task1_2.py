from graph import *
from typing import Any
from math import pi, sin, cos
windowSize(500, 400)
penColor('purple')
rectangle(0, 0, 500, 400)
brushColor(204, 255, 255)
rectangle(0, 0, 500, 200)
brushColor(0, 0, 102)
rectangle(0, 200, 500, 300)
penColor(255, 204, 0)
brushColor(255, 200, 0)
circle(455, 45, 40)

N=40
penSize(2)
ugol=2*pi/N
for i in range(N):
	line(455, 45, 70*sin(ugol*i)+455, 70*cos(ugol*i)+45)
	
rectangle(0, 300, 500, 400)
n = 13
r = 500 / (n * 2)
x = r
for i in range(n):
    circle(x, 310, r)
    x += 2 * r
penColor(102, 51, 0)
penSize(5)
line(55, 280, 55, 390)
brushColor(255, 69, 0)
penSize(1)
polygon([(5, 280), (55, 260), (60, 260), (110, 280)])
brushColor(128, 0, 0)
penColor(128, 0, 0)
pol=[]
i=1
t=0
while t !=pi/2:
    t = i / 200 * pi
    dx =250- 30 * cos(t)
    dy = 220+ 30 * sin(t)
    pol.append((dx, dy))
    i+=1
polygon(pol)
polygon([(250,250),(350,250),(420,220),(220,220)])
penSize(5)
penColor(50,0,0)
line(295,220,295,120)
penSize (2)
brushColor(200,200,200)
polygon([(295,220),(390,170),(320,170),(295,220)])
polygon([(295,120),(390,170),(320,170),(295,120)])
circle(356,235,9)
x=100
y=70
penSize(1)
penColor(0,0,240)
brushColor(250,250,250)
penSize(1)
penColor(100, 100, 200)
for i in range(2):
	for i in range (3):
		circle(x,y, 25)
		x+=15
	y+=12
	x+=-20
	for i in range(2):
		circle(x,y,20)
		x-=15
	x=300
	y=50
x=200
y=130
for i in range (3):
	circle(x,y, 15)
	x+=15
y+=12
x+=-20
for i in range(2):
	circle(x,y,10)
	x-=15
penSize(1)  
def woman(x0, y0, color):
	penColor('black')
	if color==1 :
		brushColor(150, 50, 50)
	elif color==2 :
		brushColor(250, 50, 50)
	else :
		brushColor(250, 50, 150)
	polygon([(x0, y0), (x0+20, y0+60), (x0-20, y0+60)])
	brushColor(220, 220, 200)
	circle(x0, y0, 15)
	polyline([(x0-7, y0+60), (x0-7, y0+75), (x0-14, y0+75)])
	polyline([(x0+7, y0+60), (x0+7, y0+75), (x0+14, y0+75)])
	polyline([(x0-10, y0+25), (x0-15, y0+15), (x0-18, y0+5)])
	polyline([(x0+10, y0+25), (x0+15, y0+15), (x0+18, y0+5)])

woman(420, 310, 1)
woman(320, 320, 2)
woman(200, 310, 3)
woman(80, 320, 1)

run()
