import tkinter, random

canvas=tkinter.Canvas(width=500,height=500)
canvas.pack()

x, y = 10, 120

# for i in range(47):
#     x1=x+10
#     y1=y+random.randint(-10,10)
#     canvas.create_line(x,y,x1,y1)
#     x,y = x1 , y1


# for i in range(20):
#     x2 = random.randint(5, 480)
#     y2 = random.randint(5, 498)
#     canvas.create_text(x2,y2,text="poj ma tricat",)


for i in range(40):
    dlzka = random.randint(2,100)
    x = random.randint(2,480)
    y = random.randint(2,480)
    r =random.randint(1,255)
    g=random.randint(1,255)
    b=random.randint(1,255)
    farba = f"#{r:02x}{g:02x}{b:02x}"
    canvas.create_rectangle(x,y,x+dlzka,y+dlzka,fill = farba)



canvas.mainloop()