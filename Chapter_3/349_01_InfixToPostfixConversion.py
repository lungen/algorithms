"""
1. Create an empty stack called op_stack for keeping operators. Create an empty list for
output.
2. Convert the input infix string to a list by using the string method split.
3. Scan the token list from left to right.
• If the token is an operand, append it to the end of the output list.
• If the token is a left parenthesis, push it on the op_stack.
• If the token is a right parenthesis, pop the op_stack until the corresponding left
parenthesis is removed. Append each operator to the end of the output list.
• If the token is an operator, *, /, +, or −, push it on the op_stack. However, first
remove any operators already on the op_stack that have higher or equal precedence
and append them to the output list.
When the input expression has been completely processed, check the op_stack. Any
operators still on the stack can be removed and appended to the end of the output list.
"""

from Stack import *


def infix_to_postfix(string):
    op_stack = Stack()
    postfix_list = []
    token_string = string.split()

    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1

    for token in token_string:
        if token in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' or token in '0123456789':
            postfix_list.append(token)
        elif token == '(':
            op_stack.push(token)
        elif token == ')':
            top_token = op_stack.pop()
            while top_token != '(':
                postfix_list.append(top_token)
                top_token = op_stack.pop()
        else:
            while (not op_stack.is_empty()) and (prec[op_stack.peek()] >= prec[token]):
                postfix_list.append(op_stack.pop())
            op_stack.push(token)

    while not op_stack.is_empty():
        postfix_list.append(op_stack.pop())
    print("String: ", string, "\nConverion: ", end='')
    return " ".join(postfix_list)

#print(infix_to_postfix("( A + B ) * ( C + D )"))
print(infix_to_postfix("( A + B ) * C"))
