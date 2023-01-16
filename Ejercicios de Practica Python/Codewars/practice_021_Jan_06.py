""""
Regex validate PIN code

ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot
contain anything but exactly 4 digits or exactly 6 digits.

If the function is passed a valid PIN string, return true, 
else return false.

https://www.codewars.com/kata/55f8a9c06c018a0d6e000132
"""

# My solution
def validate_pin(pin):
    return pin.isdigit() and (len(pin) == 4 or len(pin) == 6)

# Interesant One
def validate_pin(pin):
    return len(pin) in (4, 6) and pin.isdigit()

# -------------------------------------------------------------------

"""
Grasshopper - Summation

Write a program that finds the summation of every number from 1 to num.
The number will always be a positive integer greater than 0.

"""
def summation(num):
    return sum(x for x in range(1,num+1))