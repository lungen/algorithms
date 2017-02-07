"""
Assume the postfix expression is a string of token delimited by spaces. The
operators are *, /, +, and -, and the operands are assumed to be single-digit
integer values. The output will be an integer result.
    
    1. Create an empty stack called operand_stack

    2. Convert the string to a list by using the string mehtod split.

    3. Scan the token list from left to right.

        - If the token is an operand, convert it from a string to an integer 
        and push the value onto the operand_stack.

        - If the token is an operator it will need to operands. Pop the 
        operand_stack twice. The first pop is the second operand and the second
        pop the first operand. Perform the arithmetic operation. Push the result
        back on the operand_stack.

    4. When the input expression has been completely processed, the result is 
    on the stack. Pop the operand_stack and return the value.

To assist with the arithmetic, a helper function do_math is definded that 
will take two operands and an operator and then perform the proper 
arithmetic operation.
"""

from Stack import *


# string: 456*+      string: 78+32+/

def postfixEvaluation(string='4 5 6 * +'):

    def do_math(op, op1, op2):
        if op == '*': return op1 * op2
        elif op == '/': return op1 / op2
        elif op == '+': return op1 + op2
        elif op == '-': return op1 - op2
        else: print("FAIL OPERAND")


    operand_stack = Stack()  # ad 1.
    token_list = string.split()  # ad 2.

    for token in token_list:  # ad 3.
        if token in '0123456789':
            operand_stack.push(int(token))
        elif token in '*/+-':
            b, a = operand_stack.pop(), operand_stack.pop()
            operand_stack.push(do_math(token, a, b))
        else:
            print("Wrong Statemant (ignoring): ", token)
    
    return operand_stack.pop()


print(postfixEvaluation('7 8 + % 3 2 + /'))
