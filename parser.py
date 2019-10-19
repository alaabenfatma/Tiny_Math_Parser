# Written by Alaa Ben Fatma 2019
import sys

# EXPRESSION
exp = []
index = 0

# Get the current value of the expression


def currentToken():
    return exp[0]

# Jump to the next element of the expression


def next():
    if(len(exp) > 1):
        exp.remove(exp[0])


# Definitions
PLUS = '+'
MINUS = '-'
MULT = '*'
DIV = '/'
OB = '('
CB = ')'

# Return a number if the value of the token is numeric, check for brackets otherwise.


def factor(res):
    if(str.isnumeric(currentToken())):
        res = (float)(currentToken())
        next()
        return res
    elif(currentToken() == OB):
        next()
        res = parse(res)
        next()
        return res
    else:
        return res
    pass

# Perform multiplication & division for them being the operators with the highest priority


def high_priority_terms(res):
    if(currentToken() == MULT):
        next()
        x = high_priority_terms(res)
        y = factor(res)
        res = x*y
    elif(currentToken() == DIV):
        next()
        x = high_priority_terms(res)
        y = factor(res)
        res = x/y
    return res

# Trigger the function above


def high_prio_terms_trigger(res):
    res = factor(res)
    return high_priority_terms(res)

# Perform addition & subtraction for them being the operators with the highest priority


def low_priority_terms(res):
    if(currentToken() == PLUS):
        next()
        res = high_prio_terms_trigger(res) + low_priority_terms(res)
    elif(currentToken() == MINUS):
        next()
        res = low_priority_terms(res) - high_prio_terms_trigger(res)
    return res

# Trigger the function above


def low_priority_terms_trigger(res):
    res = high_prio_terms_trigger(res)
    return low_priority_terms(res)

# Parse the equation


def parse(res):
    return low_priority_terms_trigger(res)


# Main ? (I know that you are laughing, C fans).
exp = sys.argv[1].split(' ')
print(parse(0.0))
