from graph import*
#time=0
dt=50
x=50
y=50
dx=1
dy=0
t=300
parametr=0
def wentvniz():
	global x, y, dx, dy, t, parametr
	brushColor('yellow')
	rectangle(0,0,500,600)
	brushColor('red')
	penColor('black')
	penSize(1)
	circle(x, y, 10)
	penSize(10)
	line(0, 37, 500, 37)
	line(0, 520, 500, 520)
	if parametr==0:
		x+=dx
		t+=dt
		y+=dy
		dy+=t*dt/300000
	else:
		x+=dx
		t-=dt
		y-=dy
		dy-=t*dt/300000
	if y>=495:
		parametr=1
	if y<=50:
		parametr=0
	
		
		
onTimer(wentvniz, dt)

run()
