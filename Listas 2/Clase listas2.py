#Lista con algunos presidentes de México

presidentes=["Andres Manuel", "Enrique Peña", "Felipe Calderon", "Vicente Fox"]

# for presidente in presidentes:
#     print (f"Hola {presidente} cuanto dinero te robaste")
#     print (f"Devuelve el dinero, plox\n")

# for valor in range (0,20,2):
#     print(valor)

# cuadrados = []  #lista vacía
# digitos=list(range(10))
# #print (digitos)
# print(max(digitos)) #funcion para detectar el más grande
# print(min(digitos)) #funcion para detectar el más pequeño
# print(sum(digitos)/len(digitos))    #promedio de los elementos de la lista

# for value in range (1,11):
#     cuadrado=value**2
#     cuadrados.append(cuadrado)  #llenado de lista vacía
# print(cuadrados)
#Código para generar la lista de cuadrados

# cuadrados=[value **2 for value in range (1,11)]
# print(cuadrados)

#vaciar una lista

# invitados = ["luis", "jose", "adriana", "fernando", "maria"]

# while len(invitados) >2:
#     invitado = invitados.pop()
#     print(f"{invitado} tu ya no estas invitado")

# print(invitados)    

####SLICING####
#Rebanar lista para extraer sublistas
ultimos_presidentes = presidentes [0:2]
print(ultimos_presidentes)
