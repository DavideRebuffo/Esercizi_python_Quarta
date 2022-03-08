class IPAddress:
    def __init__(self,ip):
        self.ip = ip
    def bin2dec(self,stringa):
        dec = 0
        for k,carattere in enumerate(stringa[::-1]): 
            if carattere == "1": dec += 2 ** k
        return dec
    def dec2bin(self,numero,nbit):
        numeroBin = bin(numero)[2:]
        return "0" * (nbit-len(numeroBin))+numeroBin
    def IP_dec2bin(self):
        pezzi,finale = self.ip.split("."),""
        for cella in pezzi:
            finale+= str(self.dec2bin(int(cella), 8))
        return finale
    def controllo(self):
        pezzi,ok = self.ip.split("."),True
        for cella in pezzi:
            if int(cella) > 255:
                ok = False
                break
        return ok
    def isSubnet(self):
        ok = False
        for k in range(32):
            if '1'* k + '0'* (32-k) == self.IP_dec2bin():
                ok = True
                break
        return ok

def main():
    ip = IPAddress(input("inserisci un indirizzo ip: "))
    if ip.controllo(): print("corretto")
    else: print("errato")
    if ip.isSubnet(): print("è una subnet")
    else: print("non è una subnet")

if __name__  == "__main__":
    main()