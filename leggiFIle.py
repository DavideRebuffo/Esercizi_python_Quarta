import turtle
f = open("Istruzioni.txt","r")
righe = f.readlines()
f.close()

snow = turtle.Turtle()
finestra = turtle.Screen()
snow.speed(50)

for riga in righe:
    lista = riga.split(":")
    if lista[0] == "goto":
        valore = int(lista[1][:-1])
        if lista[0] == "forward":
            snow.forward(valore)
        elif lista[0] == "left":
            snow.left(valore)
        elif lista[0] == "right":
            snow.right(valore)
        elif lista[0] == "backward":
            snow.backward(valore)
        elif lista[0] == "penup":
            snow.penup()
        elif lista[0] == "pendown":
            snow.pendown()
    else:
        lista1 = lista[1].split(",")
        valore1 = int(lista1[0])
        valore2 = int(lista1[1])
        snow.goto(valore1,valore2)

finestra.exitonclick()