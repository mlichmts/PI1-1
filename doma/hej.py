import turtle

t = turtle


def polkruznica(velkost,smer):
    if smer:
        uhol = 10
    else:
        uhol = -10
    for i in range(18):
        t.fd(velkost)
        t.lt(uhol)
t.lt(90)
for i in range(10):
    polkruznica(3,i%2)

t.mainloop()
