fmeno = open("mena.txt","r",encoding="utf-8")
fpriezvisko= open("priezviska.txt","r",encoding="utf-8" )
fmena_priezviska = open("mena_priezviska.txt","w",encoding="utf-8") #w otvori subor na zapis, ak neexistuej ,tak sa vytvori a ak existuje tak sa zmaze jeho obsah
for meno in fmeno:
    priezvisko=fpriezvisko.readline()

    print(f"{meno.strip()}, {priezvisko.strip()}",file=fmena_priezviska)
    # fmena_priezviska.write(f"{meno.strip()}, {priezvisko.strip()}\n")

fpriezvisko.close()
fmeno.close()
fmena_priezviska.close()