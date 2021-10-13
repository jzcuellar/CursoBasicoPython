nombre = input("Cual es tu nombre?")
nombre.upper() #1
nombre.capitalize() #2 
nombre.lower()  #3
nombre.strip()  #4
nombre.replace('o', 'a') #5
nombre[0] #7 #8

nombre = nombre.capitalize() #6

#1 'todos los caracteres del String en MAYÚSCULAS'
#2 'solo el primera Caracter  en MAYÚSCULA'
#3 'todos los caracteres en minúscula'
#4'eliminar espacios basura del string'
#5 Variable.replace('caractera a cambiar', 'caracter por poner') = remplazar carácter
#6 Para guardar el resultado del metodo este se debe asignar en una variable
#7 [0] Corchetes indican indice por lo cual nombre[0] devolvera la posicion del caracter solicitado en el corchete se inicia a contar en 0
#8 En progranacion CONTAMOS DESDE 0 casi SIEMPRE