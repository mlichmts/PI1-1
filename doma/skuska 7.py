
while True:
    cislo = int(input("Zadaj číslo: "))
    pocet = 0
    for i in range(2,cislo+1):
        if cislo % i == 0:
            print(i," ",)
            pocet += 1

    if pocet >= 1:
        print(f"Číslo {cislo} je prvocislo")
    else:
        print(f"Číslo {cislo} nie je prvocislo")
    print("počet delitelov je",pocet)
    print()
    if cislo == 0:
        break