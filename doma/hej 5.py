import turtle
import random

t=turtle
t.speed(0)


def troj(rameno,uhol):
    a= int(360/uhol)
    for i in range(a):
        t.fillcolor(f'#{random.randrange(256 ** 3):06x}')
        t.begin_fill()
        t.fd(rameno)
        t.lt(90+uhol/2)
        t.fd(360/uhol)
        t.lt(90+uhol/2)
        t.fd(rameno)
        t.rt(180)
        t.end_fill()




troj(300,20)
t.mainloop()