#1 - Usa un ciclo for para imprimir los numeros nones del 1 al 99

for valor in range (1,100) :
    if (valor % 2 !=0):  #Operación con % sirve para obtener el residuo de una división
        print(valor)

