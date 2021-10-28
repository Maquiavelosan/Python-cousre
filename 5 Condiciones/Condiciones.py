# carros = ["audi", "bmw", "subaru", "toyota"]

# for carro in carros:
#     if carro == "bmw":
#         print(carro.upper())
#     else:
#         print(carro.title()) #Primer letra en mayuscula

#Operadores Boleanos

# edad = 20
# print(edad <25)
# print(edad>25)
# print(edad <=25)
# print(edad >=25)

##MUltiples condiciones

# edad=15
# if edad >=12 and edad <=18:
#     print("Eres un adolescente")
# else:
#     print("No eres un adolescente")

# if edad < 12 or edad > 18:
#     print("No eres un escuincle")

##Version 1
numeros=[1,23,54,2,75]
busqueda=78 #Valor busqueda se encuentra dentro de numeros?
# salida= False
# for valor in numeros:
#     if busqueda == valor:
#         salida=True
#         print("Si se encuentra")
#         break   #sale de la condicion
# if salida == False:
#     print("No se encuentra")

# ##Version 2
# if busqueda in numeros:
#     print("Si se encuentra")
# else:
#     print("No se encuentra")

###Calcular el costo del ticket en selva mágica

edad =int(input("Ingrese su edad: "))
costo=0

if edad < 4:
    costo= 0
elif edad < 18:
    costo = 80
else:
    costo =150

print(f"Debes pagar {costo} pesos")
