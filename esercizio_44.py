lista = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"," "]

def trovaInLista(lettera):
    continua = True
    k = 0
    while continua == True:
        if lettera != lista[k]:
            k+=1
            continua = True
        else:
            continua = False
    return (k)

def codifica():
    stringa = input("inserisci la stringa da crittografare: ")
    stringa = stringa.upper()
    numero = int(input("inserisci il numero per la crittografia: "))
    stringaCritto = ""
    #codifica
    for lettera in stringa:
        indice = trovaInLista(lettera)
        stringaCritto = stringaCritto + lista[(indice+numero)% lista.__len__()]
    print(f"La stringa crittografata è: {stringaCritto}")

def decodifica():
    stringa = input("inserisci la stringa da crittografare: ")
    stringa = stringa.upper()
    listaStringhe = []
    stringaDecritto = ""
    for k in range(1,lista.__len__()-1):
        for lettera in stringa:
            indice = trovaInLista(lettera)
            stringaDecritto = stringaDecritto + lista[(indice-k)% lista.__len__()]
        listaStringhe.append(stringaDecritto)
        stringaDecritto = ""
    print(listaStringhe)

def main():
    risposta = "si"
    while risposta == "si":
        conferma = True
        while conferma == True:
            scelta = int(input("inserisci 0 per codificare e 1 per decodificare: "))
            if scelta == 0 | scelta == 1:
                conferma = False
            else:
                conferma = True
                print("inserisci un valore corretto")
        if scelta == 0:
            cofidica()
        elif scelta == 1:
            decodifica()
        risposta = input("vuoi continuare? ")

if __name__ == "__main__":
    main()