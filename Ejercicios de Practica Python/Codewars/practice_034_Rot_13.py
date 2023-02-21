"""
Rot13
https://www.codewars.com/kata/530e15517bc88ac656000716/python
"""

def rot13(message):
    abc = [chr(i) for i in range(ord('a'), ord('z')+1)]*2 +  [chr(i) for i in range(ord('A'), ord('Z')+1)]*2  #1
    new_message = []
    for i in message:
        if i in abc:
            new_message.append(abc[abc.index(i)+13])
        else:
            new_message.append(i)
    
    return ''.join(new_message)

print(rot13('test'))

#1  Generates a List where Abc lower case is repeated twice and abc uppercase is repeated twice
#   Este código utiliza la función ord para obtener el valor numérico de los caracteres "a" y "z",
#   y "A" y "Z", y luego genera una lista que contiene todos los caracteres en este rango, 
#   utilizando la función chr para convertir los valores numéricos en caracteres.