from graph import*
x=30
y=300
dx=2
dt=50
raspad=0
x1=0
y1=300
dx1=2
dy1=2
x2=0
y2=300
dx2=1
dy2=-2
def went_one():
	global x, raspad, y1, y2, x1, x2
	brushColor('yellow')
	rectangle(0,0,500,600)
	if raspad==0:
		brushColor('red')
		penColor('black')
		penSize(1)
		circle(x, y, 10)
		x+=dx
	else:
		brushColor('black')
		penColor('green')
		penSize(2)
		circle(x1, y1, 10)
		circle(x2, y2, 10)
		x1+=dx1
		y1+=dy1
		x2+=dx2
		y2+=dy2
	if x>=200 and raspad==0 :
		raspad=1
		x1=x+10
		x2=x+10	
		
onTimer(went_one, dt)

run()
