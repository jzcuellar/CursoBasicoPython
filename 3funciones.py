# def imprimir_mensaje():  #1 #2
#     print('Mensaje especial:')
#     print('Estoy aprendiendo a usar funciones! :')
    
# imprimir_mensaje() #3 
# imprimir_mensaje()
# imprimir_mensaje()

#1 Para Declarar una funcion utilizo def nombre_funcion
#2 Nombre de las funciones en minuscala y palabras separadas por guion bajo
#3 Para invocar la funcion 

# def conversacion(mensaje): #4 
#     print('Hola ')
#     print('Como estas? ')
#     print(mensaje)
#     print('Adios ')

# opcion = int(input('Elige una opcion (1,2,3):'))
# if opcion == 1:
#     conversacion('Elegiste la opcion 1: ') #5
# elif opcion == 2:
#     conversacion('Elegiste la opcion 2: ')
# elif opcion == 3:
#     conversacion('Elegiste la opcion 3: ')
# else:
#     print('Escribe la opcion correcta')
    
#4 Un parametro es un valor que la funcion espera recibir cuando sea invocada, Se indican entre los parentesis
#5 Para asignar valor al parametro se invoca la funcion y dentro de los parentesis se asigna valor al parametro

def suma(a,b):
    print('Se suman dos numeros ')
    resultado = a + b
    return resultado #6

sumatoria = suma(1,4) #7 
print(sumatoria)

#6 Return Statement sirve para devolver el resultado de la funcion de vuelta al argumento o variable que invoca la funcion
#7 Se asigna el valor resultante de la funcion a la variable sumatoria