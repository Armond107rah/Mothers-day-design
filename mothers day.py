import math
import turtle

turtle.shape("turtle")
turtle.setup(width=900, height=700)
turtle.speed(0)
turtle.bgcolor('black')
turtle.color('red')


def heart1(h):
    return 15 * math.sin(h) ** 3


def heart2(h):
    return 12 * math.cos(h) - 5 * math.cos(2 * h) - 2 * math.cos(3 * h) - math.cos(3 * h) - math.cos(4 * h)


for i in range(400):
    x, y = heart1(i) * 20, heart2(i) * 20
    turtle.goto(x, y)

turtle.color('purple')
turtle.penup()
turtle.goto(0, -24)
turtle.pendown()
turtle.write("Happy Mother's Day!", align='center', font=('Arial', 25, 'bold'))
turtle.color('blue')
turtle.goto(0, -50)
turtle.write("This is how you do a CI/CD Pipeline on AWS!",
             align='center', font=('Arial', 25, 'bold'))


turtle.done()
