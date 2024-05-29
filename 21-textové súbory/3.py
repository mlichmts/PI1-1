import tkinter
canvas = tkinter.Canvas(height=400,width=400)
canvas.pack()




fbody =open("body.txt","r")

for riadok in fbody:
    i= riadok.find(" ")
    x =  int(riadok[:i])
    y = int(riadok[i:])
    canvas.create_oval(x,y,x+20,y+20)
    print(x,y)












canvas.mainloop()
