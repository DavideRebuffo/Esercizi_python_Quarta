serie = []

def fibonacci(ultimo,penultimo,limite):
    num = ultimo + penultimo
    if num < limite:
        serie.append(num)
        fibonacci(num, ultimo, limite)
    return serie

def main():
    limite = int(input("inserisci un numero: "))
    print(fibonacci(1,1,limite))

if __name__ == "__main__":
    main()