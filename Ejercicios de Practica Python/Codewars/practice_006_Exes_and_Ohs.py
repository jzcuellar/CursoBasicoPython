##  Mi Solucion Jefferzon

def xo(s):
    letter_x = 0
    letter_o = 0

    for i in s:
        if i.upper() == 'X':
            letter_x += 1
        if i.upper() == 'O':
            letter_o += 1
    
    return letter_o == letter_x

##  Solucion interesante

def xo(s):
    return s.lower().count('x') == s.lower().count('o')