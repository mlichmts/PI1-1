import turtle
import random

t = turtle


def terc(pocet,farba1,farba2):
    for i in reversed(range(1,pocet+1)):
        t.dot(i*15,farba1)
        farba1,farba2=farba2,farba1

terc(20,"blue","yellow")




t.mainloop()