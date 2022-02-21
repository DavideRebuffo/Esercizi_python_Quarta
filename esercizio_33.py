f = open("c:/Users/Client/Desktop/SHULKER BOX/SCUOLA/4a/SISTEMI E RETI/TEORIA/PYTHON/datiAnaGrafici.txt","w")
dizionario = {}
quanti = int(input("quanti elementi vuoi inserire? "))
for _ in range(quanti):
    dizionario["Nome"] = input("inserisci nome: ")
    dizionario["Cognome"] = input("inserisci cognome: ")
    dizionario["Giorno"] = int(input("inserisci giorno di nascita: "))
    dizionario["Mese"] = int(input("inserisci mese di nascita: "))
    dizionario["Anno"] = int(input("inserisci anno di nascita: "))
    f.write("Nome: " + dizionario["Nome"] + " Cognome: " + dizionario["Cognome"] + " Nato il: " +
            str(dizionario["Giorno"]) + "/" + str(dizionario["Mese"]) + "/" + str(dizionario["Anno"]) + "\n")
f.close()