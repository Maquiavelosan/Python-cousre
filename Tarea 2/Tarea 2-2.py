#Convertir a número ASCII

print("Ingresa caracter a convertir en ASCII: ")

dato=input()
resultado= ord(dato) #Función ord extrae el número que representa el código ascii
print(f'El caracter "{dato}" representa en ASCII= {resultado}')