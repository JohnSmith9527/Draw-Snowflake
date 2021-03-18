import turtle,random
turtle.mode("logo")
turtle.shape("turtle")

turtle.bgcolor("black")
turtle.speed(0)

#draw the sun
turtle.speed(0)
turtle.pencolor("red")

size_of_sun=10
sun_x = 0
sun_y = 300

for j in range(12):
    turtle.penup()
    turtle.goto(sun_x,sun_y)
    turtle.pendown()
    for i in range(3):
        turtle.circle(size_of_sun,180)
        turtle.right(180)
    turtle.right(30)

# end of drawing the sun



turtle.colormode(255)

red = random.randint(0,255)
green = random.randint(0,255)
blue = random.randint(0,255)
turtle.pencolor(red,green,blue)

size=10

for k in range(10):
    x = random.randint(-400,400)
    y = random.randint(-400,400)
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    for j in range(10):
        for i in range(0,2,1):
            red = random.randint(230,255)
            green = random.randint(150,200)
            blue = random.randint(10,60)
            turtle.pencolor(red,green,blue)
            
            turtle.forward(size)
            turtle.left(60)
            turtle.forward(size)
            turtle.left(120)
        turtle.left(36)

turtle.hideturtle()

