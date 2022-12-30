def run():
    for contador in range(10):
        if contador % 2 != 0: 
            continue #1 
        print(contador)


    # for i in range(10): #2
    #     print(i)
    #     if i == 6:
    #         break #3 
    
        
    # texto = input('Escribe un texto ')
    # for letra in texto: #4
    #     if letra == 'o':
    #         print(letra.replace('o','a'))
    #         continue
    #     print(letra)
    
    
    # LIMITE = 100
    # contador = 1
    # multiplo_10 = 10*contador
    # while multiplo_10 < LIMITE:
    #     print('El multiplo ' + str(contador) + ' de 10 es ' + str(multiplo_10))
    #     contador += 1
    #     multiplo_10 = 10*contador
    # print('The End')

if __name__ ==  "__main__":
    run()

#1 Continue Statement se utiliza para saltar la condicion y continuar ejecutando el ciclo
#2 Es usual utilizar la variable i como varible iterante en los ciclos en varios lenguajes (BUENA PRACTICA)
#3 Break Statement se utiliza para romper el ciclo en tanto se cumple una condicion
#4 Puedo utilizar Break y Continue statements con ciclos en cadenas de caracteres