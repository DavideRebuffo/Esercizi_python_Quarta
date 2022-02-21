class Pila():
    def __init__(self):
        self.pila = []
    
    def push(self,elemento):
        self.pila.append(elemento)
    
    def pop(self):
        if self.pila.__len__() != 0:
            return self.pila.pop()
        else:
            return None
    
    def print(self):
        print(self.pila)

class Coda():
    def __init__(self):
        self.coda = []
    
    def enqueue(self,elemento):
        self.coda.append(elemento)

    def dequeue(self):
        if self.coda.__len__ != 0:
            return self.coda.pop(0)
        else:
            return None
    
    def print(self):
        print(self.coda)

def main():
    p1 = Pila()
    p1.push("salve")
    p1.push(8)
    p1.print()
    
    c1 = Coda()
    c1.enqueue("ciao")
    c1.enqueue(5)
    c1.print()

if __name__ == "__main__":
    main()

