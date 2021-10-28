""" 1 - Crea una lista que contenga algunos nombres de usuarios incluido 'admin', para cada usuario imprime un mensaje de bienvenida:
'Hola {username}, bienvenido'. Unicamente para el usuario admin debe imprimir el mensaje 'Hola admin, quieres visualizar el reporte de uso?' """

usuarios= ["admin", "alfredo", "sergio", "lupita", "uriel"]

for cont in usuarios:
    if cont == "admin":
        print("Bienvenido Admin, quieres visualizar el reporte de uso?")
    else:
        print(f"Bienvenido {cont}")
        
