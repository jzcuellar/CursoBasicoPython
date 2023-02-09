"""
Sort the odd
https://www.codewars.com/kata/578aa45ee9fd15ff4600090d/python
"""

#My solution #1
def sort_array(source_array):
    final_list = sorted([x for x in source_array if x%2!=0])
    for i in range(len(source_array)):
        if source_array[i] % 2 == 0:
            final_list.insert(i,source_array[i])
    return final_list

#Solution #2 CodeWars 
def sort_array(source_array):
    odds = sorted((x for x in source_array if x%2 != 0), reverse=True)
    return [x if x%2==0 else odds.pop() for x in source_array]

print(sort_array([5, 3, 2, 8, 1, 4]))

