from Stack import *


def toStr(nr, base):

    conv_str = '0123456789ABCDEF'
    r_stack = Stack()

    while nr > 0:
        if nr < base:
            r_stack.push(conv_str[nr])
        else:
            r_stack.push(conv_str[(nr % base)])
        nr = nr // base

    res = ''
    while not r_stack.is_empty():
        res += r_stack.pop()
    return res

print(toStr(173, 10))


