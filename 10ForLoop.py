def run():
    # for contador in range(20): #0
    #     print(contador)
    
    for i in range(10): #3
        print(11 * i)


    print("Comienzo")
    for i in ["Alba", "Benito", 27]: #1 
        print(f"Hola. Ahora i vale {i}") #2
    print("Final")


if __name__ == "__main__":
    run()

#0 Un Ciclo FOR o FOR Loop ejecutara unas instrucciones (Cuerpo del bucle) un numero determinado de veces por el elemento recorrible (Rango, Lista, Caracteres de una cadena) 
#1 Puedo Crerar un Ciclo For sin definir variable
#2 Para imprimir un valor aleatorio dentro de un String utilizo f-strings o literal Strings mas info https://www.python.org/dev/peps/pep-0498/
#2 f-string debo colocar f antes del string y entre corchetes {i} el valor que va a variar
# 3 Un Range se puede representar range(1,10)range(1,10) == range(10) Este representara los numeros hasta el anterior  