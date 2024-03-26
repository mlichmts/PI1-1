import tkinter
import random

zoznam = []

def klik(event):
    xy = event.x, event.y
    zoznam.append(xy)
    canvas.create_text(xy, text='+')
    if len(zoznam) == 3:
        fill = f'#{random.randrange(256**3):06x}'
        canvas.create_polygon(zoznam, fill=fill)
        zoznam.pop(0)

canvas = tkinter.Canvas()
canvas.pack()

canvas.bind('<ButtonPress-1>', klik)

tkinter.mainloop()