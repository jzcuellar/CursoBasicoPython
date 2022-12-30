"""
Given a string of digits, you should replace any digit below 5 with '0'
and any digit 5 and above with '1'. Return the resulting string.

https://www.codewars.com/kata/57eae65a4321032ce000002d/python
"""

# My Solution
# def fake_bin(x):
#     for i in range(5):
#         x = x.replace(str(i),'0')
#     for i in range(5,10):
#         x = x.replace(str(i),'1')
#     return x

# Clever One
# def fake_bin(x):
#     return ''.join('0' if dig < '5' else '1' for dig in x)

# print(fake_bin('45385593107843568'))

# --------------------------- Otros ejercios

# def paperwork(n, m):
#     return 0 if n < 0 or m < 0 else n*m

# def printer_error(s):
#     cadena = [i for i in s]
#     errors = [chr(i) for i in range(110,123)]
    
#     cant_err = 0
#     for i in cadena:
#         if i in errors:
#             cant_err +=1
    
#     return (f'{cant_err}/{len(cadena)}') 

# s = "aaabbbbhaijjjm"
# print(printer_error(s))


