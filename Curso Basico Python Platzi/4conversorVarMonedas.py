def conversor(tipo_pesos, valor_dolar,):
    pesos = input("Cuantos pesos " + tipo_pesos + " tienes: ") #4 
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")

menu = """
Bienvenido al conversor de monedas 💰

1 - Pesos Colombianos
2 - Pesos Argentinos
3 - Pesos Mexicanos

Elige una opcion: """ #1 #2

opcion = int(input(menu)) #3

if opcion == 1:
    conversor("Colombianos", 3875)
elif opcion == 2:
    conversor("Argentinos", 65)
elif opcion == 3:
    conversor("Mexicanos", 24)
else:
    print("Ingresa una opcion correcta por favor")

#1 Boton Win + . Paraa Sacar Emojis 
#2 con """ """ puedo hacer Strings Multi lineas
#3 Puedo desplegar string multilinea que esta almacenado en una variable, al invocar la variable y solicitar un Input por parte del usuario EJ input(menu)
#4 Ctrl + f2 para cambiar todas las variables iguales al mismo tiempo EJ -> cambiar pesomex a pesocol