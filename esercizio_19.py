lista = ["ciao", "ornitorinco", "facile"]
max = ""

for cella in lista:
    if(len(cella)> len(max)):
        max = cella
print(max)
