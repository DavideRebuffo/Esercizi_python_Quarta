def calcolaFattoriale(numero):
    if numero == 0:
        return 1
    else:
        return numero*calcolaFattoriale(numero-1)

def main():
    numero = int(input("inserisci un numero: "))
    print(f"il fattoriale di {numero} è {calcolaFattoriale(numero)}")

if __name__ == "__main__":
    main()