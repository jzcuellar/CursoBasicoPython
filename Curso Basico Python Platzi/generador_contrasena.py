import random

def generar_contrasena():
    mayus = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
    minus = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    simb = ['*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"']

    charact=mayus+minus+nums+simb # Concateno todas las litas en una lista llamada charact

    contrasena = [] #Creo una lista vacia para almacenar caracteres de mi contrasena

    for i in range(15): #15 Vueltas del ciclo for para crear una contrasena de 15 caracteres, 'seguridad suficiente'
        caracter_random = random.choice(charact) #choice es una funcion especial del modulo random que me permite escoger un caracter al azar
        contrasena.append(caracter_random)
        
    contrasena = ''.join(contrasena) #''.join(lista) sirve para convertir una lista a string
    return contrasena

def run():
    contrasena = generar_contrasena()
    print(f'Tu nueva contraseña es: {contrasena}')


if __name__ == '__main__':
    run()