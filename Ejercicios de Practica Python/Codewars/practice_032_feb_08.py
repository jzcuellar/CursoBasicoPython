"""
Vowel Count
https://www.codewars.com/kata/54ff3102c1bad923760001f3/train/python
"""

# My Solution #1
def get_count(sentence):
    vowels = ['a','e','i','o','u']
    return len([x for x in sentence.lower() if x in vowels])

# Other solution Codewars
def get_count(sentence):
    return len([x for x in sentence.lower() if x in 'aeoiu'])

print(get_count("aeiou"))

"""
Keep up the hoop
https://www.codewars.com/kata/55cb632c1a5d7b3ad0000145/train/python
"""

def hoop_count(n):
    return "Great, now move on to tricks" if n>=10 else "Keep at it until you get it"