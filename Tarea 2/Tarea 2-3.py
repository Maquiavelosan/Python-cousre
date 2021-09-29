#Crea un programa que pida: Nombre, Edad, Teléfono, Dirección, Email y Nacionalidad e imprima un
#mensaje personalizado para él donde diga algo similar a lo siguiente:
#Hola Luis, me dijiste que tienes 43 años de edad y que tu teléfono es el 3315648790, además sé que 
#tu dirección es Independencia #23 y tu correo electrónico es luis25@gmail.com

print ("Ingrese su nombre porfavor: ")
nombre=input()

print ("Ingrese su edad: ")
edad=input()

print("Ingrese su número de teléfono: ")
tel=input()

print("Ingrese su dirección: ")
direc=input()

print("Ingrese su e-mail: ")
mail=input()

print ("Ingrese su nacionalidad: ")
nacion=input()

print(f" Bienvenido {nombre} \n Tu edad es de {edad} años \n Tu número telefónico es: {tel} \n Tu dirección es: {direc} \n Tu e-mail es: {mail} \n Tu nacionalidad es: {nacion}")
