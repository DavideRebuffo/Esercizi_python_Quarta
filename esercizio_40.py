import random
def movimento():
    n = random.randint(0, 1)
    if n == 0:
        n = -1
    return (n)

lista = [movimento() for _ in range(5*24*60*60)]
somma = 0
for cella in lista:
    somma = somma + cella
print(somma)