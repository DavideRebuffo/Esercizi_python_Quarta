lista = ["Dado","Gioco", "Sedia", "Palla"]

def main():
    dizionario = {indice:cella for indice,cella in enumerate(lista)} #dictionary comprehension
    print(dizionario)

if __name__ == "__main__":
    main()