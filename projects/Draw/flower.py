from turtle import Turtle, Screen

screen = Screen()
screen.bgcolor('#333')


def draw_petal(turtle, radius):
    heading = turtle.heading()
    turtle.color('#b56969')
    turtle.speed(10)
    turtle.circle(radius, 60)
    turtle.left(120)
    turtle.circle(radius, 60)
    turtle.setheading(heading)


my_radius = 200
my_petals = 20

bob = Turtle()

for _ in range(my_petals):
    draw_petal(bob, my_radius)
    bob.left(360 / my_petals)
bob.right(90)
bob.forward(500)
bob.hideturtle()


screen.exitonclick()


