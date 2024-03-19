import turtle
import random

t = turtle
t.speed(0)

def kosostvorec(velkost,farba):
    t.fillcolor(farba)
    t.begin_fill()
    for i in range(2):
            t.fd(velkost)
            t.left(45)
            t.fd(velkost)
            t.lt(135)
    t.end_fill()
def kvet():
    for i in range(8):
        kosostvorec(50,("tan","tomato")[i%2])
        t.lt(45)

for j in range(5):
    kvet()
    t.pu()
    x = random.randrange(-400,300)
    y = random.randrange(-400, 300)
    t.setpos(x,y)
    t.pd()


t.mainloop()

