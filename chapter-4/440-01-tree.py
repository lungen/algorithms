import turtle

t = turtle.Turtle()
my_win = turtle.Screen()
t.pensize(10)
def tree(branch_len, t):
    if branch_len > 30:
        t.forward(branch_len)
        t.right(20)
        tree(branch_len - 15, t)
        t.color('red')
        t.left(40)
        tree(branch_len - 10, t)
        t.color('blue')
        t.right(20)
        t.backward(branch_len)
tree(90, t)

my_win.exitonclick()
