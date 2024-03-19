import turtle
import random

t=turtle

t.speed(0)
def bodky(n,m):
    for j in range(n):
        for i in range(m):
            t.penup()
            a=random.randrange(20,35)
            t.dot(a,"salmon")
            t.fd(30)
        t.fd(-m*30)
        t.rt(90)
        t.fd(30)
        t.lt(90)


bodky(10,15)


t.mainloop()