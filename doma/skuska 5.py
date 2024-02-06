import random
import tkinter


canvas = tkinter.Canvas(width=300,height=300)
canvas.pack()


def sucet(cislo):
    (cislo + 50)

sucet = 0
n = 10
x = 20
y = 20
x1 = 70
y1 = 40
x2 = 45
y2 = 30
for i in range(n):
    hodnota = random.choice((1, 2, 5, 10, 20, 50))
    canvas.create_rectangle(x, y,x1 , y1, fill="light blue")
    canvas.create_text(x + 25,y+10,text=str(hodnota) + " €",font=16)
    y = y+25
    y1 = y1+25
    sucet = sucet+hodnota

canvas.create_text(100,50,text=str(sucet) + " €",font=16)

canvas.mainloop()

