# 3.4.5 Convertign Decimal Numbers to Binary Numbers

from Stack import *


def divide_by_2(dec_number):

    rem_stack = Stack()

    while dec_number > 0:
        n = dec_number % 2
        rem_stack.push(n)
        dec_number = dec_number // 2

    bin_string = ''
    while not rem_stack.is_empty():
        bin_string = bin_string + str(rem_stack.pop())

    return bin_string

print(divide_by_2(233))
