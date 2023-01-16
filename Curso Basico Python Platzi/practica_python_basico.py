# # CONVERSOR DE MONEDAS ----------------------------------------------------------------------------------

# eleccion = input("""
# Bienvenido al conversor de monedas

# Que operacion quieres hacer

# 1. Convertir de Pesos a Dolares
# 2. Convertir de Dolares a Pesos

# """)

# valor_Dolar =  5000

# def conv_pes_dolar():
#     cant_pesos = float(input('Cuantos pesos colombianos tienes: '))
#     cant_dolar = round(cant_pesos/valor_Dolar,2)
#     return cant_dolar


# def conv_dolar_pes():
#     cant_dolar = float(input('Cuantos dolares tienes: '))
#     cant_pesos = round(cant_dolar*valor_Dolar,2)
#     return cant_pesos

# if eleccion == '1':
#     print(f'Tienes {conv_pes_dolar()} Dolares')
# elif eleccion == '2':
#     print(f'Tienes {conv_dolar_pes()} Pesos Colombianos')
# else:
#     print("Selecciona un valor correcto")

# CONVERSOR MONEDAS VARIOS PAISES

# def calculo_conv(tipo_mon,valor_cambio):
#     pesos = float(input(f'Cuantos pesos {tipo_mon} tienes: '))
#     print(f'Tienes {round(pesos/valor_cambio,2)} dolares')

# eleccion = input(
#     """
#     BIENVENIDO AL CONVERSOR DE MONEDAS

#     Que quieres hacer:

#     1. Convertir de Peso Colombiano a dolar.
#     2. Convertir de Peso Argentino a dolar.
#     3. Convertir de Peso Mexicano a dolar.

#     """
# )

# cop_dol=5000
# ar_dol=166.6
# mx_dol=19.31

# if eleccion == '1':
#     calculo_conv('Colombianos',cop_dol)
# elif eleccion == '2':
#     calculo_conv('Argentinos',ar_dol)
# elif eleccion == '3':
#     calculo_conv('Mexicanos',mx_dol)
# else:
#     print('Ingresa una opcion correcta por favor')


# def es_palindromo(frase):
#     frase = frase.replace(' ','').lower()
#     if frase == frase[::-1]:
#         return True
#     else:
#         return False

# def run():
#     frase_usuario = input('Escribe una palbra o frase: ')

#     if es_palindromo(frase_usuario):
#         print('Es Palindromo')
#     else:
#         print('No es Palindromo')

# if __name__ == '__main__':
#     run()

# i = 1
# while i <= 1000:
#     print(f'{}')


# def format_tel(tel):
#     tel = str(tel).replace('-','')
#     tel = tel.lstrip('0')
#     tel = tel[:4] + ' ' + tel[4:10]
#     return tel

# telefono = '0-000-103-456'

# print(format_tel(telefono))

# import re

# def extract_mail(text):
#     match = re.search(r'[\w.+-]+@[\w-]+\.[\w.-]+', text)
#     return match

# texto= 'Maxwell <maxwell_hamilton557388853@nimogy.biz> Contact Info.'

# print(extract_mail(texto))

# Buena practica dos espacios entre funciones, Todas las funciones def por encima de la Funcion principal. 

# BUCLES

# WHILE LOOP
# def run():
#     i = 0
#     while 2**i < 1000000:
#         print(f'2 Elevado a la {i} es igual a {2**i}')
#         i += 1

# if __name__ == '__main__':
#     run() 

# def run():
#     i = 0
#     while i < 10:
#         print(i)
#         i += 1

# if __name__ == '__main__':
#     run()

#FOR LOOP

# def run(): 
#     for i in range(10):
#         print(f'10 x {i} es igual a {10*i}')

# if __name__ == '__main__':
#     run()

# FOR LOOP para recorer una lista u objeto

# def run():
#     nombre = input('Cual es tu nombre: ')

#     for i in nombre:
#         print(i, end=',')

# if __name__ == '__main__':
#     run()

# def run():
#     frase = input('Escribe una frase: ')

#     for i in frase:
#         print(i.upper(), end='')

# if __name__ == '__main__':
#     run()


# INTERRUMPINEDO CICLOS CON BREAK AND CONTINUE ------------------------------------------------------------------------

# def run():
#     # EJEMPLO CONTINUE
#     # for i in range(1000): 
#     #     if i%2 != 0:
#     #         continue
#     #     print(i)

#     # i = 0
#     # while i < 20:
#     #     i += 1
#     #     if i%2 != 0:
#     #         continue
#     #     print(i)
#     # print('God Bye')        

#     # EJEMPLOS BREAK
#     # for i in range(10000):
#     #     print(i)
#     #     if i == 5658:
#     #         break

#     # i = 0
#     # while i < 20:
#     #     i += 1
#     #     if i == 12:
#     #         break
#     #     print(i)
#     # print('God Bye')        

#     # frase = input('Ingresa una frase: ')
#     # for i in frase:
#     #     if i == 'o':
#     #         break
#     #     print(i, end='')

# if __name__ == '__main__':
#     run()

# PRUEBA DE PRIMALIDAD PYTHON

# def es_primo(num):
#     contador = 0
#     for i in range(1,num+1):
#         if num%i==0:
#             contador+=1
    
#     if contador == 2:
#         return True
#     else:
#         return False

# def run():
#     numero = int(input('Escribe un numero: '))
#     if es_primo(numero):
#         print('Es un numero primo')
#     else:
#         print('No es un numero primo')

# if __name__ == '__main__':
#     run()

# # OTRA Forma Prueba Primalidad Usando Teorema de Wilson, y libreria Math

# from math import factorial

# def prueba_prim(num):
#     if factorial(num - 1) % num == -1 % num:
#         return True
#     else:
#         return False

# def run():
#     num = int(input('Escribe un numero: '))
#     if prueba_prim(num):
#         print('Es un numero primo')
#     elif num == 1:
#         print('No es un numero primo')
#     else:
#         print('No es un numero primo')

# if __name__ == '__main__':
#     run()

# JUEGO ELEGIR EL NUMERO ALEATORIO ------------------------------------------------------------------

# import random

# def instruction(num_u,num_r):
#     if num_u > num_r:
#         return 'Elige un numero menor'
#     else:
#         return 'Elige un numero mayor'

# def run():
#     # Juego para adivinar el numero        
#     lives = 10
#     num_random = random.randint(1,100)

#     while lives > 0:
#         print(f'Te quedan {lives} vidas')
#         num_user = int(input('Elige un numero del 1 al 100: '))    
#         if num_random == num_user:
#             print('!Ganaste!')
#             break
#         else:
#             lives -= 1 
#             print(f'{instruction(num_user,num_random)}')
    
#     if lives == 0:
#         print(f'Te quedaste sin vidas el numero correcto era {num_random} perdiste 😔')

# if __name__ == '__main__':
#     run()

# DICCIONARIOS  ----------------------------------------------------------------------------------------

# def run():
#     mi_diccionario = {
#         'Argentina': 44_938_712,
#         'Brasil': 210_147_125,
#         'Colombia': 50_372_424,
#     }

#     # print(mi_diccionario['Argentina'])
#     # print(mi_diccionario['Brasil'])
#     # print(mi_diccionario['Colombia'])

#     # for pais in mi_diccionario.keys(): #Acceder a llaves
#     #     print(pais)

#     # for pais in mi_diccionario.values(): #Acceder a valores
#     #     print(pais)

#     for pais, poblacion in mi_diccionario.items():
#         print(f'{pais} tiene una poblacion de {poblacion} habitantes')

# if __name__ == '__main__':
#     run()

# PROYECTO GENERADOR DE CONTRASEÑAS -----------------------------------------------------------------------------

# import random

# MAYUS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
# MINUS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
# NUMS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
# CHARS = ['*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"']

# def run():
#     total_chars = MAYUS+MINUS+NUMS+CHARS
#     len_des = int(input('Cuantos Caracteres quieres en tu contraseña: '))
#     password = []

#     while len(password) < len_des:
#         password.append(random.choice(total_chars))

#     print(f'Tu contrasena es : {"".join(map(str, password))}')
#     print(len(password))

# if __name__ == '__main__':
#     run()

# SABER SI CON LOS TRES LADOS SE PUEDE CONSTRUIR UN TRAINGULO ---------------------------------------------------------------------

# def is_triangle(a, b, c):
#     return (a+b>c) and (b+c>a) and (c+a>b)  # Desigualdades Triagulares, https://es.quora.com/C%C3%B3mo-determinar-si-es-posible-la-construcci%C3%B3n-de-un-tri%C3%A1ngulo-sabiendo-sus-lados

# print(is_triangle(7,2,2))

