from Stack import *

# completed extended par_checker for {, [, (, ), ], }

def matches(open, close):
    opens = '([{'
    closes = ')]}'

    return opens.index(open) == closes.index(close)

def par_checker(symbolString):


    s = Stack()
    balanced = True
    index = 0

    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in '{[(':
            s.push(symbol)
        else:
            if s.is_empty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    balanced = False
        index = index + 1

    if s.is_empty() and balanced: 
        return True
    else: 
        return False

#print(par_checker('([{}])'))
print(par_checker('('))

