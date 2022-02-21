#1) chiedere stringa utente.
#2) ciclo sulla stringa in cui snobbate tutto cio che nn è ()[]{}
#3) se trovo parentesi aperta faccio push
#4)se trovo parentesi chiusa faccio pop 
stringa,parentesiAperte,parentesiChiuse,parentesi = "Stringa_costante[ BLA BLA}",["(","[","{"],[")","]","}"],["(","[","{",")","]","}"]

isParentesiAperta = lambda carattere: carattere in parentesiAperte
isParentesiChiusa = lambda carattere: carattere in parentesiChiuse
confronta = lambda carattere,indice: parentesi[indice] == carattere

def trovaIndice(carattere):
    k = 0
    while k < 3:
        if carattere == parentesiChiuse[k]:
            break
        else:
            k+=1
    return k

def main():
    lista = []
    for carattere in stringa:
        if isParentesiAperta(carattere):
            lista.append(carattere)
        if isParentesiChiusa(carattere):
            indice = trovaIndice(carattere)
            par = lista.pop()
            if confronta(par ,indice):
                print("PARENTESI CORRETTE")
            else:
                print("ERRORE")

if __name__ == "__main__":
    main()