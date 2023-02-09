"""
Count characters in your string
https://www.codewars.com/kata/52efefcbcdf57161d4000091/train/python
"""

# My solution #1
# def count(string):
#     dictionary = {}
#     for i in string:
#         dictionary[i] = string.count(i)
#     return dictionary

# My solution # 2 Using dictionary comprehensions
# def count(string):
#     return {letter: string.count(letter) for letter in string} 

# print(count('aba'))

"""
Testing 1-2-3
https://www.codewars.com/kata/54bf85e3d5b56c7a05000cf9/train/python
"""

# My solution #1 
def number(lines):
    list1 = []
    x = 0
    for i in lines:
        list1.append(f'{x+1}: {i}')
        x+=1
    return list1

# My solution #2
def number(lines):
    return [f'{i+1}: {lines[i]}' for i in range(len(lines))]



print(number(["a", "b", "c"]))