#Calcular el área de un cuadrado

lado = 0 #inicializar la variable

print ("Ingrese el valor del lado del cuadrado")
dato= input() #Ingresar datos cadena de texto
lado=int(dato) #conversión a enteros

area= lado * lado
#area= lado**2

#Imprimir frase con variables 
print(f"El área de tu cuadrado de l= {lado} es:{area}")

