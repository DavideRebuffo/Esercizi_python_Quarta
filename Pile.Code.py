import esercizio_48 as pc #alias

def main():
    c1, c2,p1, risp= pc.Coda(),pc.Coda(),pc.Pila(),"si" 
    while risp == "si":
        c1.enqueue(input("inserisci un elemento dentro la pila: "))
        risp = input("vuoi continuare? ")
    c1.print()
    for _ in range(len(c1.coda)):
        p1.push(c1.dequeue())
    for _ in range(len(p1.pila)):
        c2.enqueue(p1.pila.pop())
    c2.print()

if __name__ == "__main__":
    main()