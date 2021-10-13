import random #1

def run():
    numero_aleatorio = random.randint(1, 100) #2 #3
    numero_elegido = int(input('Elige un numero del 1 al 100: '))
    numero_vidas = 10
    
    
    while numero_elegido != numero_aleatorio and numero_vidas > 0:
        numero_vidas -= 1
        print('Tienes ' + str(numero_vidas) + ' intentos')
        if numero_elegido < numero_aleatorio:
            print('Busca un numero mas grande')
        else:
            print('Busca un numero mas pequeño')
        numero_elegido = int(input('Elige Otro numero: '))
    
    
    if numero_vidas == 0:
        print('Perdiste!')
    else:
        print('Ganaste!')
     


if __name__ == "__main__":
    run()

#1 ramdom es un modulo de python (Paquete de funciones, clases y variables desarrollado por los credares de python) para generar numero aleatorios 
#2 Para acceder a funciones del modulo se escribe el nombre del modulo punto y la funcion EJ random.randint()
#3 random.randint() genera un numero aleatorio entre 2 valores (incluidos los valores)

#** Modulo de python == Paquete de funciones, clases y variables desarrollado por los credares de python
#  Para Importar un modulo se escribe Import + el nombre del modulo 
