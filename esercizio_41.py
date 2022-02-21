import turtle
griglia,finestra,x,y,passo,nQuadrati = turtle.Turtle(),turtle.Screen(),0,0,50,4
for conta in range(1,(nQuadrati+1)*2+1):
    griglia.goto(passo*x,passo*y)
    griglia.pendown()
    griglia.forward(passo*nQuadrati)
    griglia.penup()
    if conta <nQuadrati+1:
        y-=1
    elif conta == nQuadrati+1:
        y = 0
        griglia.right(90)
    else:
        x+=1
finestra.exitonclick()