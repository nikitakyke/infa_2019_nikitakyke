from graph import*
#time=0
dt=50
x=0
y=0
dx=10
dy=10
def went():
	global x, y
	brushColor('yellow')
	rectangle(0,0,500,500)
	brushColor('black')
	circle(x, y, 10)
	x+=dx
	y+=dy
onTimer(went, dt)

run()
