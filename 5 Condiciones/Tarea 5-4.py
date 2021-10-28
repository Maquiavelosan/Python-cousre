""" 4.1 - Juego de adivinar el numero secreto: Utiliza el metodo uniform (https://docs.python.org/es/3/library/random.html#random.uniform) 
para generar un numero aleatorio entre 1 y 100.
4.2 - Usa un ciclo que repita las siguientes instrucciones.
    - Imprime un mensaje que diga 'Intenta adivinar el numero secreto, ingresa un numero entre el 1 y el 100'.
    - Utiliza un input para pedir el numero al usuario.
    - Cuando el numero ingresado no sea el mismo que se genero aleatoriamente, mostrar un mensaje que diga que el numero esta equivocado
    - El Juego debe repetirse mientras no se adivine el numero. """

import random

correcto = False
numero = int(random.uniform(1,100))
print(numero)

while correcto == False:
    print("Ingresa numero entre el 1 y el 100")
    entrada=int(input())
    
    if entrada == numero:
        print(f"El número {entrada} es correcto")
        correcto == True
        break

    else:
        print(f"El número {entrada} es incorrecto \n")

    
