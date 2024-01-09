import tkinter
import random

canvas = tkinter.Canvas(width=400, height=300)
canvas.pack()

for i in range(10000):
    x = random.randrange(400)
    y = random.randrange(300)
    if x >=y and 300 - x <= y:
        farba = 'blue'
    elif x>0 and y>150:
        farba = "red"
    else:
        farba = ""

    canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill=farba, width=0)

tkinter.mainloop()