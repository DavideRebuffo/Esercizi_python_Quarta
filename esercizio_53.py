def bin2dec(stringa):
    dec = 0
    for k,carattere in enumerate(stringa[::-1]):
        if carattere == "1":
            dec += 2 ** k
    return dec

def dec2bin(numero,nbit):
    numeroBin = bin(numero)[2:]
    return "0" * (nbit-len(numeroBin))+numeroBin

def IP_dec2bin(stringa):
    pezzi,finale = stringa.split("."),""
    for cella in pezzi:
        finale+= str(dec2bin(int(cella), 8))
    return finale

def IP_bin2dec(stringa):
    finale = ""
    for num in range(0,32,8):
        finale+= str(bin2dec(stringa[num:num + 8])) + "."
    return finale[:-1]

def main():     
    print(IP_dec2bin("192.168.10.0"))
    print(IP_bin2dec("11000000101010000000101000000001")) #/24 32-24 = 8 2**8-2 254
    

if __name__ == "__main__":
    main()