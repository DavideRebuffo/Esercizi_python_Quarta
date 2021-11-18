"""
tuple
liste
dizionari

"""

#tuple --> contenitori immutabili
tupla = (3,6,-1,10)
#tupla[0] = 5    TypeError: 'tuple' object does not support item assignment
print(tupla[0])

#liste -->contenitori mutabili
listaEtero = [3,3.1415, "ciao"] #lista eterogenea --> pk fatta di tipi diversi
listaOmo = [2,3,5,7,11,13] #lista omogenea --> pk fatta di stessi tipi
print(listaEtero)
print(listaOmo)

listaEtero[1] = 2.645
print(listaEtero)

#dander = doppio underscore --> __

listaOmo.append(17)
print(listaOmo)
print(f"la lunghezza è: {len(listaOmo)}")

#come si concatenano le liste

altri_numeri_primi = [19,23,29]
molti_numeri_primi = listaOmo + altri_numeri_primi
print(molti_numeri_primi)

print(5*altri_numeri_primi)


#ciclo for
for numero_primo in listaOmo:
    print(numero_primo, end=" ")
print ("FINE")


#dizionari --> ogni elemento di un dizionario è una coppia, ogni coppia è costituita da una chiave e un valore

dizionario = {"to get": "prendere", "hello": "ciao", "print": "stampa"}

#nei dizionari non si usano indici, si accede per chiave

print(dizionario["hello"])



