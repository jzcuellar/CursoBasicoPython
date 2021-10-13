def run():
    numero = int(input('Por favor ingrese un numero: '))
    if numero==2 : #Como es la primer opcion no entra a la segunda por tanto se cumple la condicion
        modulo = numero % 2
        cociente = numero / 2
        print(f'el modulo de 2 es {modulo} pero su cociente es {int(cociente)}  por tanto es primo')
    elif numero % 2 ==0:
        print('no es primo')
    else:
        print('es primo')
        
            
if __name__ == "__main__":
    run()```
