usuarios = [
    ["Chanchito", 4],
    ["Felipe", 1],
    ["Pulga", 5]
]
# Vamos a aplicar una transformación a la lista de usuarios para que nos devuelva una lista de nombres

nombres = []
for usuario in usuarios:
    nombres.append(usuario[0])
print(nombres)

# Existe una forma más corta de hacer esto, que es utilizando comprensión de listas
# variable = [expresion for item in lista]. Tambien se la conoce como map
nombres2 = [usuario[0] for usuario in usuarios]
print(nombres2)
# Ahora deseo filtrar elementos. tambien conocido como filter
nombres = [usuario for usuario in usuarios if usuario[1] > 2]
print(nombres)
# También podemos modificar y filtrar una lista al mismo tiempo utilizando la comprensión de listas
nombres3 = [usuario[0] for usuario in usuarios if usuario[1] > 2]
print(nombres3)

# para utilizar map hacemos lo siguiente
nombres = list(map(lambda usuario: usuario[0], usuarios))
print(nombres)
# para utilizar filter hacemos lo siguiente
menosUsuarios = list(filter(lambda usuario: usuario[1] > 2, usuarios))
print(menosUsuarios)
