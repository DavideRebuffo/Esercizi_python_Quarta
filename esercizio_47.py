def enqueue(coda,elemento):
    coda.append(elemento)

def dequeue(coda):
    if coda.__len__ != 0:
        return coda.pop()
    else:
        return None

coda = []
cliente1 = {"nome": "Mario","id":123456}
cliente2 = {"nome": "John","id":654321}
cliente3 = {"nome": "Fernando","id":615243}
enqueue(coda, cliente1)
enqueue(coda, cliente2)
enqueue(coda, cliente3)
print(coda)
