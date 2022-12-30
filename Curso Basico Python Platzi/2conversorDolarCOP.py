pesos = input("Cuantos pesos Colombianos tienes?: ") #1 
pesos = float(pesos) #2
valor_dolar = 3875 
dolares = pesos / valor_dolar
dolares = round(dolares, 2) #3
dolares = str(dolares)#4
print("Tienes $" + dolares + " dolares")

#1 input == Solicitar datos al usuario a travez de un texto hyj6jn[m=-pp;.]
#2 float == convertir string a numero o numero con decimal
#3 round == devulve un valor con n numero de decimales
#4 str == convertir un numero a string
# Para asignar una variable se pone nombre de variable = y el valor de la misma
# Se utiliza # para hacer comentarios en Python

"""Este es un comentario multilínea.
Podemos escribir tantas líneas queramos a modo de documentación. Tambie Es un String Multilinea en Pytho """