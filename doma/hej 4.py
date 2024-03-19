import turtle
import random

t=turtle
t.pu()

def stvorec(dlzka):
    t.fillcolor(f'#{random.randrange(256 ** 3):06x}')
    t.begin_fill()
    for i in range(4):
        t.fd(dlzka)
        t.rt(90)
    t.end_fill()

def stvorce(dlzka,krok):
    while dlzka>0:
        stvorec(dlzka)
        dlzka -= krok
        t.fd(krok/2)
        t.lt(90)
        t.fd(dlzka)
        t.rt(90)






stvorce(100,25)
t.mainloop()


