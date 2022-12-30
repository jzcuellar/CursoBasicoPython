"""
You are provided with a list (or array) of integer pairs.
Elements of each pair represent number of people get into bus (The first item)
and number of people get off the bus (The second item) in a bus stop.

https://www.codewars.com/kata/5648b12ce68d9daa6b000099/python

"""

# MY SOLUTION
# def number(bus_stops):
#     persons = 0
#     for i in bus_stops:
#         persons += i[0]
#         persons -= i[1]
#     return persons

#Clever One
# def number(bus_stops):  
#     return sum([stop[0] - stop[1] for stop in bus_stops]) #Using list comprehensions, y despues funcion suma

# Another Clever One
# def number(stops):
#     return sum(ing - out for ing, out in stops)

# lista = [[10,0],[3,5],[5,8]]
# number(lista)


# Categorize New Member ------------------------------------------------------------------------------------------------------------------

"""
To be a senior, a member must be at least 55 years old and have a handicap greater than 7.
In this croquet club, handicaps range from -2 to +26; the better the player the lower the handicap.

EXAMPLE
input =  [[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]
output = ["Open", "Open", "Senior", "Open", "Open", "Senior"]

https://www.codewars.com/kata/5502c9e7b3216ec63c0001aa/solutions/python
"""

# My Solution #1
# def open_or_senior(data):
#     out_lst = []
#     for info in data:
#         if info[0]>=55 and info[1]>7:
#             out_lst.append('Senior')
#         else:
#             out_lst.append('Open')
#     return out_lst

# Smartest Solution using List comprehensions
# def open_or_senior(data):
#     return ["Senior" if age >= 55 and handicap >= 8 else "Open" for (age, handicap) in data]

# Other Way using list comprenhesions
# def open_or_senior(members):
#     return ["Senior" if info[0]>54 and info[1]>7 else "Open" for info in members]

# input =  [[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]
# print(open_or_senior(input))