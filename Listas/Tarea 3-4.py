from abc import abstractmethod
import random


invitados=["Cantinflas", "Luis Armstrong", "Eichiro Oda", "Rafael Perez"]
tamaño=len(invitados)
contar=0

while contar < tamaño:
    print(f"Buenas noches {invitados[contar]}, \n te invito a cenar el día de mañana a las 8pm en 'LA PIZZERIA'\n")
    contar = contar +1
    print("Asistirá a la cena? \nResponda 1= SI / 2= NO")
    asiste=int(input())

    if asiste==2:
        print(f"{invitados[contar]} no podrá asistir \n ¿A quién quieres invitar?: ")
        invitados[contar]=input()
        print(f"Buenas noches {invitados[contar]}, \n te invito a cenar el día de mañana a las 8pm en 'LA PIZZERIA'\n")

#Mesa más grande
print("Se aumento el tamaño de la mesa, puedes agregar más invitados")

print("Primer invitado adicional")
invitados.insert(0,input())
print(f"Buenas noches {invitados[0]}, \n te invito a cenar el día de mañana a las 8pm en 'LA PIZZERIA'\n")

print("Segundo invitado adicional")
invitados.insert(3,input())
print(f"Buenas noches {invitados[3]}, \n te invito a cenar el día de mañana a las 8pm en 'LA PIZZERIA'\n")

print("Tercer invitado adicional")
invitados.append(input())
print(f"Buenas noches {invitados[-1]}, \n te invito a cenar el día de mañana a las 8pm en 'LA PIZZERIA'\n")

print(invitados)

#Mesa no disponible, solo 2 invitados
tamaño=len(invitados)
print(tamaño)

while tamaño > 2 :
    borra = random.randint(0,tamaño)
    #print(invitados)
    print(f"Por límitaciones del COVID el restaurante restringió el número de invitados, {invitados[borra]} agradezco tu interés por asistir pero no será posible en ésta oocasión\n")
    invitados.pop(borra)
    #print (invitados)
    tamaño=len(invitados)

tamaño=len(invitados)
contar =0

while contar < tamaño:
    print(f"Buenas noches {invitados[contar]}, \n te invito a cenar el día de mañana a las 8pm en 'LA PIZZERIA'\n")
    contar = contar +1

print("¿Como les pareció la CENA?\n")