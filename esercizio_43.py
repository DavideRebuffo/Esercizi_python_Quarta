def trovaInLista(lettera):
    continua,k = True,0
    while continua == True:
        if lettera != lista[k]:
            k+=1
            continua = True
        else:
            continua = False
    return (k)

def cirfrario(stringa,chiave,metodo):
    if metodo == 1:
        chiave = chiave * -1
    stringaCritto = ""
    for lettera in stringa:
        indice = trovaInLista(lettera)
        stringaCritto = stringaCritto + lista[(indice+chiave)% lista.__len__()]
    return (stringaCritto)

lista = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"," "]

def main():
    stringa = input("inserisci la stringa da crittografare: ")
    stringa = stringa.upper()
    numero = int(input("inserisci il numero per la crittografia: "))
    metodo = int(input("inserisci 0 per codificare o 0 per decodificare: "))
    parolaDiversa = cirfrario(stringa, numero,metodo)
    print(f"La stringa crittografata è: {parolaDiversa}")

if __name__ == "__main__":
    main()