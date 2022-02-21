import turtle

nLati = int(input("inserisci il numero di lati: "))

poligono = turtle.Turtle()
finestra = turtle.Screen()

for _ in range(nLati):
    poligono.forward(50)
    poligono.left(360/nLati)

finestra.exitonclick()