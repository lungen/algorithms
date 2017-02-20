import turtle
import canvasvg
import random
from Stack import *

def r_color():
    colors = {1:"red", 2:"blue", 3:"green", 4:"grey", 5:"orange", 6:"yellow", 7:"brown"}
    r = random.randint(1, 7)
    return colors[r]

def g_color():
    # grey colors
    st = Stack()
    grey_list = ('#080808', '#020202', '#404040', '#050505', '#707070', '#909090', '#A0A0A0', '#D0D0D0', '#F0F0F0')

    for c in reversed(grey_list):
        st.push(c)

    return st

def tree(branch, pensize, color, t):

    #t.speed(1)
    t.pensize(pensize)
    t.pencolor(color)
    angle = random.randint(10, 45)
    sub = random.randint(3, 21)

    if branch > 1:
        t.forward(branch)
        t.right(angle)
        tree(branch - sub, pensize * 0.8, color, t)
        t.left(2 * angle)
        tree(branch - sub, pensize * 0.8, color, t)
        t.right(angle)
        t.backward(branch)
        #t.circle(sub)
        t.color(r_color())
        t.stamp()


def main():

    t = turtle.Turtle()
    my_win = turtle.Screen()
    my_win.bgcolor('#000000')
    #my_win.delay(100)
    t.speed(100)
    color_st = g_color()

    t.left(90)
    t.up()
    t.backward(350)
    t.down()
    for i in range(75, 150, 30):
        color = r_color()
        tree(i, 10, color, t)
    pic = t.getscreen().getcanvas()
    canvasvg.saveall('trees3.svg', pic)

    my_win.exitonclick()

main()
