"""
You're a square!
https://www.codewars.com/kata/54c27a33fb7da0db0100040e/train/python
"""

# My solution #1
import math
def is_square(n):
    return False if n<0 else int(math.sqrt(n)) == math.sqrt(n)

# Other Solution Codewars
import math
def is_square(n):
    return n > -1 and math.sqrt(n) % 1 == 0;

# print(is_square(-1))


"""
Counting sheep...
https://www.codewars.com/kata/54edbc7200b811e956000556/train/python
"""

# My solution
def count_sheeps(sheep):
    return sum([x for x in sheep if x == True])

# Clever One
def count_sheeps(sheeps):
    return sheeps.count(True)