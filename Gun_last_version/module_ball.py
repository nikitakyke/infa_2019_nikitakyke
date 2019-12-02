from random import randrange as rnd, choice
import tkinter as tk
import math
import time
"""Количество выпущенных снарядов
создание массива шариков"""
bullet = 0 
balls = []
class ball():
    def __init__(self, x=40, y=450):
        """ Конструктор класса ball
        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        vx, vy - скорости
        k - коэффициент затухания скоростей (k<1)
        Радиусы шаров r равны 10
        """
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.k = 0.97
        self.color = choice(['purple', 'blue', 'brown', 'yellow'])
        self.id = canv.create_oval(
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r,
                fill=self.color
        )
        """Время жизни шарика"""
        self.live = 70 

    def set_coords(self):
        """Параметры рисования шарика"""
        canv.coords(
                self.id,
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r
        )
    def move(self):
        """Перемещение мяча за единицу времени
        Перемещение шарика с учетом гравитации (g=1),
        столкновения со стенками (экран 800*600), затуханием (k).
        Для целей k=0.99<1, шариков k=0.97<1 (оптимально)"""
        """поиск расстояния до стен"""
        distance_left = self.x - self.r
        distance_right = 800 - self.x - self.r
        distance_down = 600 - self.y - self.r
        distance_up = self.y - self.r
        if (distance_left < 0):
            self.vx = - self.vx
            self.x = self.r
        if (distance_right < 0):
            self.vx = - self.vx
            self.x = 800 - self.r
        if (distance_up < 0):
            self.vy = - self.vy
            self.y = self.r
        if (distance_down < 0):
            self.vy = - self.vy
            self.y = 600 - self.r
        self.x += self.vx
        self.y -= self.vy
        """ускорение"""
        self.g=1	
        self.vy -= self.g
        """Затухание после удара"""
        self.vy = self.k*self.vy
        self.vx = self.k*self.vx
        self.set_coords()
    def hit(self):
        """Попадание шарика в цель. 
        Цель превращаем в неподвижную точку с координатами 
        x = -50 , y = -50"""
        canv.coords(self.id, 0, 0, 0, 0)
        self.r = 0
        self.vx = 0 
        self.vy = 0
        self.x = -50
        self.y = -50
    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.
        Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        Цели существуют, если r!=0"""
        distance_x = self.x - obj.x
        distance_y = self.y - obj.y
        distance = (distance_x**2 + distance_y**2)**0.5
        if distance<obj.r :
            return True
        else :
            return False

class target(ball):
    """Наследование классов - некоторых общих функций 
    move, set_coords, hit. """
    def __init__ (self):
        """начальные значения жизни целей, результата, 
        выводимого на экран"""
        self.points = 0
        self.live = 1
        self.id = canv.create_oval(0,0,0,0)
        self.new_target()
        self.id_points = canv.create_text(70,30,text = "Результат: "+str(self.points),font = '28')
    def new_target(self):
        """ Инициализация новой цели.
        Рандомные скорости и координаты, 
        k - коэффициент затухания скорости цели"""
        x = self.x = rnd(200, 780)
        y = self.y = rnd(200, 550)
        r = self.r = rnd(20, 50)
        self.k = 0.99
        self.vx = rnd(10, 30)
        self.vy = rnd(10, 30)
        color = self.color = 'red'
        canv.coords(self.id, x-r, y-r, x+r, y+r)
        canv.itemconfig(self.id, fill=color)
    def result(self, points=1):
        """обновление результата на экране"""
        canv.itemconfig(self.id_points, text=" ")
        self.points += points
        self.id_points = canv.create_text(70,30,text = "Результат: "+str(self.points),font = '28')
    def deleteresult(self):
        """удаление результата на экране"""
        canv.itemconfig(self.id_points, text=" ")
class gun():
    def __init__ (self):
        """параметры ружья: заряжается ли, размер."""
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.id = canv.create_line(20,450,50,420,width=7)

    def fire2_start(self, event):
        """старт зарядки ружья, значение не нуль"""
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.
        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши."""
        global balls, bullet
        bullet += 1
        new_ball = ball()
        self.an = math.atan((event.y-new_ball.y) / (event.x-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls += [new_ball]
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event=0):
        """Прицеливание. Зависит от положения мыши."""
        if event and event.x!=20:
            self.an = math.atan((event.y-450) / (event.x-20))
        if self.f2_on:
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')
        canv.coords(self.id, 20, 450,
                    20 + max(self.f2_power, 10) * math.cos(self.an),
                    450 + max(self.f2_power, 10) * math.sin(self.an)
                    )

    def power_up(self):
        """увеличение размеров ружья и изменение его цвета"""
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')
