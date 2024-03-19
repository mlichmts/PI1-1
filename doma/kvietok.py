import turtle
import random


t=turtle
t.speed(0)
def patik(dlzka):
    t.fillcolor("green")
    t.begin_fill()
    t.rt(90)
    t.fd(dlzka+200)
    t.fd(-dlzka-50)
    t.lt(90)
    lupen1(dlzka)
    t.lt(180)
    lupen1(dlzka)
    t.end_fill()


def polkruh(dlzka):
    for i in range(9):
        t.fd(dlzka)
        t.lt(10)


def lupen1(dlzka):
    polkruh(dlzka)
    t.lt(90)
    polkruh(dlzka)
    t.lt(90)
def lupen(dlzka):
    t.fillcolor(f'#{random.randrange(256 ** 3):06x}')
    t.begin_fill()
    polkruh(dlzka)
    t.lt(90)
    polkruh(dlzka)
    t.lt(90)
    t.end_fill()

def kvet(dlzka,n):
    t.pendown()
    patik(dlzka)
    t.rt(90)
    t.fd(150)
    for i in range (n):
        lupen(dlzka)
        t.rt(360/n)
    t.rt(90)
    t.penup()


for i in range(4):
    kvet(10,10)
    x = random.randrange(-300,300)
    y = random.randrange(-300, 300)
    t.setpos(x,y)

t.mainloop()

