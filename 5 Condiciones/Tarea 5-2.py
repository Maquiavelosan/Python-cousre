""" 2 - Crea una lista con los numeros (tipo entero) del 1 al 9. 
Itera la lista y crea una cadena de if-elif-else dentro del ciclo, para imprimir el numero ordinal, por ejemplo para el 1 -> primero, 2 -> segundo, etc. 
Cada numero se debe imprimir en una linea diferente. """

numeros= [1,2,3,4,5,6,7,8,9]

for cont in numeros:
    if cont == 1:
        print("1 -> Primero")
    elif cont == 2:
        print("2 -> Segundo")
    elif cont == 3:
        print("3 -> Tercero")
    elif cont == 4:
        print("4 -> Cuarto")
    elif cont == 5:
        print("5 -> Quinto")
    elif cont == 6:
        print("6 -> Sexto")
    elif cont == 7:
        print("7 -> Septimo")
    elif cont == 8:
        print ("8 -> Octavo")
    else:
        print ("9 -> Noveno")
