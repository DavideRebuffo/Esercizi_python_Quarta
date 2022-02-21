def push(pila,elemento):
    pila.append(elemento)

def pop(pila):
    if pila.__len__() != 0:
        return pila.pop()
    else:
        return None


stringa = input("inserisci una stringa: ")
pila = []
for carattere in stringa:
    push(pila,carattere)

while pila.__len__()!= 0:
    print(pop(pila))
