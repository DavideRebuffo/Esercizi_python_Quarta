"""none = NULL in c
True, False --> con la lettera maiuscola

garbage colletion -->pulizia della memoria dagli orfani
"""

#slicing
stringa = "Classe quarta A robotica"
print(f"il primo carattere della stringa è {stringa[0]}")
print(f"l' ultimo carattere della stringa è {stringa[-1]}")


print(stringa[0:6]) #prende i caratteri a partire da quello con indice 0 fino a quello con indice 6 escluso

print(stringa[6:]) #dal 6 in poi

print(stringa[:-2])#dall' inizio al -2

print(stringa[2:14]) #dal 2 al 14

print(stringa[2:14:2]) #dal 2 al 14 saltando di 2 in 2

print(stringa[::-1]) #inverte la stringa
"""
stringa[15] = "B" #le stringhe in python sono IMMUTABILI
TypeError: 'str' object does not support item assignment
"""
stringa_nuova = stringa[:14] + "B" + stringa[15: ]
print(stringa_nuova)
print(f"LA STRINGA MODIFICATA E': {stringa_nuova}")

print(print) #stampa la funzione print





