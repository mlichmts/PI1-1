

# def sucet(retazec):
#     i = retazec.find('+')
#     return int(retazec[:i]) + int(retazec[i+1:])
#
# x = sucet('15+9')
# print(x)


# def sucet(retazec):
#     vysl = 0
#     while True:
#         i = retazec.find("+")
#         if i>0:
#             vysl += int(retazec[:i])
#             retazec = retazec [i+1:]
#         else:
#             return vysl + int(retazec)
#
# x = sucet('15+90+5')
# print(x)

# def postupnost(od, do, krok=1):
#     vysl = ''
#     for i in range(od, do, krok):
#         if vysl == '':
#             vysl = str(i)
#         else:
#             vysl += ' ' + str(i)
#     return vysl
#
# p = postupnost(13, 5,-1)
# print(p)


# def rozsekaj(text, sirka):
#     vysl = ''
#     for i in range(0, len(text), sirka):
#         vysl += text[i:i + sirka] + '\n'
#     return vysl[:-1]
#
# ret = rozsekaj('Anicka dusicka, kde si bola', 10)
# print(ret)

# def stvorec(n, znak):
#     return znak*n + "\n"+(n-2)*(znak+" "*(n-2)+znak+ "\n")+znak*n
#
#
# r = stvorec(10, '#')
# print(r)

# def vyhod_duplikaty(retazec):
#     vysl = pred = ""
#     for znak in retazec:
#         if znak != pred:
#             vysl += znak
#             pred = znak
#     return vysl
#
# x = vyhod_duplikaty('Braatisssllavaaaaa')
# print(x)

# def ozatvorkuj(retazec, podretazec):
#     if podretazec in retazec:
#         return retazec.replace(podretazec, "("+podretazec+")")
#     else:
#         return "neni tam"
#
#
# b = ozatvorkuj('Bratislava', 'ava')
# print(b)

# import tkinter
# import random
# canvas = tkinter.Canvas()
# canvas.pack()
#
# x,y = 50,130
# for i in range(0x2654,0x265A):
#     farba = f'#{random.randrange(256 ** 3):06x}'
#     canvas.create_text(x,y,text=chr(i),font="arial 50",fill=farba)
#     x += 60
#
#
# canvas.mainloop()

# import tkinter
# import random
# canvas = tkinter.Canvas()
# canvas.pack()

# def stvorce(vel,retazec):
#     x,y = 10,60
#     while retazec:
#         i = (retazec+" ").find(" ")
#         farba = retazec[:i]
#         retazec = retazec[i+1:]
#         print(retazec)
#         canvas.create_rectangle(x, y, x + vel, y + vel, fill=farba)
#         x += vel + 3
#
# stvorce(40, 'red blue purple red gold')
#
# canvas.mainloop()
import tkinter
import random
canvas = tkinter.Canvas(width=500)
canvas.pack()

def stvorce(retazec):
    x,y = 10,200
    povodny=retazec
    while True:
        if retazec == "":
            retazec=povodny
        i=retazec.find(" ")
        vel = int(retazec[:i])
        retazec = retazec[i+1:]
        print(retazec)
        if x+vel>=sirka:
            break
        i=(retazec+" ").find(" ")
        farba = retazec[:i]
        retazec = retazec[i+1:]
        canvas.create_rectangle(x, y, x + vel, y - vel, fill=farba)
        x += vel + 3
sirka = 450

stvorce('40 red 20 blue 60 purple 40 red 30 gold')


canvas.mainloop()