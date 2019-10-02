from graph import*
import random
x=random.randint(50, 300)
y=random.randint(50, 400)
dx=random.randint(0, 8)-1
dy=random.randint(0, 4)-2
dt=50
parametr=1
raspad=0
x1=0
y1=y
dx1=random.randint(0, 4)-2
dy1=random.randint(0, 2)-1
x2=0
y2=y
dx2=random.randint(0, 4)-2
dy2=random.randint(0, 2)-1
cwet_one=randColor()
cwet_two=randColor()
cwet_three=randColor()
def went_one():
	global x, y, raspad, y1, y2, x1, x2, parametr, cwet_one, cwet_two, cwet_three
	brushColor('yellow')
	rectangle(0,0,500,600)
	if raspad<20:
		brushColor(cwet_one)
		penColor('black')
		penSize(1)
		circle(x, y, 10)
		x+=dx
		y+=dy
		raspad+=1
	else:
		brushColor(cwet_two)
		penColor('green')
		penSize(2)
		circle(x1, y1, 10)
		brushColor(cwet_three)
		circle(x2, y2, 10)
		x1+=dx1
		y1+=dy1
		x2+=dx2
		y2+=dy2
	if raspad>=20 and parametr==1 :
		x1=x+3
		x2=x+3
		y1=y+3
		y2=y+3
		raspad+=2
		parametr=0
onTimer(went_one, dt)

run()
