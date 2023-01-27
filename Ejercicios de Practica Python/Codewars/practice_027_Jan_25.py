"""
You only need one - Beginner

https://www.codewars.com/kata/57cc975ed542d3148f00015b/train/python

"""
# Solution #1
def check(seq, elem):
    return True if elem in seq else False

# Solution #2
# def check(seq, elem):
#     return elem in seq

# def greet():
#     return "hello world!"

"""
Double Char
https://www.codewars.com/kata/56b1f01c247c01db92000076/python
"""

# def double_char(s):
#     return ''.join([x+x for x in s])

# print(double_char("String"))

"""
Convert a string to an array
https://www.codewars.com/kata/57e76bc428d6fbc2d500036d/train/python
"""

# Solution #1
# def string_to_array(s):
#     return [""] if s== '' else s.split()

# # Solution #2
# def string_to_array(s):
#     return s.split(' ')

# print(string_to_array(""))

import numpy as np

A = np.array([[2, 4], [-1, 2]])
Ainversa = np.linalg.inv(A)

print(Ainversa)

print(np.matmul(A, Ainversa))
