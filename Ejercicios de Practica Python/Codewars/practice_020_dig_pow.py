"""
Given a positive integer n written as abcd... (a, b, c, d... being digits) 
and a positive integer p

we want to find a positive integer k, if it exists, such that the sum of the digits
of n taken to the successive powers of p is equal to k * n.

In other words:

Is there an integer k such as : (a ^ p + b ^ (p+1) + c ^(p+2) + d ^ (p+3) + ...) = n * k

If it is the case we will return k, if not return -1.

Note: n and p will always be given as strictly positive integers.

https://www.codewars.com/kata/5552101f47fc5178b1000050/python
"""

# My Solucion # 1
# def dig_pow(n, p):
#     dig = [int(x) for x in str(n)]
#     potencias = []
    
#     for i in dig:
#         potencias.append(i**p)
#         p += 1
    
#     if sum(potencias) % n == 0:
#         return sum(potencias)/n
#     else:
#         return -1

# print(dig_pow(46288, 3))