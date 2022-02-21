"""Autore: Davide Rebuffo"""

import random
lista = [1,2,3,4,5,6,7,8,9]

def main():
    listaNuova,listaDoppi = [],[]
    while len(listaNuova) != len(lista):
        indice = random.randint(0,len(lista)-1)
        if indice not in listaDoppi:
            listaNuova.append(lista[indice])
        listaDoppi.append(indice)
    print(listaNuova)

if __name__ == "__main__":
    main()