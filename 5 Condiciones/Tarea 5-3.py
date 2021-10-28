""" 3 - Crea un programa que lea una frase desde el teclado e imprima un mensaje que indique si esa palabra es un palindromo o no (https://es.wikipedia.org/wiki/Pal%C3%ADndromo), 
Tip: los strings tambien son indexados como las listas, por tarto se pueden iterar exactamente igual. """

print("Ingrese palabra a revisión de Palindromo")
lectura= input()
print(f"String {lectura}")

lista= lectura.split()
print(f"Lista {lista}")
tamaño=lista.__len__()

print(f"La cantidad de letras es {tamaño}")
