import tkinter

canvas = tkinter.Canvas(width=600, height=500)
canvas.pack()


x = 5
y = 5
d = 35
xx = 5
stvrtina = d // 4
vyskadomceka= d+2*stvrtina
pocet = 598//d  #dve // je celociselne delenie 7//3=2
vyska = 498//vyskadomceka

for j in range(vyska):
    for i in range (pocet):
        canvas.create_rectangle(x, y+d//2, x+d,y+(d+d//2), fill= "orange")
        canvas.create_polygon(x, y+d//2,x+2*stvrtina,y,x+d,y+d//2 , fill="red")
        canvas.create_rectangle(x+stvrtina, y+d // 2+stvrtina, x+3*stvrtina, y+d+stvrtina, fill="light blue")
        canvas.create_line(x+stvrtina, y+d//2+2*stvrtina, x+3*stvrtina,y+d)
        canvas.create_line(x+2*stvrtina, y+d // 2+stvrtina,x+2*stvrtina, y+d+stvrtina)
        x=x+d
    y=y+d+2*stvrtina
    x=xx



canvas.mainloop()