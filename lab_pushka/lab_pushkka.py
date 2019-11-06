from random import randrange as rnd, choice
import tkinter as tk
from tkinter import mainloop
import math
import time

root = tk.Tk()
fr = tk.Frame(root)
root.geometry('800x600')
canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)


class ball():
    def __init__(self, x=40, y=450):
        """ Конструктор класса ball
        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(['blue', 'green', 'red', 'brown'])
        self.id = canv.create_oval(
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r,
                fill=self.color
        )
        self.live = 70

    def set_coords(self):
        canv.coords(
                self.id,
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r
        )

    def move(self):
        """Переместить мяч по прошествии единицы времени
        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
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
        self.g=1
        self.vy -= self.g
        self.vy = 0.97*self.vy
        self.vx = 0.97*self.vx
        self.set_coords()
    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        distance_x = self.x - obj.x
        distance_y = self.y - obj.y
        distance = (distance_x**2 + distance_y**2)**0.5
        if distance < (obj.r) and self.r!=0 :
            return True
        else :
            return False
           
class gun():
    def __init__ (self):
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.id = canv.create_line(20,450,50,420,width=7)

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.
        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = ball()
        new_ball.r += 5
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
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')

class target():
    def __init__ (self):
        self.points = 0
        self.live = 1
        self.id = canv.create_oval(0,0,0,0)
        self.new_target()
        self.id_points = canv.create_text(70,30,text = "Результат: "+str(self.points),font = '28')
    def new_target(self):
        """ Инициализация новой цели. """
        x = self.x = rnd(200, 780)
        y = self.y = rnd(200, 550)
        r = self.r = rnd(20, 50)
        self.vx = rnd(10, 20)
        self.vy = rnd(10, 20)
        color = self.color = 'red'
        canv.coords(self.id, x-r, y-r, x+r, y+r)
        canv.itemconfig(self.id, fill=color)
       
    def set_coords(self):
        canv.coords(
                self.id,
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r
        )
    def move(self):
        delta=10
        distance_left = self.x
        distance_right = 800 - self.x
        distance_down = 600 - self.y
        distance_up = self.y
        if (distance_left < delta):
            self.vx = - self.vx
        if (distance_right < delta):
            self.vx = - self.vx
        if (distance_up < delta):
            self.vy = - self.vy
        if (distance_down < delta):
            self.vy = - self.vy
        self.x += self.vx
        self.y -= self.vy
        self.set_coords()

    def hit(self):
        """Попадание шарика в цель."""
        canv.coords(self.id, -10, -10, -10, -10)
    def result(self, points=1):
        canv.itemconfig(self.id_points, text=" ")
        self.points += points
        self.id_points = canv.create_text(70,30,text = "Результат: "+str(self.points),font = '28')
    def deleteresult(self):
        canv.itemconfig(self.id_points, text=" ")
t1 = target()
t2 = target()
screen1 = canv.create_text(400, 300, text='', font='28')
g1 = gun()
bullet = 0
balls = []

def new_game(event=''):
    global gun, t1, t2, screen1, balls, bullet
    t1.new_target() #создание целей
    t2.new_target()
    t2.deleteresult()  #стираю Результат
    bullet = 0
    balls = []
    canv.bind('<Button-1>', g1.fire2_start)
    canv.bind('<ButtonRelease-1>', g1.fire2_end)
    canv.bind('<Motion>', g1.targetting)
    
    z = 0.03
    t1.live = 1
    t2.live = 1
    while t1.live or t2.live:  #Живые цели
        if t1.live!=0:
            t1.move()
        if t2.live!=0:
            t2.move()
        for b in balls:
            b.move()
            if b.hittest(t1) and t1.live!=0:
                    t1.live = 0
                    t1.hit()   #убираю цель №1
            if b.hittest(t2) and t2.live!=0:
                    t2.live = 0
                    t2.hit()   #убираю цель №2
            b.live-=1
            if b.live<=0:
               canv.delete(b.id) 
               b.r=0      #убираю шарик
        if t1.live==0 and t2.live==0:
            t1.result()   #обновление Результата
            canv.itemconfig(
                screen1, 
                text=
                'Вы уничтожили цель за ' + str(bullet) + ' выстрелов'
                    )
            canv.update()
            time.sleep(1) 
        canv.update()
        time.sleep(0.03)
        g1.targetting()
        g1.power_up()
    for b in balls:
        canv.delete(b.id)
    canv.itemconfig(screen1, text='')
    canv.update()
    root.after(5, new_game)


new_game()

mainloop()
