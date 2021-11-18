stringa = "ornitorinco"

print(f"la prima lettera è {stringa[0]} e l' ultima è {stringa[-1]}")

#tutto tranne primo e ultimo
print(stringa[1:-1])

#1 si 1 no
print(stringa[::2])

#al contrario
print(stringa[::-1])

#con ? al 3 carattere
stringa_nuova = stringa[:2] + "?" + stringa[3:]
print(stringa_nuova)