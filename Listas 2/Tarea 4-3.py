# - Crea una lista con los numeros del 1 al 100, Usa una lista de comprension para generar una nueva lista con
    #la raiz cuadrada (Nota: investigar como calcularla en python) de los numeros de la primer lista
import math
    
principal=[0]
raiz=[0]

#Calculo de raiz cuadrada de todos los valores
for valor in range (1,101): #Repite 100 veces
    principal.insert (0,valor)
    #raiz.insert(0,(math.sqrt(valor))

print(principal)
print(raiz)