"""
Abbreviate a Two Word Name
https://www.codewars.com/kata/57eadb7ecd143f4c9c0000a3/python
"""

# My Solution #1
# def abbrev_name(name):
#     l1 = name.upper().split()
#     l2 = [x[0] for x in l1]
#     return '.'.join(l2)

# One line solution mala praxis. My Solution #2
# def abbrev_name(name):
#     return '.'.join([x[0] for x in name.upper().split()])    

# print(abbrev_name("Sam Harris"))


"""
Will you make it?
https://www.codewars.com/kata/5861d28f124b35723e00005e/train/python
"""

def zero_fuel(distance_to_pump, mpg, fuel_left):
    return mpg*fuel_left >= distance_to_pump