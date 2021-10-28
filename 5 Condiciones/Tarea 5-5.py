""" 5.1 - Genera el codigo (usando ciclos) para generar la lista con los numeros primos entre el 1 y el 1000 (https://es.wikipedia.org/wiki/N%C3%BAmero_primo)
5.2 - Imprime esta lista y verifica que sea correcta (ver wikipedia ahi aparece la lista con los numeros primos menores a 1000) """

#NUMEROS PRIMOS = SOLO SON DIVISIBLES ENTRE SI MISMOS Y 1 

#Creacion de lista original
lista=[]
primo=[]
for valor in range (1,101) :
    lista.insert(0,valor) 
#Verificación de números primos, si se puede dividir mas de 2 veces no es primo
contador=0
for valor in range (2,101):
    dividendo= valor
    if valor % dividendo == 0 : #Si residuo es 0 es divisible y suma una 
        contador=contador+1
       

        if contador > 2:
            contador =0
            primo.insert(0,dividendo)
    

print(f"Lista {lista}")
print(f"Primos {primo}")