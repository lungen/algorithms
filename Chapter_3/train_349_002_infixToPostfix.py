from Stack import *

# string = '( A + B ) * C'
# => AB + C *

def infix2postfix(string):

    prec = {}
    prec["*"] = '3'
    prec['/'] = '3'
    prec['+'] = '2'
    prec['-'] = '2'
    prec['('] = '1'

    op_stack = Stack()
    token_list = string.split()
    postfix_list = []


    for token in token_list:
        if token in 'ABCDEFG' or token in '0123456789':
            postfix_list.append(token)
        elif token == '(':
            op_stack.push(token)
        elif token == ')':
            top_token = op_stack.pop()
            while top_token != '(':
                postfix_list.append(top_token)
                top_token = op_stack.pop() 
        else:
            while (not op_stack.is_empty()) and \
                  prec[op_stack.peek()] >= prec[token]:
                postfix_list.append(op_stack.pop())
            op_stack.push(token)

    while not op_stack.is_empty():
        postfix_list.append(op_stack.pop())

    print("String: ", string, '\n' , end='')
    return ' '.join(postfix_list)

print(infix2postfix('( A + B * C ) - D'))
