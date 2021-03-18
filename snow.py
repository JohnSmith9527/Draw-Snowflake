import turtle,random
turtle.mode("logo")
turtle.shape("turtle")

turtle.bgcolor("black")
turtle.speed(0)

turtle.pencolor("white")

size=10

for k in range(40):
    x = random.randint(-400,400)
    y = random.randint(-400,400)
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    for j in range(10):
        for i in range(0,2,1):
            turtle.forward(size)
            turtle.left(60)
            turtle.forward(size)
            turtle.left(120)
        turtle.left(36)

turtle.hideturtle()

