#!/usr/bin/env python3

import operator


operators = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
        '^': operator.pow
}

def calculate(arg):
    stack = []
    for token in arg.split():
        try:
            value = int(token)
            stack.append(value)
        except ValueError:
            function = operators[token]
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = function(arg1, arg2)
            stack.append(result)
        print(stack)
    if len(stack) != 1:
        raise TypeError('Too many parameters')
    return stack.pop()

def main():
    while True:
        result = calculate(input('rpn calc> '))
        print('Result: ', result);

if __name__ == '__main__':
    main()
