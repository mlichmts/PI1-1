import tkinter


canvas = tkinter.Canvas(height=600, width=800)
canvas.pack()
pocet_riadkov = int(input("Zadaj počet riadkov: "))
def farba (r, g, b):
    return f"#{r:02x}{g:02x}{b:02x}"

def stvorce ( x, y, pocet, dlzka, r=255, g=255, b=255 ):
    for j in range(pocet_riadkov):
        y=y+dlzka
        for i in range(pocet):
            krok = 255//dlzka
            canvas.create_rectangle(x, y, x+dlzka, y+dlzka, fill=farba(r,g,b))
            x = x+dlzka
            if r > krok:
                 r -= krok
            if g > krok:
                 g -= krok
            if b > krok:
                 b -= krok
            if x == 420:
                x = 20
            if r == 15:
                r = 255
            if r == 255:
                r = 0
                g = 255
            if g == 15:
                g = 0
                b = 255
            if b == 15:
                b = 0
                r = 255
stvorce(20,20,20,20,255,0,0)


tkinter.mainloop()