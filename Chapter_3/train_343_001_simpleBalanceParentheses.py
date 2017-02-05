from Stack import *


def par_checker(string):
    s = Stack()
    balanced = True
    index = 0

    while index < len(string) and balanced:
        if string[index] == '(':
            s.push(string[index])
        elif s.is_empty():
                balanced = False
        else:
            s.pop()

        index += 1

    if s.is_empty() and balanced:
        return True
    else:
        return False


#print(par_checker('(())'))
#print(par_checker('(()'))
print(par_checker(')'))

