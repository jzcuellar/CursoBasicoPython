"""
Take a Number And Sum Its Digits Raised To The Consecutive Powers And ....¡Eureka!!
https://www.codewars.com/kata/5626b561280a42ecc50000d1/train/python
"""

def sum_dig_pow(a, b): 
    numbers = [str(x) for x in range(a,b+1)]
    eureka_list = []

    for num in numbers:
        if sum([int(num[x])**(int(x)+1) for x in range(len(num))]) == int(num):
            eureka_list.append(int(num))
        
    return eureka_list

print(sum_dig_pow(1,10000))