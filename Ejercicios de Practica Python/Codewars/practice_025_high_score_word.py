"""
Given a string of words, you need to find the highest scoring word.
Each letter of a word scores points according to its position in the
alphabet: a = 1, b = 2, c = 3 etc.

For example, the score of abad is 8 (1 + 2 + 1 + 4).

You need to return the highest scoring word as a string.
If two words score the same, return the word that appears earliest in the original string.
All letters will be lowercase and all inputs will be valid.
"""

# My Solution
def high(x):
    words = x.lower().split()
    word_score = []
    
    for i in words:
        word_score.append(sum((ord(x)-ord('a')+1) for x in i)) #1
    
    max_score = max(word_score)
    return (words[word_score.index(max_score)])
    
#1 ord(x) returns a number with the ascii of the letter 

# Smarter Solution
def high(x):
    return max(x.split(), key=lambda k: sum(ord(c) - 96 for c in k))