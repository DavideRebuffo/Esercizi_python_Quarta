palindroma = lambda stringa:True if(stringa == stringa[::-1])else None
maiuscola = lambda stringa:True if((stringa[0] >= 'A') &( stringa[0] <= 'Z'))else None


lista = ["anna", "non", "siuuuuum", "Simone"]
palindrome = []
maiuscole = []

for cella in lista:
    if maiuscola(cella):
        maiuscole.append(cella)
    if palindroma(cella):
        palindrome.append(cella)

print(f"le stringhe con la iniziale maiuscola sono: {maiuscole}")
print(f"le stringhe palindrome sono: {palindrome}")