"""
Complete the function that accepts a string parameter, 
and reverses each word in the string. All spaces in the
string should be retained.

"This is an example!" ==> "sihT si na !elpmaxe"
"double  spaces"      ==> "elbuod  secaps"

"""

# MI SOLUCION

def reverse_words(text):
    words_list = [i for i in text.split(' ')]
    reverse_words_list = [i[::-1] for i in words_list]
    return ' '.join(reverse_words_list)

print(reverse_words("double  spaces"))

# SOLUCION INTERESANTES

def reverse_words(str):
    return ' '.join(s[::-1] for s in str.split(' ')) 