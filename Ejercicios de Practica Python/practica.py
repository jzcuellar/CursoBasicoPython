def dividir(num1,num2):
    try: #Ejecuta este codigo
        return num1/num2
    except ZeroDivisionError: #Ejecuta este codigo cuando hay una excepcion del tipo ZeroDivisionError (Division entre 0)
        print('No se puede dividir entre 0')
        return 'Operacion erronea'

num1=int(input('Ingresa un numero: '))
num2=int(input('Ingresa un numero: '))

print(dividir(num1,num2))