# My solution
# def solution(string, ending):
#     if string[(len(string)-len(ending)):(len(string))] == ending:
#         return True
#     else:
#         return False

# Clever solutions
def solution(string, ending):
    return string.endswith(ending) # endswith() Compare if a String ends with a value

print(solution('abcde','')) # ---> returns True
print(solution('abc', 'bc')) # ---> returns True
solution('abc', 'd') # ---> returns False