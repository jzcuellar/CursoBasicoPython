def palindromo(palabra):
    palabra = palabra.replace(' ','') #3
    palabra = palabra.lower() #4
    palabra_invertida = palabra[::-1] #5
    if palabra == palabra_invertida:
        return True
    else:
        return False


def run(): #1 #2
    palabra = input('Escribe una palabra: ')
    es_palindromo = palindromo(palabra) 
    if es_palindromo == True:
        print('Es palindromo')
    else:
        print('No es palindromo')


if __name__ == "__main__":
    run()


#OBJETIVO PROGRAMA: Identificar si una palabra es un palindromo (Palabra o frase que se escribe igual al derecho y al reves salvo espacios)

#1 Es una buena practica en Python tener una Funcion principal, que corra el programa desde el principio (Y a partir de ahi escribir nuestro codigo)
#2 Es un estandar de comunidad en Python que la funcion sea def run(): o def main():
#3 Remplaza los espacios de la pabra o frase por Strig vacio una cadena vacia (Asi eliminamos espacios de frases)   
#4 Pasamos todas las letras a minusculas con palabra.lower() ya que para el sistema caracter minuscula es diferente a caracter Mayuscula r != R
#5 Invertimos la palabra con el slice [::-1] que cambia el orden de los caracteres, y lo asignamos a palabra_invertida


# BUENAS PRACTICAS PYTHON

# --> [Dejar dos espacios (líneas de código) entre las funciones]
# --> [Crear una función principal] Usualmente se utiliza def run(): o def main():

# --> if __name__ == "__main__":
#         run()
# """Esta linea de codigo es una buena practica es el punto de entrada de un programa de Python. 
# Una vez que se encuentra Python con esta línea de código, empieza a ejecutar todo lo qué esté abajo, 
# En este ejemplo, la función "run"."""

# IMPORTANTE Una FUNCION def function(): Siempre se debe crear encima del lugar en donde se va a invocar