maiuscola = lambda stringa:True if((stringa[0] >= 'A') &( stringa[0] <= 'Z'))else None

s = input("inserisci una stringa: ")
if maiuscola(s):
    print("la stringa inizia con una lettera maiuscola")
else:
    print("la stringa non inizia con una lettera maiuscola")