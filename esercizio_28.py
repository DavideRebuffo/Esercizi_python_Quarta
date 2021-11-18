palindroma = lambda stringa:True if(stringa == stringa[::-1])else None

stringa = input("inserisci una stringa: ")

if palindroma(stringa):
    print("la stringa è palindroma")
else:
    print("la stringa non è palindroma")