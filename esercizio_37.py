isDivisibile = lambda divisibile: numero % divisibile == 0
numero = int(input("inserisci un numero: "))

if isDivisibile(2):
    print("il numero è divisibile per 2")
if isDivisibile(3):
    print("il numero è divisibile per 3")
if isDivisibile(5):
    print("il numero è divisibile per 5")
else: 
    print("il numero non è divisibile ne per 2 ne per 3 ne per 5")