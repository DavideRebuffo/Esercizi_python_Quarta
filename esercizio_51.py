import turtle,random

def stella(penna,x,y,dim):
    penna.penup()
    penna.goto(x,y)
    penna.pendown()
    for _ in range(5):
        penna.forward(dim)
        penna.right(144)

def main():
    penna,finestra = turtle.Turtle(),turtle.Screen()
    penna.speed(0)
    for _ in range(50):
        stella(penna,random.randint(-turtle.screensize()[0],+turtle.screensize()[0]),random.randint(-turtle.screensize()[1],+turtle.screensize()[1]),random.randint(10,40))
    finestra.exitonclick()

if __name__ == "__main__":
    main()