import turtle, random

t = turtle.Turtle()
my_win = turtle.Screen()

def draw(line, t):
    if line > 5:
        t.forward(line)
        t.left(90)
        draw(line - 10, t)

draw(100, t)
my_win.exitonclick()

