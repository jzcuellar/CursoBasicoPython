def es_primo(numero):
    contador = 0
    for i in range(1, numero + 1): #2 #3
        if i == 1 or i == numero:
            continue #4
        if numero % i == 0:
            contador += 1
    if contador == 0:
        return True
    else:
        return False


def run():
    numero = int(input('Escribe un numero: '))
    if es_primo(numero): #1
        print('Es Primo')
    else:
        print('No es Primo')
    

if __name__ == "__main__":
    run()

#1 En un condicional If al colocar una funcion podemos obviar el ==True EJ: "if es_primo(numero):" == "if es_primo(numero) == TRUE:"  
#2 Un range produce un listado de numeros desde el parametro inicial hasta parametro final - 1 range(i,j) produce i,i+1,i+2...j-1
#3 Colocamos range(1, numero + 1) ya que queremos ir desde el 1 hasta el numero que coloco el usuario
#4 Si la variable que itera i es igual a 1 o al numero ingresado nos vamos a saltar la vuelta del ciclo

# OTRA Forma Prueba Primalidad Usando Teorema de Wilson, y libreria Math

from math import factorial

def prueba_prim(num):
    if factorial(num - 1) % num == -1 % num:
        return True
    else:
        return False

def run():
    num = int(input('Escribe un numero: '))
    if prueba_prim(num):
        print('Es un numero primo')
    elif num == 1:
        print('No es un numero primo')
    else:
        print('No es un numero primo')

if __name__ == '__main__':
    run()
