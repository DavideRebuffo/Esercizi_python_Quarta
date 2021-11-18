x1 = float(input("inserisci x1: "))
y1 = float(input("inserisci y1: "))
x2 = float(input("inserisci x2: "))
y2 = float(input("inserisci y2: "))


punto1 = (x1,y1)
punto2 = (x1,y2)

diffX = punto2[0] - punto1[0]
diffy = punto2[1] - punto1[1]

dEuclidea = ((diffX**2) + (diffy**2))**(1/2)
print(dEuclidea)
