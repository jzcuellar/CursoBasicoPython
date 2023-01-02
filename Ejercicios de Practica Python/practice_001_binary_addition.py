"""
Implement a function that adds two numbers together and returns their sum in binary. The conversion can be done before, or after the addition.
The binary number returned should be a string.
"""
# 
# MY SOLUTION ONLY WORKS WITH ENTEROS

# def add_binary(a,b):
#     import math
#     num = a+b
#     binary = ''
    
#     while num > 0:
#         binary += str(num%2)
#         num = math.floor(num/2)
#     return binary[::-1]


# print(add_binary(6,6))

def add_binary(a,b):
    return bin(a+b)[2:]

print(add_binary(6,6))