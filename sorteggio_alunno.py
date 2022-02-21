import random
def main():
    elenco = {1:"Bosticardo", 2:"Castellano",3:"Cavaglieri",4:"Coppola",5:"Dalmasso",6:"De Carlini",
            7:"Degiovanni",8:"Di Nicola",9:"Dutto",10:"Faggio",11:"Galfrè",12:"Galieti",
            13:"Giordano",14:"Migliore",15:"Molineri",16:"Olivero",17:"Pellegrino",18:"Piumatto",
            19:"Rebuffo",20:"Ristorto",21:"Ruggero",22:"Simondi",23:"Sparla",24:"Sulkuqi"}
    sorteggio = random.randint(1,24)
    print(f"alunno sorteggiato: {elenco[sorteggio]}")

if __name__ == "__main__":
    main()