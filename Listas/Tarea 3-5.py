lugares=["Chile", "Londres", "Japón", "Canada"]
tamaño=len(lugares)
contar=0

# while contar < tamaño:
#     print(f"Quiero ir a {lugares[contar]}\n")
#     contar = contar +1
print("ORIGINAL")
print(lugares)

print("RANDOM")
modificado=sorted(lugares)
print(modificado)

print("REVERSA")
reversa=list(reversed(lugares))
print(reversa)

print("REVERSA ORIGINAL")
reversa=list(reversed(lugares))
print(reversa)
########################################CORREGIR SORT
print("ALFABETICO")
alfa=lugares.sort(key=str.lower)
print(alfa)

print("ORIGINAL")
print(lugares)