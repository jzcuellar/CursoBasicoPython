"""
You are asked to square every digit of a number and concatenate them.
For example, if we run 9119 through the function, 811181 will come out, 
because 92 is 81 and 12 is 1.

Note: The function accepts an integer and returns an integer
"""
# My 1st Solution
# def square_digits(num):
#     result = ''
#     for i in str(num):
#         result += str(int(i)**2)
#     return int(result)

# My 2nd Solution
# def square_digits(num):
#     sq_ev_dg = [int(x)**2 for x in str(num)] # Using List comprehensions 
#     return int(''.join(map(str, sq_ev_dg))) # Function map passes a function for each element in a list

# My 3rd Solution
# def square_digits(num):
#     sq_ev_dg = map(lambda x: int(x)**2, str(num)) #Using lambda
#     return  int(''.join(map(str, sq_ev_dg)))

# print(square_digits(9119))



