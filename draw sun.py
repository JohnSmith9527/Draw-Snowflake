import turtle

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
