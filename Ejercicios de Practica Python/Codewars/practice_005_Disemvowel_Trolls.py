def disemvowel(string_):    
    vowels=['a','e','i','o','u']
    for i in len(string_):
        string_.replace(vowels[1],'')
    return string_


string_='This website is for losers LOL'
print(disemvowel(string_))
