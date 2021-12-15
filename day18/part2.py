# Count the one and three chain links

import re
import pprint
import copy

pp = pprint.PrettyPrinter(indent=4)

with open('input1.txt', 'r') as input:
    equations = [line.strip() for line in input.readlines()]

def splitEquation(equation):
    equation_parts = []
    for char in list(equation):
        if char == ' ':
            continue
        equation_parts.append(char)
    return equation_parts

operator_precedence = {
    '+': 1,
    '*': 0
}

def createPostfixFromInfix(equationList):
    stack = []
    postfix = []
    for part in equationList:
        if part == '(':
            stack.append(part)
        elif part in operator_precedence:
            while len(stack) and stack[-1] in operator_precedence and operator_precedence[stack[-1]] >= operator_precedence[part]:
                postfix.append(stack.pop())
            stack.append(part)
        elif part == ')':
            while stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()
        else:
            postfix.append(part)
    while len(stack):
        postfix.append(stack.pop())
    return postfix

def evaluatePostfix(postfix):
    accum = []
    for part in postfix:
        if part in operator_precedence:
            a = accum.pop()
            b = accum.pop()
            if part == '+':
                accum.append(a+b)
            elif part == '*':
                accum.append(a*b)
        else:
            accum.append(int(part))
    return accum.pop()


answers = []
for equation in equations:
    equationList = splitEquation(equation)
    postfix = createPostfixFromInfix(equationList)
    answer = evaluatePostfix(postfix)

    # print(equation)
    # print(postfix)
    print(answer)
    answers.append(answer)

print('Sum: ', sum(answers))
