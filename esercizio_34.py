#gioco del tris
def chiediMossa(giocatore):
    """chiede un numero all' utente e verifica che sia inseribile nella griglia"""
    print(f"E' il turno di {giocatore}")
    continua = True
    while continua == True:
        numero = int(input("INSERISCI DOVE VUOI INSERIRE: "))
        if numero < 1 | numero > 9:
            continua = True
            print("Il numero inserito non è corretto")
        else:
            continua = False
    return (numero)

def isCellaOccupata (numero,giocatore): 
    """controlla se la cella della griglia sia già occupata"""
    if griglia[numero] == " ":
        ok = False
        if giocatore == giocatore1:
            griglia[numero] = "X"
        else:
            griglia[numero] = "O"
    else:
        print("Posizione gia occupata")
        ok = True
    return (ok)

def disegnaGriglia():
    """disegna la griglia"""
    print(f"{griglia[1]} | {griglia[2]} | {griglia[3]} \n---------\n{griglia[4]} | {griglia[5]} | {griglia[6]} \n---------\n{griglia[7]} | {griglia[8]} | {griglia[9]}")

def isVincitore(giocatore):
    ok = False
    if giocatore == giocatore1:
        tris = "XXX"
    else:
        tris = "OOO"
    if ((str(griglia[1]) + str(griglia[2]) + str(griglia[3]) ==tris) | (str(griglia[4]) +
    str(griglia[5]) + str(griglia[6]) == tris) | (str(griglia[7]) + str(griglia[8]) + 
    str(griglia[9]) == tris) | (str(griglia[1]) + str(griglia[4]) + str(griglia[7]) == tris)
    | (str(griglia[2]) + str(griglia[5]) + str(griglia[8]) == tris) | (str(griglia[3]) +
    str(griglia[6]) + str(griglia[9]) == tris) | (str(griglia[1]) + str(griglia[5]) + 
    str(griglia[9]) == tris) | (str(griglia[3]) + str(griglia[5]) + str(griglia[7]) == tris)):
        ok = True
    return (ok)

griglia = {1:" ",2:" ",3:" ",4:" ",5:" ",6:" ",7:" ",8:" ",9:" "}

giocatore1 = input("inserisci il nome del primo giocatore: ")
giocatore2 = input("inserisci il nome del secondo giocatore: ")

disegnaGriglia()
vincita = False
conta = 0
inserimentoValoreCorretto = True
inserimentoValoreCorretto2 = True
while vincita == False & conta < 9:
    while inserimentoValoreCorretto == True:
        posizioneGiocatore1 = chiediMossa(giocatore1)
        inserimentoValoreCorretto = isCellaOccupata(posizioneGiocatore1, giocatore1)
    inserimentoValoreCorretto = True
    disegnaGriglia()
    if isVincitore(giocatore1):
        vincita = True
        break
    conta+=1
    if conta == 9:
        break
    while inserimentoValoreCorretto2 == True:
        posizioneGiocatore2 = chiediMossa(giocatore2)
        inserimentoValoreCorretto2 = isCellaOccupata(posizioneGiocatore2, giocatore2)
    inserimentoValoreCorretto2 = True
    disegnaGriglia()
    if isVincitore(giocatore2):
        vincita = True
    conta+=1

if conta == 9:
    print("Pareggio")
elif isVincitore(giocatore1):
    print(f"{giocatore1} vince la partita")
else:
    print(f"{giocatore2} vince la partita")