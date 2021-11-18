print("""Applicazione calcolatrice
        1) addizione
        2) sottrazione
        3) moltiplicazione
        4) divisione
        5) potenza""")

scelta =int(input("scegli il tipo di calcolo che vuoi fare: "))
num1 = float(input("inserisci il primo numero: "))
num2 = float(input("inserisci il secondo numero: "))

if scelta == 1:
    print(f"La somma tra {num1} e {num2} è: {num1+num2}")
elif scelta == 2:
    print(f"La differenza tra {num1} e {num2} è: {num1-num2}")
elif scelta == 3:
    print(f"Il prodotto tra {num1} e {num2} è: {num1*num2}")
elif scelta == 4:
    print(f"Il quozionte tra {num1} e {num2} è: {num1/num2} e il resto è di: {num1%num2}")
elif scelta == 5:
    print(f"{num1} alla {num2} da come risultato: {num1**num2}")