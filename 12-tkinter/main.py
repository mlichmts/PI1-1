import tkinter
import random

canvas = tkinter.Canvas(width=600, height=500)
canvas.pack()
x = 3
y = 0
d = 100
xx = 3
pocet = 598//d  #dve // je celociselne delenie 7//3=2
vyska = 498//d
for j in range(vyska):
    for i in range(pocet):
        farba = random.choice(("green", "red", "orange", "purple", "blue","magenta"))
        canvas.create_rectangle(x, y, x+d, y+d, fill=farba)
        canvas.create_line(x, y, x+d, y+d)
        canvas.create_line(x, y+d, x+d, y)
        x =x+d
    x = xx
    y = y + d





canvas.mainloop()