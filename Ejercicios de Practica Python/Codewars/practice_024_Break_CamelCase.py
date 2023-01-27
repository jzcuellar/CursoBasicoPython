"""
Break camelCase

Complete the solution so that the function will break up camel casing,
using a space between words.

Example
"camelCasing"  =>  "camel Casing"
"identifier"   =>  "identifier"
""             =>  ""

https://www.codewars.com/kata/5208f99aee097e6552000148/python
"""


# My Solution
def solution(s):
    letters = []
    for i in s:
        if i.isupper():
            letters.append(' ')
            letters.append(i)
        else:
            letters.append(i)
    return "".join(letters)

# Clever One - Using List comprenhesions
def solution(s):
    return ''.join([' ' + i if i.isupper() else i for i in s])

# Using Regular expressions
"""
La función principal utilizada es "re.sub()" que busca un patrón en
una cadena y lo reemplaza con otro valor.

- El primer argumento de "re.sub()" es el patrón a buscar, en este caso
utiliza una expresión regular que busca cualquier caracter alfabetico
en mayuscula, es decir "[A-Z]".
- El segundo argumento es la cadena de reemplazo, en este caso 
se utiliza "r' \1'" donde \1 es una referencia al caracter que fue 
encontrado en el primer argumento, es decir, se agrega un espacio 
antes del caracter encontrado. 
- Finalmente, el tercer argumento es la cadena donde se buscara el patrón
"""
import re
def solution(s):
    return re.sub('([A-Z])', r' \1', s)
