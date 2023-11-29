import tkinter,random


canvas = tkinter.Canvas(width=500, height=500)
canvas.pack()

meno = "Jan"
priezvisko = "Mrkvička"
vek = 255

print("volám sa",meno,priezvisko,"a")
print(F"Volam sa {meno} {priezvisko} a mam {vek:02x} rokov") #vek:02x, 02 je pocet cifier a x prevedie do 16tkovej sustavy

polomer=10

for i in range(50):
    x=random.randint(2,480)
    y=random.randint(2,480)
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    farba = f"#{r:02x}{g:02x}{b:02x}"
    canvas.create_oval(x-polomer,y-polomer,x+polomer, y + polomer,fill=farba)



canvas.mainloop()