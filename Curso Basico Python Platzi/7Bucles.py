def run():
    LIMITE = 1000 #1
    contador = 0
    potencia_2 = 2**contador #3
    while potencia_2 < LIMITE: #2
        print('2 Elevado a ' + str(contador) + ' es igual a: '+ str(potencia_2))
        contador += 1 #4
        potencia_2 = 2**contador


if __name__ == "__main__":
    run()

# 1 CONSTANTE Variable que no puede ser modificada, la nombro en Mayuscula EJ LIMITE = 1000
# 2 WHILE es una funcion que ejecutara una serie de instrucciones x veces mientras la condicion principal se cumpla 
#   Condicion Principal es la que viene despues del While
# 3 ** es el operador para indicar potencia en python
# 4 contador += 1 == contador = contador + 1  "+=" Significa coger la variable anterior y sumarle 