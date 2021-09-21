#Imprimir Mensaje desde una variable
mensaje="Holis holiwis"
print (mensaje)

print (mensaje.upper()) #Cambiar a mayusculas
print (mensaje.lower()) #Cambiar a minúsculas

#Concatenar variables de texto
nombre = "Alfredo"
apellido = "Carbajal"
print(nombre + " " + apellido)

#Concatenar una variable e imprimir la concatenación
nombre_completo= (nombre +" "+apellido)
print (nombre_completo)

#Cadenas F 
#Sirve para concatenar variables
nombre_f= f"{nombre} {apellido}"
print ("variable F " +nombre_f)

#Salto de línea "\n"
saltar="Salto\nde \nlinea"
print (saltar)

#Tabulador de línea "\t"
tabulador= "Tabulador \tde \tlinea"
print (tabulador)

#limpieza de espacios vacios de una cadena
limpiar="        holis       "
print(limpiar.lstrip())#limpiar espacios a la izquierda
print(limpiar.rstrip())#limpiar espacios a la derecha
print (limpiar.strip())#limpiar espacios a ambos lados

#git status para revisar estatus del archivo 
#git add  para agregar el archivo al staged
#git commit -m "NOMBRE DEL ARCHIVO"

#git push  para subir el archivo a la nube de Git

