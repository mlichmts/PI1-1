import tkinter
import turtle
import random

t=turtle
t.delay(0)
t.speed(0)
t.pu()
def stvorec(dlzka):
    t.fillcolor(f'#{random.randrange(256 ** 3):06x}')
    t.begin_fill()
    for i in range(4):
        t.fd(dlzka)
        t.lt(90)
    t.end_fill()

def stvorce(dlzka,krok):
    while dlzka>0:
        stvorec(dlzka)
        t.lt(90)
        t.fd(dlzka)
        t.rt(90)
        t.fd(krok/2)
        dlzka=dlzka-krok

stvorce(120,30)






t.mainloop()

