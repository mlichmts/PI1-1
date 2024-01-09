import tkinter
import random

canvas = tkinter.Canvas()
canvas.pack()

n = 7
for i in range(n):
    x = random.randint(10, 370)
    y = random.randint(10, 240)
    canvas.create_oval(x - 3, y - 3, x + 3, y + 3, fill='red')
    if i == 0:
        x1 = x2 = x
        y1 = y2 = y
    else:
        if x < x1:
            x1 = x
        if x > x2:
            x2 = x
        if y < y1:
            y1 = y
        if y > y2:
            y2 = y
canvas.create_rectangle(x1, y1, x2, y2, outline='blue')

tkinter.mainloop()