import random

def main():
    lista,listaDivisa = [],[]
    f = open("./prezzi.csv","r")
    lista = f.readlines()
    for cella in lista: # divido ogni pezzo del file
        listaDivisa.append(cella.split(";"))
    print(listaDivisa)
    
    oggetto1 = "Acqua minerale (cl. 900)"
    oggetto2 = "Carne fresca suina con osso (gr. 1000)"
    oggetto3 = "Prosciutto crudo (gr.1000)"
    oggetto4 = "Parmigiano reggiano (gr.1000)"
    oggetto5 = "Zucchero (gr.1000)"
    conta = 0
    for cella in listaDivisa[0]:
        if cella == oggetto1:
            ricordo1 = conta
        if cella == oggetto2:
            rocordo2 = conta
        if cella == oggetto3:
            rocordo3 = conta
        if cella == oggetto4:
            rocordo4 = conta
        if cella == oggetto5:
            rocordo5 = conta
        conta+=1
    somma1,somma2,somma3,somma4,somma5 = 0,0,0,0,0
    contaLista = 0
    for listaContatore in listaDivisa:
        if contaLista == 0:
            somma1 = somma1 + listaContatore[ricordo1]
            somma2 = somma2 + listaContatore[ricordo2]
            somma3 = somma3 + listaContatore[ricordo3]
            somma4 = somma4 + listaContatore[ricordo4]
            somma5 = somma5 + listaContatore[ricordo5]
        contaLista+=1
    print(f"{somma1} {somma2} {somma3} {somma4} {somma5}")

if __name__ == "__main__":
    main()