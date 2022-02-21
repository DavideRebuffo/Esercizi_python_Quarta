import turtle

poligono1 = turtle.Turtle()
poligono2 = turtle.Turtle()
finestra = turtle.Screen()

n = int(input("inserisci un numero intero: "))
lista = [poligono1,poligono2]
cambio = 0
for k in range(n*2):
    if k == n:
        cambio+=1
        lista[cambio].right(180)
    lista[cambio].forward(50)
    lista[cambio].right(360/n)

finestra.exitonclick()