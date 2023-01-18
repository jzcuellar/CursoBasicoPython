"""
Break camelCase

Complete the solution so that the function will break up camel casing,
using a space between words.

Example
"camelCasing"  =>  "camel Casing"
"identifier"   =>  "identifier"
""             =>  ""

https://www.codewars.com/kata/5208f99aee097e6552000148/python
"""



# My Solution
def solution(s):
    letters = []
    for i in s:
        if i.isupper():
            letters.append(' ')
            letters.append(i)
        else:
            letters.append(i)
    return "".join(letters)

# Clever One
def solution(s):
    return ''.join([' ' + i if i.isupper() else i for i in s])

#----------------------------------------------------------------------------------------------------
"""

"""

l1 = ['a', 'b', 'a', 'b']
l2 = ['1' if x=='a' else '2' if x=='b' else x for x in l1]

print(l2)