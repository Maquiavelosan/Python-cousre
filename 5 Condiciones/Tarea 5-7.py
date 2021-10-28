""" 7.1 - Crea una lista con 10 colores, crea una segunda lista con tus colores favoritos.
7.2 - Imprimer un mensaje si alguno de tus colores favoritos esta dentro de la lista de colores. """

colores= ["Negro", "Azul", "Verde", "Rojo", "Amarillo", "Rosa", "Naranja", "Cafe", "Gris", "Morado"]

favoritos= ["Azul", "Rojo"]

for cont in favoritos:
    for cont2 in colores:
        if cont == cont2:
            print(f"Tu color favorito {cont} se encuentra el la lista principal")
        