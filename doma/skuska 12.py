import turtle
import random

t = turtle
t.rt(5)

def domcek(d):
    for i in range(4):
        t.fd(d)
        t.lt(90)
    t.lt(45)
    d2 = d * 2 ** 0.5
    t.fd(d2)
    for j in range(2):
        t.lt(90)
        t.fd(d2/2)
    t.lt(90)
    t.fd(d2)
    t.lt(45)


domcek(100)
domcek(80)
domcek(20)


t.mainloop()