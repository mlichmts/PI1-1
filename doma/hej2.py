import turtle
import random

t=turtle

t.speed(0)

def polkruznica(velkost,smer):
    if smer:
        uhol = 10
    else:
        uhol = -10
    t.fillcolor(random.choice(("red","green","blue")))
    t.begin_fill()
    for i in range(18):
        t.fd(velkost)
        t.lt(uhol)
    t.end_fill()
t.lt(90)
for i in range(10):
    polkruznica(3,i%2)
for i in range(10):
    polkruznica(3,i%2 == 0)


t.mainloop()