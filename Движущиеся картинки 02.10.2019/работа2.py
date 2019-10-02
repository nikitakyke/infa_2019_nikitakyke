from graph import*
#time=0
dt=30
x=50
y=50
dx=0
dy=0
t=300
def went():
	global x, y, dx, dy, t
	brushColor('yellow')
	rectangle(0,0,500,600)
	brushColor('black')
	circle(x, y, 10)
	x+=dx
	y+=dy
	t+=dt
	dx+=10*t/100000
	dy+=t*dt/100000
onTimer(went, dt)

run()
