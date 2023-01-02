# https://www.codewars.com/kata/54ba84be607a92aa900000f1/train/python

"""
An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

isIsogram "Dermatoglyphics" = true
isIsogram "moose" = false
isIsogram "aba" = false

"""

# MI SOLUCION

# def is_isogram(string):
#     contador = 0
#     string = string.lower()
    
#     for i in range(len(string)):
#         for j in range(len(string)):
#             if string[i] == string[j]:
#                 contador += 1
    
#     if contador > len(string):
#         return False
#     else:
#         return True

# print(is_isogram('isIsogram'))

# SOLUCIONES INTERESANTES

# def is_isogram(string):
#     return len(string) == len(set(string.lower())) # Set transforma el string en una estructura de datos en donde caracteres no se repiten

# def is_isogram(string):
#     string = string.lower()
#     for letter in string:
#         if string.count(letter) > 1: return False  # string.count(letter) Cuenta las veces que x caracter aparece en el str
#     return True

