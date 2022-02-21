lista = [1,2,3,4,5,6,45,4,22,3,1]

isDoppio = lambda listaDoppi,cella: cella in listaDoppi

def main():
    listaDoppi,listaFinale = [],[]
    print(f"lista di partenza: {lista}")
    for cella in lista:
        if isDoppio(listaDoppi,cella) == False:
            listaFinale.append(cella)
        listaDoppi.append(cella)
    print(f"lista finale: {listaFinale}")

if __name__ == "__main__":
    main()