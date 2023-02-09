"""
Detect Pangram
https://www.codewars.com/kata/545cedaa9943f7fe7b000048/train/python
"""

# My Solution # 1
# def is_pangram(s):
#     abc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#     print(len(abc))
#     contador = 0
#     for i in abc:
#         if i in s.upper():
#             contador += 1
#     return contador == 26

# My Solution # 2
# def is_pangram(s):
#     abc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#     appears = [True for x in abc if x in s.upper()]
#     return sum(appears)==26

# Solution Codewars
# import string

# def is_pangram(s):
#     return set(string.ascii_lowercase).issubset(s.lower()) #1 

#1 Verifica si todas las letras minúsculas del alfabeto están en la cadena s 

# print((is_pangram("The quick, brown fox jumps over the lazy dog!")))
