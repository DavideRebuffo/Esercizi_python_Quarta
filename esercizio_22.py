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

if isPrimo(int(input("inserisci un numero: "))):
    print("il numero è primo")
else:
    print("il numero non è primo")