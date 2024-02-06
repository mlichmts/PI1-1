import tkinter
canvas = tkinter.Canvas(width=500, height=500)
canvas.pack()


a=int(input("Zadaj sirku"))
b=int(input("Zadaj vysku"))

vel = 30
farba1, farba2 = 'maroon', 'gold'
x=50
y=50
xx=50

for i in range(b):
    farba1, farba2 = farba2, farba1
    for j in range(a):
        canvas.create_rectangle(x,y,x+vel,y+vel,fill=farba1)
        farba1, farba2 = farba2, farba1
        x=x+vel+3
    x=xx
    y=y+vel+3
canvas.mainloop()