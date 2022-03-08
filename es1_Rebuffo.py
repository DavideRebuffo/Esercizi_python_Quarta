def contaMedaglie(tipoMedaglia, nazione,lista):
    conta = 0
    for cella in lista:
        for pezzo in cella:
            if pezzo == nazione:
                if cella[0] == tipoMedaglia:
                    conta+=1
    return conta

def main():
    f = open("./medals.csv","r")
    lista,listaDivisa = f.readlines(),[]
    for cella in lista: # divido ogni pezzo del file
        listaDivisa.append(cella.split(","))
    dizionario = {"ori":contaMedaglie("Gold","Italy",listaDivisa),"argenti":contaMedaglie("Silver","Italy",listaDivisa),"bronzi":contaMedaglie("Bronze","Italy",listaDivisa)}
    print(f"ori: {dizionario['ori']}\nargenti: {dizionario['argenti']}\nbronzi: {dizionario['bronzi']}")
    f.close()

if __name__ == "__main__":
    main()