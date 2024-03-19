import turtle
import tkinter
import random
t = turtle
def slnko(pocet, velkost):
    t.pensize(10)
    t.pencolor("gold")
    for i in range(pocet):
        t.fd(velkost)
        t.fd(-velkost)
        t.right(360/pocet)
    t.dot(velkost,"gold")



slnko(10,100)

t.mainloop()

