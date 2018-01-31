import turtle
import random
# nice color palette  #22264b  #b56969   #e6cf8b   #e8edf3
# "arrow","turtle","circle","square","triangle","classic"
# "fastest",  # 0"fast",    # 10 "normal",  # 6 "slow",    # 3 "slowest"  # 1
colors = ["#b56969" ,"#e6cf8b","#e8edf3"]


# turtle.setup(width=600, height=500)
# turtle.reset()
# turtle.hideturtle()

def canvas(color):
    win = turtle.Screen()
    win.bgcolor(color)
    return win


def squareDraw(size,deg=90):
    for i in range(4):
        square.forward(size)
        square.right(deg)



def circle(size,color,tshape="classic",speed='6'):
    circle = turtle.Turtle()
    circle.color(color)
    circle.circle(size)
    circle.speed(speed)


def draw_triangle(triangle):
    for i in range(2):
        triangle.forward(100)
        triangle.left(120)
    triangle.forward(100)
    triangle.left(180)



win = canvas('#22264b')

square = turtle.Turtle()
square.shape('classic')
square.color(colors[0])
square.speed(0)
for i in range(360):
    deg = 90
    newcolor = colors[random.randint(0, 2)]
    newcolor = colors[0]
    squareDraw(200, deg)
    square.right(7)
    
    circle = turtle.Turtle()
    circle.color("#e6cf8b")
    circle.circle(90)
    circle.speed(0)
    circle.left(50)

win.exitonclick()
