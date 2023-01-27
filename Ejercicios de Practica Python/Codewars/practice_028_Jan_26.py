"""
Find the stray number
https://www.codewars.com/kata/57f609022f4d534f05000024/train/python
"""

# My Solution
# def stray(arr):
#     unique_values = set(arr)
#     for i in unique_values:
#         if arr.count(i) == 1:
#             return i

#Smarter Solution
# def stray(arr):
#     return min(arr, key=arr.count)

# print(stray([3, 2, 2, 2, 2]))

"""
Even or Odd
https://www.codewars.com/kata/53da3dbb4a5168369a0000fe/train/python
"""

# def even_or_odd(number):
#     return 'Even' if number%2 == 0 else 'Odd'

"""
Delete occurrences of an element if it occurs more than n times
https://www.codewars.com/kata/554ca54ffa7d91b236000023/train/python
"""

# Solution from Chat GPT
# def delete_nth(order,max_e):
#     count = {}
#     i = 0
#     while i < len(order):
#         if count.get(order[i], 0) >= max_e:
#             order.pop(i)
#         else:
#             count[order[i]] = count.get(order[i], 0) + 1
#             i += 1
#     return order

# Smarter Answer
def delete_nth(order,max_e):
    ans = []
    for i in order:
        if ans.count(i) < max_e: ans.append(i)
    return ans

print(delete_nth([2, 6, 2, 18, 6, 18, 18, 6, 18, 18, 18, 18, 2, 2, 2, 2, 2, 2, 6, 18, 18, 6, 6, 6, 18, 6, 18, 2], 3))

