import random,sys,pygame

def assegnaCelleVuote(mappa):
    dizionario,n,dim = {},0,len(mappa)
    for k in range(dim):
        for j in range(dim):
            if mappa[k][j] == 0:
                dizionario[n] = [k,j]
                n+=1
    return dizionario

def controlloBordi(lista,dim):
    dizioBool,ritorno= {"su":None,"giu":None,"dx":None,"sx":None},[]
    if lista[0] == 0 :
        dizioBool["su"] = False
    if lista[1] == 0:
        dizioBool["sx"] = False
    if lista[0] == dim-1:
        dizioBool["giu"] = False
    if lista[1] == dim-1:
        dizioBool["dx"] = False
    for chiave in dizioBool:
        if dizioBool[chiave] == False: ritorno.append(chiave)
    return ritorno

def trovaChiave(dizioVuote,x,y):
    for chiave in dizioVuote:
        if dizioVuote[chiave] == [x,y]: return chiave
    return -1

def controlloFinale(opzioniSbagliate,mappa,dizioVuote,chiave):
    listaFinale = []
    if "su" not in opzioniSbagliate: 
        chiaveTrovata = trovaChiave(dizioVuote, dizioVuote[chiave][0]-1, dizioVuote[chiave][1])
        if  chiaveTrovata != -1: 
            listaFinale.append(chiaveTrovata)
    if "giu" not in opzioniSbagliate:
        chiaveTrovata = trovaChiave(dizioVuote, dizioVuote[chiave][0]+1, dizioVuote[chiave][1])
        if  chiaveTrovata != -1: 
            listaFinale.append(chiaveTrovata)
    if "dx" not in opzioniSbagliate:
        chiaveTrovata = trovaChiave(dizioVuote, dizioVuote[chiave][0], dizioVuote[chiave][1]+1)
        if  chiaveTrovata != -1:
            listaFinale.append(chiaveTrovata)
    if "sx" not in opzioniSbagliate:
        chiaveTrovata = trovaChiave(dizioVuote, dizioVuote[chiave][0], dizioVuote[chiave][1]-1)
        if  chiaveTrovata != -1:
            listaFinale.append(chiaveTrovata)
    return listaFinale

def creaMappa(dim):
    mat = [[0]*dim for _ in range(dim)]
    for k in range(dim):
        for j in range(dim):
            x = random.choice([0,0,0,0,1])
            mat[k][j] = x
    return mat



def trovaAdiacenze(mappa,dizioVuote):
    dizioAdiacenze,opzioniSbagliate = {},[]
    for chiave in dizioVuote:
        opzioniSbagliate = controlloBordi(dizioVuote[chiave],len(mappa))
        print(f"{chiave}: {opzioniSbagliate}")
        dizioAdiacenze[chiave] = controlloFinale(opzioniSbagliate,mappa,dizioVuote,chiave)
    return dizioAdiacenze

def main():
    #mappa = [[0,0,0,1],[1,0,0,1],[0,0,0,0],[1,1,1,0]]
    mappa = creaMappa()
    print(mappa)
    sys.exit()
    dizioVuote = assegnaCelleVuote(mappa)
    print(f"dizionario delle celle il cui si puo andare: {dizioVuote}")
    print(f"dizionario adiacenze: {trovaAdiacenze(mappa, dizioVuote)}")

if __name__ == "__main__":
    main()