from tkinter import *
from random import randrange as rnd, choice
import time

root = Tk() # окно
root.geometry('800x600')
canv = Canvas(root,bg='white')
canv.pack(fill=BOTH,expand=1)

colors = ['red','orange','yellow','green','blue'] # цвета для шаров
rating=0	# Начальный рейтинг в игре
time=10 # промежуток между запусками в (мс)
alltime=0 # общее время игры в (с)
print("Идет счет очков: ")
class Ball:
	def __init__(self):
		self.rand()	
	def rand(self):
		self.vx=rnd(-5, 5)
		self.vy=rnd(-5, 5)
		self.color=choice(colors)
		self.x = rnd(100,700)
		self.y = rnd(100,500)
		self.r = rnd(15,35)
		self.ball=canv.create_oval(
					self.x-self.r, 
					self.y-self.r, 
					self.x+self.r,
					self.y+self.r, 
					fill = self.color, width=0
					)
	def gooball(self):
		canv.move(self.ball, self.vx, self.vy)
		self.x+=self.vx
		self.y+=self.vy
		hight_down=abs(self.y-600)	# расстрояние до нижней стенки
		hight_up=abs(self.y)		# до верхней
		width_right=abs(self.x-800) # до правой
		width_left=abs(self.x)		# до левой
		delta=10	# погрешность оценки столкновения со стенкой
		if hight_down<=delta or hight_up<=delta:																		
			self.vy=-self.vy	# смена вертикал.скорости
		if width_right<=delta or width_left<=delta:
			self.vx=-self.vx	# смена гиризонт.скорости
	
balls = [Ball() for i in range(20)]	# class Ball для каждого шарика

def new_ball():	
	global alltime																											
	for ball in balls:	# обращение к шарикам в balls																					
		ball.gooball()	# движение шарика ball
	alltime+=time/1000	# счет времени (с)
	root.after(time, new_ball) 
def click(event):		# проверка на нажатие
	global rating
	for ball in balls:	# проходим по шарикам в balls
		x1 = ball.x-event.x
		y1 = ball.y-event.y
		l=(x1**2+y1**2)**0.5 # расстояние от центра шарика до клика
		if l<=ball.r :	# попали в шарик?!
			rating+=1
			canv.delete(ball.ball)	# удаляем шарик
			ball.rand()	# создаем шарик
			print(str(rating)+"   Время: "+ str(int(alltime))+" c")
new_ball()
canv.bind('<Button-1>', click)
mainloop()
