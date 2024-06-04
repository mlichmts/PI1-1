# # def priemer(a, b):
# #     return (a + b) / 2
# #
# #
# # print(priemer(5,2))
#
#
# # def nsn(a,b):
# #     sucin=a*b
# #     while b!=0:
# #         a,b=b,a%b
# #     return sucin//a
# #
# #
# #
# # print(nsn(5,))
#
#
# # def vyhod_medzery(text):
# #     novy=""
# #     for znak in text:
# #         if znak != " ":
# #             novy+=znak
# #     return novy
# #
# #
# # print(vyhod_medzery('  mám   rád Python '))
#
# # import tkinter
#
# # def koleso(x,y,r=15,farba="blue"):
# #     canvas.create_oval(x-r,y-r,x+r,y+r,fill=farba)
# #
# #
# # def doska(x, y, sir=100, vys=20, farba='red'):
# #     canvas.create_rectangle(x-sir/2, y, x+sir/2, y-vys, fill=farba)
# #
# # def maly_vozik(x, y):
# #     doska(x, y)
# #     koleso(x - 30, y)
# #     koleso(x + 30, y)
# #
# # def velky_vozik(x, y):
# #     doska(x, y, 150, 40, 'green')
# #     koleso(x - 35, y, 25, 'orange')
# #     koleso(x + 35, y, 25, 'orange')
# #
# # canvas = tkinter.Canvas()
# # canvas.pack()
# #
# # maly_vozik(200, 100)
# # velky_vozik(150, 200)
# # maly_vozik(300, 210)
# #
# # tkinter.mainloop()
#
# import tkinter
# import random
# canvas = tkinter.Canvas()
# canvas.pack()
#
#
# # def kruhy(x,y):
# #     sirka = 50
# #     for i in range(10):
# #         farba = f'#{random.randrange(256 ** 3):06x}'
# #         canvas.create_oval(x+sirka,y+sirka,x-sirka,y-sirka,fill=farba)
# #
# #         sirka=sirka-5
# #
# # for i in range(10):
# #     kruhy(random.randint(50, 330), random.randint(50, 210))
# #
# # def karticky(x,y,text):
# #     canvas.create_rectangle(x-50,y-20,x+50,y+20,fill="light gray")
# #     canvas.create_text(x,y,text=text,font="arial 14")
# #
# # for i in range(10):
# #
# #     karticky(random.randint(50, 330), random.randint(50, 210),"ahoj")
#
# def nahodna_farba():
#     return f'#{random.randrange(256**3):06x}'
# def dom(x, y, vel1, vel2):
#     canvas.create_rectangle(x,y,x+vel1,y-vel2,fill=nahodna_farba())
#     canvas.create_polygon(x,y-vel2,x+vel1,y-vel2,x+vel1/2,y-vel2-vel1,fill=nahodna_farba())
#
#
#
# x, y = 10, 150
# while x < 330:
#     v = random.randint(20, 50)
#     dom(x, y, v, random.randint(v // 2, v))
#     x += v
#
#
#
#
#
#
# tkinter.mainloop()


# def obdlznik(sirka,znak="*"):
#     print(sirka*znak)
#     print(znak + (sirka - 2) * ' ' + znak)
#     print(sirka*znak)
#
#
# obdlznik(25, '#')

# import random
#
#
# def hadanie(od,do):
#     print("myslim si cislo,uhadni ho")
#     cislo =random.randint(od,do)
#
#
#     for i in range(10):
#         hadane_cislo = int(input("zadaj ciselko: "))
#         if hadane_cislo < cislo:
#             print("je to väcsie")
#         if hadane_cislo > cislo:
#             print("je mensie")
#         if hadane_cislo == cislo:
#             print("toto je ono")
#             break
#     if i <9:
#         print("uhadol si na",i+1,"pokus")
#     else:print("slaby chren")
#     print("bolo to cislo ",cislo)
#
#
#
#
# hadanie(1, 100)
#
# import tkinter
# import random
# canvas = tkinter.Canvas(height=500,width=500)
# canvas.pack()
# def rgb(r, g, b):
#     return f'#{r:02x}{g:02x}{b:02x}'
#
# # def nahodna_farba():
# #     return f'#{random.randrange(256**3):06x}'
# def stv(riadok,stlpec,farba="white"):
#     x, y = 5 + stlpec * 30, 5 + riadok * 30
#     canvas.create_rectangle(x,y,x+30,y+30,fill=farba)
#
# for i in range(8):
#     for j in range(12):
#         stv(i, j, rgb(255, (i+j) * 14, 0))
#
#
#
# tkinter.mainloop()

# def sucet (retazec):
# #     vysl=0
# #     while True:
# #         i=retazec.find("+")
# #         if i>0:
# #             vysl+= int(retazec[:i])
# #             retazec=retazec[i+1:]
# #         else:
# #             return vysl+int(retazec)
# #
# # x = sucet('12+9+5')
# # print(x)

# def postupnost(od,do,krok=1):
#     vysl=""
#     for i in range(od,do+1,krok):
#         if vysl == "":
#             vysl=str(i)
#         else:
#             vysl += ' ' + str(i)
#     return vysl
#
# p = postupnost(5, 13)
# print(p)

# def riadok(n,text=""):
#     while text:
#         text=" "+text+" "
#         pol1=(n-len(text))//2
#         pol2 = (n - len(text)) // 2
#         vysl="*"*pol1+text+"*"*pol2
#         return vysl
#
# sir = 40
# riadok(sir)
# print(riadok(sir, 'Ján Botto'))
# print(riadok(sir, 'Žltá ľalija'))

# def priemer(a,b):
#     return (a+b)/2
#
#
# print(priemer(5,6))


# def nsn(a,b):
#     sucin = a*b
#     while b!=0:
#         a,b=b,a%b
#
#     return sucin//a
#
#
# print(nsn(129, 162))


# def vyhod_medzery(text):
#     vysledol=""
#     for znak in text:
#         if znak!=" ":
#             print(znak)
#             vysledol+=znak
#     return vysledol
#
#
# print(vyhod_medzery('  mám   rád Python '))

# import tkinter
# import random
# canvas = tkinter.Canvas()
# canvas.pack()
# def nahodna_farba():
#     return f'#{random.randrange(256**3):06x}'
#
# def stv(riadok,stlpec,farba="white"):
#     x=5+stlpec*30
#     y = 5 + riadok * 30
#     canvas.create_rectangle(x,y,x+30,y+30,fill=farba)
#
#
# for i in range(8):
#     for j in range(12):
#         if i == j:
#             stv(i, j)
#         else:
#             stv(i, j,nahodna_farba())
#
#
#
# canvas.mainloop()

# def sucet (retazec):
#     i=retazec.find("+")
#     return  int(retazec[:i]+retazec[i+1:])


# def sucet (retazec):
#     vysl=0
#     while True:
#         i=retazec.find("+")
#         if i>0:
#             vysl += int(retazec[:i])
#             retazec = retazec[i+1:]
#         else: return int(retazec)+vysl
#
#
# print(sucet('1+2+3+4'))

# def postupnost(start,koniec,krok=1):
#     vysl=""
#     for i in range(start,koniec,krok):
#         vysl+=" "+str(i)
#
#     return vysl
#
#
# p = postupnost(5, 20,2)
# print(p)

# def rozsekaj(text,sirka):
#     vysl=""
#     for i in range(0,len(text),sirka):
#         print(i)
#         vysl+=text[i:i+sirka]+"\n"
#
#     return vysl[:-1]
#
#
# ret = rozsekaj('Anicka dusicka, kde si bola', 10)
# print(ret)

# def vyhod(retazec):
#     vysl=pred=""
#     for znak in retazec:
#         if znak !=pred:
#             vysl+=znak
#             pred=znak
#     return vysl
#
#

# import tkinter
#
# def stvorce(vel, retazec):
#     x, y = 10, 60
#     while retazec:
#         i = (retazec+" ").find(' ')
#         farba = retazec[:i]
#         retazec = retazec[i + 1:]
#         canvas.create_rectangle(x, y, x + vel, y + vel, fill=farba)
#         x += vel+3
#
# canvas = tkinter.Canvas()
# canvas.pack()
#
# stvorce(40, 'red blue purple red gold')
#
# tkinter.mainloop()

import tkinter

# def kresli(retazec):
#     x, y = 100, 100
#     for znak in retazec:
#         x1, y1 = x, y
#         if znak == 's':
#             y1 -= 10
#         elif znak == 'v':
#             x1 += 10
#         elif znak == 'j':
#             y1 += 10
#         elif znak == 'z':
#             x1 -= 10
#         else:
#             print('nerozumiem "' + znak + '"')
#             return
#         canvas.create_line(x, y, x1, y1)
#         x, y = x1, y1
#
# canvas = tkinter.Canvas()
# canvas.pack()
#
# kresli('ssvvjjzzvvvvjjzzssjjjjzzssvvzzzzssvvjj')
#
# tkinter.mainloop()

def posun_znak(znak, posun):
    if 'a' <= znak <= 'z':
        return chr((ord(znak) - 97 + posun) % 26 + 97)
    return znak
def zakoduj(text, posun):
    vysl = ''
    for znak in text:
        vysl += posun_znak(znak, posun)
    return vysl

x = zakoduj('pyThon', 10)
print(x)