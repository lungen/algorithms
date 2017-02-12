# 3.6.4 Palindrome Checker (P. 96)

from Deque import *


def pal_checker(string):
    char_deque = Deque()
    
    for s in string:
        char_deque.add_rear(s)

    still_equal = True

    while char_deque.size() > 1 and still_equal:
        first_char = char_deque.remove_front()
        last_char = char_deque.remove_rear()

        if first_char != last_char:
            still_equal = False

    return still_equal 


print(pal_checker('radar'))
print(pal_checker('sdfsdf'))
