import turtle

def r_color():
    import random
    colors = {1:"red", 2:"blue", 3:"green", 4:"black", 5:"orange", 6:"yellow"}
    r = random.randint(1, 6)
    return colors[r]

def tree(branch, t):

    t.speed(1)
    t.pensize(10)


    if branch > 10:
        #t.color(r_color())
        t.color('green')
        t.forward(branch)
        t.right(20)
        t.color('blue')
        tree(branch - 20, t)
        t.left(40)
        tree(branch - 20, t)
        t.right(20)
        t.color('yellow')
        t.backward(branch)


def main():

    t = turtle.Turtle()
    my_win = turtle.Screen()
    tree(80, t)
    my_win.exitonclick()

main()
