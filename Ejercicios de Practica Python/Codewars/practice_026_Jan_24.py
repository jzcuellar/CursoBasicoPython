"""
subtracts one list from another and returns the result.

array_diff([1,2],[1]) == [2]
array_diff([1,2,2,2,3],[2]) == [1,3]

https://www.codewars.com/kata/523f5d21c841566fde000009/python
"""

# def array_diff(a, b):
#     return [i for i in a if i not in b]

def sum_array(arr):
    if arr is None or len(arr) <= 1:
        return 0
    min_value = min(arr)
    max_value = max(arr)
    return sum(arr) - min_value - max_value

print(sum_array([6, 2, 1, 8, 10]))

l1 = [6, 2, 1, 8, 10]
l2 = []

print(min(l2))