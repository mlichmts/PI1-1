import tkinter
import random

zoznam = []

def klik(event):
    zoznam.append((event.x, event.y))
    if len(zoznam) == 2:
        fill = f'#{random.randrange(256**3):06x}'
        canvas.create_rectangle(zoznam, fill=fill)
        zoznam.clear()

canvas = tkinter.Canvas()
canvas.pack()

canvas.bind('<ButtonPress-1>', klik)

tkinter.mainloop()