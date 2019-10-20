from tkinter import *
from random import randrange as rnd, choice
import time

root = Tk() 															#окно
root.geometry('800x600')
canv = Canvas(root,bg='white')
canv.pack(fill=BOTH,expand=1)

colors = ['red','orange','yellow','green','blue']
R=0																		#количество очков в игре
class Ball:
	K = 0																#переменные - сколько раз нажали на шарики и сколько нарисовали
	N = 0
	def __init__(self):
		self.rand()
		self.N=0
		self.K=0
		
	def rand(self):
		self.vx=rnd(-10, 10)
		self.vy=rnd(-10, 10)
		self.color=choice(colors)
		self.x = rnd(100,700)
		self.y = rnd(100,500)
		self.r = rnd(30,50)
		self.x1=0
		self.y1=0
		canv.create_oval(self.x-self.r, self.y-self.r, self.x+self.r, self.y+self.r, fill = self.color, width=0)
		self.K+=1
		
	def gooball(self):
		canv.create_oval(self.x-self.r, self.y-self.r, self.x+self.r, self.y+self.r, fill = self.color, width=0)
		self.x+=self.vx
		self.y+=self.vy
		hight1=abs(self.y-600)											#расстрояния до стенок
		hight2=abs(self.y)
		width1=abs(self.x-800)
		width2=abs(self.x)
		delta=20														#погрешность оценки столкновения со стенкой
		if hight1<=delta or hight2<=delta:																		
			self.vy=-self.vy
		elif width1<=delta or width2<=delta:
			self.vx=-self.vx											#смена скорости после удара
	
print("Идет счет очков: ")

balls = [Ball() for i in range(10)]

def new_ball():															
	canv.delete(ALL)													
	for ball in balls:													#обращение к шарикам
		if ball.K==ball.N :												#если на шарик нажали - параметры K==N и рисуется новый шарик
			ball.rand()
		else:																						
			ball.gooball()												#движение шарика
	
	root.after(30,new_ball)
    
def click(event):
	global R
	for ball in balls:													#проверка- нажали на шарик?
		ball.x1 = ball.x-event.x
		ball.y1 = ball.y-event.y
		l=(ball.x1**2+ball.y1**2)**0.5
		if l<=ball.r :
			ball.N+=1
			R+=1
			print(R)
new_ball()

canv.bind('<Button-1>', click)											#нажатие

mainloop()
