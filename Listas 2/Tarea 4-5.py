""" 5.1 - Crea una listas de tus pizzas 3 favoritas
5.2 - Crea una copia de tu lista y guardala en una variable que se llame 'pizzas_de_mi_amigo' 
      * Tip: usa slicing para copiar la lista, utilizar el operador '=' no funcionara (por ejemplo: pizzas_de_mi_amigo = mis_pizzas) en la siguiente sesion veremos por que.
5.3 - Agrega una pizza nueva a tu lista de pizzas
5.4 - Agrega una pizza nueva a la lista de pizzas de tu amigo
5.5 - Imprime ambas listas y verifica que el cuarto elemento de ambas pizzas debe ser diferente """

pizza=["Napolitana", "Pepperoni","Queso"]
print(pizza)

pizzas_de_mi_amigo = pizza [:]
print(pizzas_de_mi_amigo)

print("\nIngrese un nuevo sabor de pizza para Usted:")
pizza.insert(0,input())

print("\nIngrese un nuevo sabor de pizza para Su Amigo")
pizzas_de_mi_amigo.insert(0,input())

print(pizza)
print(pizzas_de_mi_amigo)