import random

lanciAlice = [random.randint(1, 6) for _ in range(10)]
lanciBob = [random.randint(1, 6) for _ in range(10)]

f = open("c:/Users/Client/Desktop/SHULKER BOX/SCUOLA/4a/SISTEMI E RETI/TEORIA/PYTHON/lanciDadi.txt","w")
for k in range(10):
    f.write(f"{lanciAlice[k]}, {lanciBob[k]}\n")
f.close()