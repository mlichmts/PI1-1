def sucet(x, y):
    return x+y

def parne(cislo):
    if cislo % 2 == 0:
        return "je parne"
    else:
        return "nie je parne"

def prvocislo (cislo):
    prvocis=True
    for i in range(2,cislo):
        if cislo % i == 0:
            prvocis=False
    return prvocis

a = int(input("Zadaj a: "))
b = int(input("Zadaj b: "))
sucet = sucet(a, b)
print(f"sucet cisla {a} a cisla {b} je:{sucet} ")
print(f"Cislo {a} {parne(a)}")
print(f"Cislo {b} {parne(b)}")
if prvocislo(a):
    print(f"Cislo {a} je prvocislo")
else:
    print(f"Cislo {a} nie je prvocislo")
if prvocislo(b):
    print(f"Cislo {b} je prvocislo")
else:
    print(f"Cislo {b} nie je prvocislo")