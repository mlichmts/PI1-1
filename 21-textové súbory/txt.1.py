fmena = open("mena.txt","r",encoding="utf-8")  #otvorí súbor mena.txt na citanie r-citanie, w-zápis
# fmena = open("C:/dokumenty/mena.txt","r") #hlada v danom "file"


while True:
    riadok = fmena.readline()
    if riadok == "":
        break
    print(riadok[:-1])                              #[-1] vypíše všetky znaky od nulteho po -1




fmena.close() #zatvorenie súboru, vzdy treba !!!