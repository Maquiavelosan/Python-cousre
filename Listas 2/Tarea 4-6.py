""" 6.1 - Crea una lista con los numeros del 0 al 10
6.2 - Escribe el codigo para invertir los elementos de la lista sin utilizar el metodo 'reverse' o cualquier otro metodo que ya haga esta operacion (Usar for o while).
    Nota: es preferible que el resultado sea 'in-place' (que se modifique la misma lista en lugar de crear una nueva.
6.3 - Si pudiste hacer la version 'in-place' puedes intentar la version que genera una lista nueva (es un poco mas simple)
    Importante: La lista inicial deberia poder cambiar su contenido (por ejemplo cambiar el rango del 0 al 100) y el codigo deberia poder invertir la nueva lista sin problema """

decena=[]
contar=101

while contar > 0:
    decena.insert (0,contar-1)
    contar=contar-1
    
print(f"Original: {decena} ")


#6.2
contar =1
decena=[]
for contar in range(0,101):
    decena.insert(0,contar)

print(f"Al reves: {decena}" )


#funcion reverse
decena.reverse()
print(decena)