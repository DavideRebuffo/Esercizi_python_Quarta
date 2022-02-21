def main():
    f = open("./covid-19_gen1.txt","r")
    lista = f.readlines()
    contaA,contaC,contaG,contaT,dizionario = 0,0,0,0,{}
    for cella in lista:
        for carattere in cella:
            if carattere == "A":
                contaA +=1
            elif carattere == "T":
                contaT+=1
            elif carattere == "C":
                contaC+=1
            elif carattere == "G":
                contaG+=1
    dizionario["A"],dizionario["T"],dizionario["C"],dizionario["G"] = contaA,contaT,contaC,contaG
    for chiave in dizionario:
        print(f"numero di {chiave}: {dizionario[chiave]}")
    f.close()

if __name__ == "__main__":
    main()