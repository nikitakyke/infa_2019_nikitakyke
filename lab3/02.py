from graph import*
windowSize(500, 600)
brushColor(20, 200, 0)
rectangle(0, 300, 500, 600)
brushColor(100, 200, 200)
rectangle(0, 0, 500, 300)

def byket(x0, y0):
	brushColor('yellow')
	polygon([(x0, y0), (x0-60, y0-20), (x0-20, y0-60)])
	brushColor(150, 10, 10)
	circle(x0-50, y0-30, 17)
	brushColor(250, 0, 0)
	circle(x0-30, y0-50, 17)
	brushColor(250, 250, 250)
	circle(x0-50, y0-50, 17)
	
def love(x0, y0):
	brushColor(250, 0, 0)
	penSize(0)
	polygon([(x0, y0), (x0, y0-80), (x0+30, y0-70)])
	circle(x0+23, y0-70,10)
	circle(x0+8, y0-75,10)
	
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
	circle(x0, y0-(a+10), 30)
	
	penSize(2)
	line(x0-30, y0-70, x0-100, y0+10)
	line(x0+30, y0-70, x0+100, y0+10)
	polyline([(x0-10, y0+95), (x0-30, y0+160), (x0-50, y0+160)])
	polyline([(x0+10, y0+95), (x0+30, y0+160), (x0+50, y0+160)])
	penSize(1)
	byket(x0-100, y0+10)
	
def woman(x0, y0):
	brushColor(150, 10, 100)
	polygon([(x0, y0), (x0+50, y0+200), (x0-50, y0+200)])
	penSize(0)
	brushColor(180,180,180)
	circle(x0, y0, 30)
	penSize(2)
	line(x0-10, y0+40, 300, 310)
	polyline([(x0-20, y0+200), (x0-20, y0+265), (x0-40, y0+265)])
	polyline([(x0+20, y0+200), (x0+20, y0+265), (x0+40, y0+265)])
	
	polyline([(x0+10, y0+40), (x0+50, y0+70), (x0+80, y0+40), (x0+70, y0+60), (x0+100, y0-20)])
	
	love(x0+100, y0-20)
	
	
woman(350, 200)
ellipse(200, 300, 100, 50)
run()
