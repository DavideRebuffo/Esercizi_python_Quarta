#if --> funziona esattamente come il c
#if elif else

voto = int(input("inserisci  il voto che hai preso nella verifica: "))

if voto >= 8:
    print("Eccellente")
elif (voto >= 7) & (voto < 8):
    print("Buono")
elif (voto >= 6) & (voto < 7):
    print("Sufficiente")
else:
    print("insufficiente")

#ciclo while
#il python ha 2 cicli --> il while e il for

voto1 = -1

while voto1 < 6:
    print("Sei insufficiente")
    voto1 = int(input("inserisci  il voto che hai preso nella verifica: "))


#ciclo for

classi = ["4arob","3arob", "5brob","4achi", "3ainf"]
indirizzi = {"rob": "Smart-robot", "chi": "Chimica", "inf": "Informatica"}


for indice,classe in enumerate (classi):
    indirizzo = indirizzi[classe[2:]]
    print(f"Posizione {indice+1} nella lista: ")
    print(f"la classe {classe} è del indirizzo {indirizzo}",end="\n\n")