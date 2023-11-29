import tkinter

canvas = tkinter.Canvas(height=600,width=500)
canvas.pack()
x = 3
y = 3
d = 6
sirkanapisu=d*40
vyskanaoisu=d*8
xx=3
pocet = 498//sirkanapisu  #dve // je celociselne delenie 7//3=2
vyska = 598//vyskanaoisu

for j in range(vyska):
    for i in range (pocet):
        f = "red"
        canvas.create_rectangle(x, y, x+d, y+d, fill=f)
        canvas.create_rectangle(x, y+d, x+d, y+2*d, fill=f)
        canvas.create_rectangle(x, y+2*d, x+d, y+3*d, fill=f)
        canvas.create_rectangle(x, y+3*d, x+d, y+4*d, fill=f)
        canvas.create_rectangle(x, y+4*d, x+d, y+5*d, fill=f)
        canvas.create_rectangle(x, y+5*d, x+d, y+6*d, fill=f)
        canvas.create_rectangle(x, y+6*d, x+d, y+7*d, fill=f)
        canvas.create_rectangle(x+d, y+d, x+2*d, y+2*d, fill=f)
        canvas.create_rectangle(x+2*d, y+2*d, x+3*d, y+3*d, fill=f)
        canvas.create_rectangle(x+2*d, y+3*d, x+3*d, y+4*d, fill=f)
        canvas.create_rectangle(x+3*d, y+d, x+4*d, y+2*d, fill=f)
        canvas.create_rectangle(x+4*d, y, x+5*d, y+d, fill=f)
        canvas.create_rectangle(x+4*d, y+d, x+5*d, y+2*d, fill=f)
        canvas.create_rectangle(x+4*d, y+2*d, x+5*d, y+3*d, fill=f)
        canvas.create_rectangle(x+4*d, y+3*d, x+5*d, y+4*d, fill=f)
        canvas.create_rectangle(x+4*d, y+4*d, x+5*d, y+5*d, fill=f)
        canvas.create_rectangle(x+4*d, y+5*d, x+5*d, y+6*d, fill=f)
        canvas.create_rectangle(x+4*d, y+6*d, x+5*d, y+7*d, fill=f)
        #písmeno M
        x = 8*d+x
        f = "blue"
        canvas.create_rectangle(x, y+6*d, x+d, y+7*d, fill=f)
        canvas.create_rectangle(x, y+5*d, x+d, y+6*d, fill=f)
        canvas.create_rectangle(x, y+4*d, x+d, y+5*d, fill=f)
        canvas.create_rectangle(x, y+3*d, x+d, y+4*d, fill=f)
        canvas.create_rectangle(x, y+2*d, x+d, y+3*d, fill=f)
        canvas.create_rectangle(x, y+d, x+d, y+2*d, fill=f)
        canvas.create_rectangle(x+d, y, x+2*d, y+d, fill=f)
        canvas.create_rectangle(x+2*d, y, x+3*d, y+d, fill=f)
        canvas.create_rectangle(x+3*d, y, x+4*d, y+d, fill=f)
        canvas.create_rectangle(x+4*d, y+d, x+5*d, y+2*d, fill=f)
        canvas.create_rectangle(x+4*d, y+2*d, x+5*d, y+3*d, fill=f)
        canvas.create_rectangle(x+4*d, y+3*d, x+5*d, y+4*d, fill=f)
        canvas.create_rectangle(x+4*d, y+4*d, x+5*d, y+5*d, fill=f)
        canvas.create_rectangle(x+4*d, y+5*d, x+5*d, y+6*d, fill=f)
        canvas.create_rectangle(x+4*d, y+6*d, x+5*d, y+7*d, fill=f)
        canvas.create_rectangle(x+2*d, y+3*d, x+3*d, y+4*d, fill=f)
        canvas.create_rectangle(x+d, y+3*d, x+2*d, y+4*d, fill=f)
        canvas.create_rectangle(x+3*d, y+3*d, x+4*d, y+4*d, fill=f)
        #písmeno A
        x = 8*d+x
        f = "yellow"
        canvas.create_rectangle(x, y, x+d, y+d, fill=f)
        canvas.create_rectangle(x+d, y, x+2*d, y+d, fill=f)
        canvas.create_rectangle(x+2*d, y, x+3*d, y+d, fill=f)
        canvas.create_rectangle(x+3*d, y, x+4*d, y+d, fill=f)
        canvas.create_rectangle(x+4*d, y, x+5*d, y+d, fill=f)
        canvas.create_rectangle(x+2*d, y+d, x+3*d, y+2*d, fill=f)
        canvas.create_rectangle(x+2*d, y+2*d, x+3*d, y+3*d, fill=f)
        canvas.create_rectangle(x+2*d, y+3*d, x+3*d, y+4*d, fill=f)
        canvas.create_rectangle(x+2*d, y+4*d, x+3*d, y+5*d, fill=f)
        canvas.create_rectangle(x+2*d, y+5*d, x+3*d, y+6*d, fill=f)
        canvas.create_rectangle(x+2*d, y+6*d, x+3*d, y+7*d, fill=f)
        #písmeno T
        x = 8*d+x
        f = "pink"
        canvas.create_rectangle(x, y, x+d, y+d, fill=f)
        canvas.create_rectangle(x, y+d, x+d, y+2*d, fill=f)
        canvas.create_rectangle(x, y+2*d, x+d, y+3*d, fill=f)
        canvas.create_rectangle(x, y+3*d, x+d, y+4*d, fill=f)
        canvas.create_rectangle(x, y+4*d, x+d, y+5*d, fill=f)
        canvas.create_rectangle(x, y+5*d, x+d, y+6*d, fill=f)
        canvas.create_rectangle(x+d, y+6*d, x+2*d, y+7*d, fill= f)
        canvas.create_rectangle(x+2*d, y+6*d, x+3*d, y+7*d, fill=f)
        canvas.create_rectangle(x+3*d, y+6*d, x+4*d, y+7*d, fill=f)
        canvas.create_rectangle(x+4*d, y+5*d, x+5*d, y+6*d, fill=f)
        canvas.create_rectangle(x+4*d, y+4*d, x+5*d, y+5*d, fill=f)
        canvas.create_rectangle(x+4*d, y+3*d, x+5*d, y+4*d, fill=f)
        canvas.create_rectangle(x+4*d, y+2*d, x+5*d, y+3*d, fill=f)
        canvas.create_rectangle(x+4*d, y+d, x+5*d, y+2*d, fill=f)
        canvas.create_rectangle(x+4*d, y, x+5*d, y+d, fill=f)
        #písmeno U
        x = 8*d+x
        f = "orange"
        canvas.create_rectangle(x+d, y, x+2*d, y+d, fill=f)
        canvas.create_rectangle(x+2*d, y, x+3*d, y+d, fill=f)
        canvas.create_rectangle(x+3*d, y, x+4*d, y+d, fill=f)
        canvas.create_rectangle(x+4*d, y, x+5*d, y+d, fill=f)
        canvas.create_rectangle(x, y+d, x+d, y+2*d, fill=f)
        canvas.create_rectangle(x, y+2*d, x+d, y+3*d, fill=f)
        canvas.create_rectangle(x+d, y+3*d, x+2*d, y+4*d, fill=f)
        canvas.create_rectangle(x+2*d, y+3*d, x+3*d, y+4*d, fill=f)
        canvas.create_rectangle(x+3*d, y+3*d, x+4*d, y+4*d, fill=f)
        canvas.create_rectangle(x+4*d, y+4*d, x+5*d, y+5*d, fill=f)
        canvas.create_rectangle(x+4*d, y+5*d, x+5*d, y+6*d, fill=f)
        canvas.create_rectangle(x+3*d, y+6*d, x+4*d, y+7*d, fill=f)
        canvas.create_rectangle(x+2*d, y+6*d, x+3*d, y+7*d, fill=f)
        canvas.create_rectangle(x+d, y+6*d, x+2*d, y+7*d, fill=f)
        canvas.create_rectangle(x, y+6*d, x+d, y+7*d, fill=f)
        x=8*d+x
    y=y+d*8
    x=xx
canvas.mainloop()