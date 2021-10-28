""" 6 - Crea un programa que pida una fecha (dia y mes, el dia debe ser numerico y el mes en string, 
por ejemplo: dia=23, string=Mayo) si esta fecha es tu cumpleanios entonces imprime un mesaje que lo indique, en otro caso indicar que no es tu cumpleanios. 
Nota: la comparacion del mes debe ser True aunque las mayusculas y minusculas no coincidan. """

print("Ingrese su día de nacimiento")
dia=int(input())

print("Ingrese su mes de nacimiento")
mes=input()
mes=mes.capitalize()
if dia==2 and mes == "Noviembre":
    print("El 2 de Noviembre es tu cumpleaños")
else:
    print(f"El {dia} de {mes} no es tu cumpleaños")