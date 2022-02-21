stop = int(input("inserisci fino a che numero arrivare: "))

lista = [2**k for k in range(0,stop) if 2**k <= stop]
print(lista)