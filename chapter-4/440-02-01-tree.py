import turtle

def r_color():
    import random
    colors = {1:"red", 2:"blue", 3:"green", 4:"grey", 5:"orange", 6:"yellow", 7:"brown"}
    r = random.randint(1, 7)
    return colors[r]

def tree(branch, t):

    #t.speed(1)
    t.pensize(10)

    if branch > 15:
        t.color(r_color())
        t.forward(branch)
        t.right(20)
        tree(branch - 15, t)
        t.left(40)
        tree(branch - 15, t)
        t.right(20)
        t.backward(branch)


def main():

    t = turtle.Turtle()
    my_win = turtle.Screen()
    t.speed(100)
    t.left(90)
    t.up()
    t.backward(200)
    t.down()
    t.color('green')
    tree(75, t)


    my_win.exitonclick()

main()
