from tkinter import *
from random import randrange as rnd, choice
import time

root = Tk() 															#окно
root.geometry('800x600')

canv = Canvas(root,bg='white')
canv.pack(fill=BOTH,expand=1)

colors = ['red','orange','yellow','green','blue']
R=0
N=[0, 0, 0, 0]
K=[0, 0, 0, 0]
vx=[0, 0, 0, 0]
vy=[0, 0, 0, 0]
color=[0, 0, 0, 0]
x=[0, 0, 0, 0]
y=[0, 0, 0, 0]
r=[0, 0, 0, 0]

print("Идет счет очков: ")

def new_ball():															#рандомно рисуем круги по циклу
	global x,y,r, vx, vy, color
	canv.delete(ALL)
	for i in range(0,3,1):
		if K[i]==N[i]:
			x[i] = rnd(100,700)
			y[i] = rnd(100,500)
			r[i] = rnd(30,50)
			vx[i]=rnd(5, 10)
			vy[i]=rnd(5, 10)
			K[i]+=1
			color[i]=choice(colors)
			canv.create_oval(x[i]-r[i],y[i]-r[i],x[i]+r[i],y[i]+r[i],fill = color[i], width=0)
		else:																									#проверка на удар о стенку
			canv.create_oval(x[i]-r[i],y[i]-r[i],x[i]+r[i],y[i]+r[i],fill = color[i], width=0)
			x[i]+=vx[i]
			y[i]+=vy[i]
			hight1=abs(y[i]+r[i]*vy[i]/(vx[i]**2+vy[i]**2)**0.5-600)
			hight2=abs(y[i]+r[i]*vy[i]/(vx[i]**2+vy[i]**2)**0.5)
			width1=abs(x[i]+r[i]*vx[i]/(vx[i]**2+vy[i]**2)**0.5-800)
			width2=abs(x[i]+r[i]*vx[i]/(vx[i]**2+vy[i]**2)**0.5)
			if hight1<=10 or hight2<=10:
				vy[i]=-vy[i]
			elif width1<=10 or width2<=10:
				vx[i]=-vx[i]
	
	for i in range(3,4,1):
		if K[i]==N[i]:
			x[i] = rnd(100,700)
			y[i] = rnd(100,500)
			r[i] = rnd(30,50)
			vx[i]=rnd(5, 10)
			vy[i]=rnd(5, 10)
			K[i]+=1
			color[i]=choice(colors)
			canv.create_oval(x[i]-r[i]-20,y[i]-r[i],x[i]+r[i]+20,y[i]+r[i],fill = color[i], width=0)
		else:																									#проверка на удар о стенку
			canv.create_oval(x[i]-r[i]-20,y[i]-r[i],x[i]+r[i]+20,y[i]+r[i],fill = color[i], width=0)
			x[i]+=vx[i]
			y[i]+=vy[i]
			hight1=abs(y[i]+r[i]*vy[i]/(vx[i]**2+vy[i]**2)**0.5-600)
			hight2=abs(y[i]+r[i]*vy[i]/(vx[i]**2+vy[i]**2)**0.5)
			width1=abs(x[i]+r[i]*vx[i]/(vx[i]**2+vy[i]**2)**0.5-800)
			width2=abs(x[i]+r[i]*vx[i]/(vx[i]**2+vy[i]**2)**0.5)
			if hight1<=10 or hight2<=10:
				vy[i]=-vy[i]
			elif width1<=10 or width2<=10:
				vx[i]=-vx[i]
	root.after(30,new_ball)
    
def click(event):
	global R															#добавление очков за попадание
	x1=[0, 0, 0, 0]
	y1=[0, 0, 0, 0]
	for i in range(0,4,1):
		x1[i]=x[i]-event.x
		y1[i]=y[i]-event.y
		l=(x1[i]**2+y1[i]**2)**0.5
		if l<=r[i] :
			N[i]+=1
			if i==3 :
				R+=2
			else :
				R+=1
			print(R)
    

new_ball()

canv.bind('<Button-1>', click)											#нажатие

mainloop()
