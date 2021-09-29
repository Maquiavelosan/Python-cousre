#Pedir al usuario un número del 1 al 1024 e imprimir este número en binario

print("Ingrese un múmero entre el 1 y el 1024")
dato=input()

binario=bin(int(dato))
texto=str(binario)
texto=texto.lstrip("0b")

print(f"El número {dato} equivale en binario a: {texto}")
