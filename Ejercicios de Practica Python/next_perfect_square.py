"""
Complete the findNextSquare method that finds the next integral perfect square after the one passed as a parameter. 
Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.

If the parameter is itself not a perfect square then -1 should be returned. You may assume the parameter is non-negative.

121 --> 144
625 --> 676
114 --> -1 since 114 is not a perfect square

"""

# Mi Solution
# def find_next_square(sq):
#     if sq**(1/2) - round(sq**(1/2)) == 0:
#         return (sq**(1/2) + 1) ** 2  
#     else:
#         return -1

# Best practices
# def find_next_square(sq):
#     root = sq ** 0.5
#     if root.is_integer(): # is_integer() Validates 
#         return (root + 1)**2
#     return -1

# print(find_next_square(122))

