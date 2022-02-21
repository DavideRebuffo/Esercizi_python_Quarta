import turtle
class Quadrato:
    def __init__(self,lato,x,y):
        self.lato,self.x,self.y = lato,x,y
    def calcolaArea(self):
        return self.lato * self.lato
    def calcolaPerimetro(self):
        return self.lato * 4
    def isInterno(self,x,y):
        return (x >= self.x & x <= (self.x+self.lato)) & (y <=self.y & y >=(self.y - self.lato))
    def disegna(self):
        penna,finestra = turtle.Turtle(),turtle.Screen()
        penna.penup()
        penna.goto(self.x,self.y)
        penna.pendown()
        for _ in range(4):
            penna.forward(self.lato)
            penna.right(90)

def main():
    quad = Quadrato(int(input("inserisci il lato del quadrato: ")),int(input("inserisci X: ")),int(input("inserisci Y: ")))
    quad.disegna()
    print(f"l' area del quadrato è di {quad.calcolaArea()}, il perimetro è di {quad.calcolaPerimetro()}")
    if quad.isInterno(int(input("inserisci X: ")),int(input("inserisci Y: "))):
        print("il punto appartiene al quadrato")
    else:
        print("il punto non appartiene al quadrato")
    finestra.exitonclick()

if __name__ == "__main__":
    main()