from random import randrange as rnd, choice
import tkinter as tk
from tkinter import mainloop
import math
import time
import module_ball

root = tk.Tk()
fr = tk.Frame(root)
root.geometry('800x600')
canv = tk.Canvas(root, bg='green')
canv.pack(fill=tk.BOTH, expand=1)
module_ball.canv = canv

"""t1 и t2 для удобного обращения к целям"""           
t1 = module_ball.target()
t2 = module_ball.target()
"""параметры надписи"""
screen1 = canv.create_text(400, 300, text='', font='28')
g1 = module_ball.gun()

def new_game(event=''):
    """создание целей t1 и t2, 
    удаление результата цели t2,
    чтобы результаты не накладывались друг на друга"""
    global gun, t1, t2, screen1
    t1.new_target() 
    t2.new_target()
    t2.deleteresult()
    
    canv.bind('<Button-1>', g1.fire2_start)
    canv.bind('<ButtonRelease-1>', g1.fire2_end)
    canv.bind('<Motion>', g1.targetting)
    
    """время жизни целей: 
    1 - живет, 0 - не живет"""
    t1.live = 1
    t2.live = 1
    while t1.live or t2.live:
        """Если хотя бы одна цель жива - она передвигается, 
        также передвигается каждый живой шарик. 
        Если они сталкиваются - цель удаляется.""" 
        if t1.live!=0:
            t1.move()
        if t2.live!=0:
            t2.move()
        for b in module_ball.balls:
            b.move()
            if b.hittest(t1) and t1.live!=0:
                """убираю цель №1"""
                t1.live = 0
                t1.hit()   
            if b.hittest(t2) and t2.live!=0:
                """убираю цель №2"""
                t2.live = 0
                t2.hit()
            """уменьшение времени жизни шарика с live = 70"""
            b.live-=1 
            if b.live<=0:
                """удаление шарика, если его время жизни истекло"""
                b.hit() 
        if t1.live==0 and t2.live==0:
            """Если цели уничтожены, 
            происходит обновление результата и вывод его на экран"""
            t1.result()   
            canv.itemconfig(
                screen1, 
                text=
                'Вы уничтожили цель за ' + 
                    str(module_ball.bullet) + ' выстрелов'
                    )
            """обнуление количества испытаний"""
            module_ball.bullet = 0
            canv.update()
            """время для прочитывания надписи"""
            time.sleep(0.5) 
        canv.update()
        """оптимальное время между обновления"""
        time.sleep(0.03)
        g1.targetting()
        g1.power_up()
    for b in module_ball.balls:
        """Цикл для удаления оставшихся шариков"""
        b.hit()
    canv.itemconfig(screen1, text='')
    canv.update()
    root.after(25, new_game)
new_game()
mainloop()
