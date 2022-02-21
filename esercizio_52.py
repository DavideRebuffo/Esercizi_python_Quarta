import random,turtle
class Stella():
    def __init__(self,x,y,dim):
        self.dim = dim
        self.x = x
        self.y = y
    
    def draw(self,penna):
        penna.penup()
        penna.goto(self.x,self.y)
        penna.pendown()
        for _ in range(5):
            penna.forward(self.dim)
            penna.right(144)

def main():
    penna,finestra = turtle.Turtle(),turtle.Screen()
    penna.speed(0)
    for _ in range(50):
        stella = Stella(random.randint(-turtle.screensize()[0],+turtle.screensize()[0]),random.randint(-turtle.screensize()[1],+turtle.screensize()[1]),random.randint(10, 40))
        stella.draw(penna)
    finestra.exitonclick()

if __name__ == "__main__":
    main()