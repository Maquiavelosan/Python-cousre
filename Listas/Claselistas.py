"""
Colecciones de Python
Tema: Tipos de datos (Data Types) Lists & tuples - iterables
1. Las listas en Python son ordenadas, mutables, y permiten duplicados.
1.1. Los tuples en Python son ordenados, inmutables y permiten duplicados.
    Tuple Note: Si solo tenemos un valor en el tuple, tiene que terminar
    con una trailing comma ej. mi_tuple = (1,)
2. Acceder a los valores de la lista
3. list methods:
    list()
    tuple(())
    len()
    append()
    clear()
    copy()
    insert()
    pop()
3.1 tuple methods:
    count()
    index()
4. Convertir un string a una list
    string.split()
5. Convertir una list a un string
    string.join(lista)
"""
import sys
""" 
lista= []
mi_tuple=()

print(type(lista))
print(type(mi_tuple))

#Saber el tamaño de una lista o un tuple
print(f"Tamaño en memoria de la lista: {sys.getsizeof(lista)}")
print(f"Tamaño en memoria de la lista: {sys.getsizeof(mi_tuple)}")
#  """
# #Acceder a los valores de una lista o un tulple
#lista2=[1, 2, 3, 4, 5]
#tuple2=(6, 7, 8, 9, 10)

# print(lista2[2])
# print(tuple2[4])

# #Acceder al último valor de una lista o tuple
# print(lista2[-1])
# print(tuple2[-1])

#Función len() es para obtener la longuitud
#print(len(lista2))
#print(len(tuple2))

lista3= [9, 8, 7, 6, 5]
tuple3= (7, 7, 6, 1, 0)

lista3[3] = 10
lista3.insert(0,"insertado")
print(lista3)


