lista = []
indice = 0
quanti  = int(input("inserisci il numero di numeri: "))

for indice in range(0,quanti):
    lista.append(float(input(f"inserisci numero in posizione {indice}: ")))
print(f"Lista: {lista}")

"""while indice < quanti:
    lista.append(float(input(f"inserisci numero in posizione {indice}: ")))
    indice+=1
print(f"Lista: {lista}")
"""
