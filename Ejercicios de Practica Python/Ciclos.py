def run():
    
    import os
    def borrarPantalla(): #Funcion para borrar los datos en pantalla 
        if os.name == "posix":
            os.system ("clear")
        elif os.name == "ce" or os.name == "nt" or os.name == "dos":
            os.system ("cls")

    def saludo():
        import time #Modulo que provee varias funciones de tiempo en python
        tiempo = time.strftime("%H:%M:%S",time.localtime()) #Almacena la hora actual en la variable tiempo 
        print(f'La hora actual es: {tiempo}') #Funcion que imprime la hora actual
        hora = int(time.strftime("%H",time.localtime()))
        greet = 'Buenos dias!' if hora >= 5 and hora < 12 else('Buenas Tardes!' if hora >= 12 and hora < 18 
                else('Buenas noches!' if hora >= 18 and hora <24 else 'Buen dia, es de madrugada!'))
        print(greet)

    
    def calcul_ascii(): #Funcion que muestra el art ascii calculadora en consola
        print('Bienvenido a la calculadora\n')
        print('_____________________')
        print('|  _________________  |')
        print('| | JO           0. | |')
        print('| |_________________| |')
        print('|  ___ ___ ___   ___  |')
        print('| | 7 | 8 | 9 | | + | |')
        print('| |___|___|___| |___| |')
        print('| | 4 | 5 | 6 | | - | |')
        print('| |___|___|___| |___| |')
        print('| | 1 | 2 | 3 | | x | |')
        print('| |___|___|___| |___| |')
        print('| | . | 0 | = | | / | |')
        print('| |___|___|___| |___| |')
        print('|_____________________|\n\n')


    def show_menu(): #Funcion que despliega el menu
        print('Que deseas hacer?: ')
        for i in range(len(menu)):
            print(f'{i+1}. {menu[i]}')
        opc=int(input('ingresa una opcion: '))
        return opc

    
    def cant_num_user(opc):
        def insert_num():
            nu=int(input('ingresa un Numero: '))
            numeros.append(nu)
        numeros=[] #Lista numeros almacena los datos ingresados por el usuario para despues operarlos
        if opc==2:
            insert_num()
        elif opc==4 or opc==5 or opc==6:
            for i in range(2):
                insert_num()
        elif opc==3:
            for i in range(5):
                nu=int(input(f'Ingresa {i+1} Nota: '))
                numeros.append(nu)
        return numeros
        
    def default():
        print('Selecciona una opcion correcta')
        exit()
    
    def seleccion_menu(opc,numeros):
        if opc==1:
            saludo()
        elif opc==2:
            if numeros[0]%2 == 0:
                print(f'El numero {numeros[0]} es Par')
            else:
                print(f'El numero {numeros[0]} es Impar')
        elif opc==3:
            prom=sum(numeros)/len(numeros)
            print(f'El promedio de las {len(numeros)} Notas es {prom}')
        elif opc==4:
            modulo=numeros[0]%numeros[1]
            print(f'El residuo de la division "Modulo" {numeros[0]} ÷ {numeros[1]} es igual = {modulo}')
        elif opc==5:
            porc=numeros[0]/numeros[1]
            print(f'El porcentaje del primer numero respecto al segundo es {porc*100}%')
        elif opc==6:
            elev=numeros[0]**numeros[1]
            print(f'{numeros[0]} elevado a la {numeros[1]} es igual a {elev}')
        elif opc==7:
            import math
            print(f'La raiz cuadrada de {numeros[0]} es {math.sqrt(numeros[0])}')
        elif opc==8:
            print('Adios')
            exit()
        else:
            default()

    menu=['Saludar','Calcular si un número es par','Calcular el promedio de 5 notas','Calcular el módulo',
         'Calcular el porcentaje','Elevar a una potencia','Raiz cuadrada de un numero','Salir']

    borrarPantalla()
    calcul_ascii()
    opc=show_menu() #Varibale opc almacena la seleccion del usuario despues de mostrado el menu
    numeros=cant_num_user(opc)
    seleccion_menu(opc,numeros)

if __name__ == '__main__':
    run()