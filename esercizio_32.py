f = open("c:/Users/Client/Desktop/SHULKER BOX/SCUOLA/4a/SISTEMI E RETI/TEORIA/PYTHON/numeriPrimi.txt", "w")

def isPrimo(numero):
    ok = True
    rovescio = numero-1
    while (ok == True) & (rovescio > 1):
        if numero % rovescio == 0:
            ok = False
        rovescio-=1
    if rovescio == 0:
        ok = False
    return (ok)
conta = 0
numero = 1
while conta < 100:
    if isPrimo(numero):
        f.write(str(numero) + "\n")
        conta+=1
    numero+=1

f.close()