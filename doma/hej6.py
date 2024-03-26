import turtle
import tkinter
import random

canvas = tkinter.Canvas()
canvas.pack()
r=1
global farba
farba = "yellow"
def kruhy(event):
    global r
    x,y=event.x,event.y
    canvas.create_oval(x+r,y+r,x-r,y-r,fill=farba)
    r+=.1
def zmaz():
    canvas.delete("all")
    global r
    r=1

def zmen_farbu():
    global r
    r=1
    global farba
    farba = (f'#{random.randrange(256 ** 3):06x}')



canvas.bind("<B1-Motion>",kruhy)
tkinter.Button(text="Zmaž",command=zmaz).pack()
tkinter.Button(text="zmen farbu",command=zmen_farbu).pack()

canvas.mainloop()
