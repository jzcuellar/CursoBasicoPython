import math

def cockroach_speed(s):
    return math.floor(s*1000/36)

"""
Square sum
https://www.codewars.com/kata/515e271a311df0350d00000f/train/python
"""

def square_sum(numbers):
    return sum([x**2 for x in numbers])

"""
Basic Mathematical Operations
https://www.codewars.com/kata/57356c55867b9b7a60000bd7/train/python
"""

#My Solution
def basic_op(operator, value1, value2):
    if operator == '+':
        result = value1+value2
    elif operator == '-':
        result = value1-value2
    elif operator == '*':
        result = value1*value2
    elif operator == '/':
        result = value1/value2
    return result

#Interesting one
def basic_op(operator, value1, value2):
    return eval("{}{}{}".format(value1, operator, value2))

# function eval() -> toma una cadena de texto y la evalua como expresion, opera si el text tiene operacion.
# "{}{}{}".format(value1, operator, value2) -> convierte en una cadena de texto unica