lista = [3,2.2,6,8.7]
max = 0
min = 0

for indice,cella in enumerate(lista):
    if indice == 0:
        min = cella
    if cella > max:
        max = cella
    elif cella < min:
        min = cella
print(lista)
print(f"il numero minore della lista è {min}, mentre il massimo è {max}")