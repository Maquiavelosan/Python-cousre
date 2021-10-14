#2 - Crea una lista con los numeros del 1 al 1 millon, calcula la suma de los valores de la lista

millon=[0]
suma=0
for valor in range (1,1001): #lo deje en 1000 por que tarda mucho la creación de la lista de un millon de valores
    millon.insert (0,valor)
    suma=suma+valor

#print (millon)

print(f"El resultado de la sumatoria de un mil es: {suma}")

