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
for numero in range(1,1000):
    if isPrimo(numero):
        conta+=1
print(f"i numeri primi da 1 a 1000 sono: {conta}")