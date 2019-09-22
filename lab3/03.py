from graph import*
windowSize(500, 600)
brushColor(20, 200, 0)
rectangle(0, 300, 500, 600)
brushColor(100, 200, 200)
rectangle(0, 0, 500, 300)

def ellipse(x0, y0, a, b):
	x=x0-b
	y=y0
	N=100
	dx=2*b/N
	penSize(0)
	brushColor(130, 130, 130)
	while (x<x0+b) :
		rectangle(x, y, x+dx, 2*y0-y)
		x=x+dx
		y=y0+a*(1-(x-x0)**2/b**2)**0.5
		
	brushColor(180,180,180)
	circle(x0, y0-(a+10), 20)
	
	penSize(2)
	line(x0-15, y0-35, x0-50, y0+20)
	line(x0+15, y0-35, x0+50, y0+20)
	polyline([(x0-10, y0+45), (x0-20, y0+80), (x0-30, y0+80)])
	polyline([(x0+10, y0+45), (x0+20, y0+80), (x0+30, y0+80)])
	penSize(1)
	#byket(x0-100, y0+10)
	
def woman(x0, y0):
	brushColor(150, 10, 100)
	polygon([(x0, y0), (x0+25, y0+100), (x0-25, y0+100)])
	penSize(0)
	brushColor(180,180,180)
	circle(x0, y0, 15)
	penSize(1)
	polyline([(x0-10, y0+100), (x0-10, y0+130), (x0-20, y0+130)])
	polyline([(x0+10, y0+100), (x0+10, y0+130), (x0+20, y0+130)])
	
def love(x0, y0):
	line(x0, y0, x0-2, y0-30)
	x0-=2;y0-=30
	brushColor(250, 0, 0)
	penSize(0)
	polygon([(x0, y0), (x0, y0-80), (x0-30, y0-70)])
	circle(x0-23, y0-70,10)
	circle(x0-8, y0-75,10)
	
def byket1(x0, y0):
	brushColor('yellow')
	polygon([(x0, y0), (x0+30, y0-10), (x0+10, y0-30)])
	brushColor(150, 10, 10)
	circle(x0+25, y0-15, 7.5)
	brushColor(250, 0, 0)
	circle(x0+15, y0-25, 7.5)
	brushColor(250, 250, 250)
	circle(x0+25, y0-25, 7.5)
def byket2(x0, y0):
	brushColor('yellow')
	polygon([(x0, y0), (x0+20, y0-30), (x0-20, y0-30)])
	brushColor(150, 10, 10)
	circle(x0-10, y0-35, 12)
	brushColor(250, 0, 0)
	circle(x0+10, y0-35, 12)
	brushColor(250, 250, 250)
	circle(x0, y0-45, 12)
	
ellipse (100, 300, 50, 25)
love(50,320)
woman(190, 250)
line(185, 270, 150, 320)
woman(300, 250)
ellipse(390, 300, 50, 25)
line(305, 270, 340, 320)
byket1(440, 320)

polyline([(195, 270),(220, 260), (245, 240), (270, 260), (295, 270)])
line(245, 240, 260, 140)
byket2(260, 140)

run()
