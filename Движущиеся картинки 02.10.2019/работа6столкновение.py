from graph import*
x=30
y=300
dx=2
dt=50
stolknovenie=0
x1=0
y1=300
dx1=2
dy1=2
x2=0
y2=300
dx2=1
dy2=-2
def went_one():
	global x, stolknovenie, y1, y2, x1, x2
	brushColor('yellow')
	rectangle(0,0,500,600)
	if stolknovenie==0:
		brushColor('red')
		penColor('black')
		penSize(1)
		circle(200, y, 20)
		circle(x, y, 10)
		x+=dx
	else:
		brushColor('red')
		penColor('black')
		penSize(3)
		circle(x1, y1, 20)
		circle(x2, y2, 10)
		x1+=dx1
		y1+=dy1
		x2+=dx2
		y2+=dy2
	if x>=176 and stolknovenie==0 :
		stolknovenie=1
		x1=x+10
		x2=x+10	
		
onTimer(went_one, dt)

run()
