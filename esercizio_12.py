primoNumero = float(input("inserisci una variabile: "))
secondoNumero = float(input("inserisci la seconda variabile: "))

lista = []

lista.append((primoNumero**2) + (secondoNumero **2))
lista.append((primoNumero+secondoNumero)**2)
lista.append((primoNumero**2) - (secondoNumero **2))
lista.append((primoNumero - secondoNumero)**2)
print(lista)
