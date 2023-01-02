"""
Write a function which calculates the average of the numbers in a given list.
"""
# My Solution
# def find_average(numbers):
#     sum_lst = 0
#     for i in numbers:
#         sum_lst += i
#     return sum_lst/len(numbers) 

# My Solution 2
# def find_average(numbers):
#     return 0 if numbers == [] else sum(numbers)/len(numbers)

# Best Practice
def find_average(array):
    try:
        return sum(array) / len(array)
    except ZeroDivisionError:
        return 0

lista = [1,2,3,4]
print(find_average(lista))