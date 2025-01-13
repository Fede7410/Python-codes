numeros = [3, 1, 4, 5, 9, 2, 6]

numeros.sort()
print(numeros)  # [1, 2, 3, 4, 5, 6, 9]

numeros.sort(reverse=True)
print(numeros)  # [9, 6, 5, 4, 3, 2, 1]

numeros = [3, 1, 4, 5, 9, 2, 6]
numeros2 = sorted(numeros)  # Devuelve una nueva lista
print(numeros)  # [3, 1, 4, 5, 9, 2, 6]
print(numeros2)  # [1, 2, 3, 4, 5, 6, 9]
numeros3 = sorted(numeros, reverse=True)  # Ordena de mayor a menor
print(numeros3)  # [9, 6, 5, 4, 3, 2, 1]

usuarios = [
    [4, "Chanchito"],
    [1, "Felipe"],
    [5, "Pulga"]
]
usuarios.sort()
print(usuarios)  # [[1, 'Felipe'], [4, 'Chanchito'], [5, 'Pulga']]

usuarios = [
    ["Felipe", 1],
    ["Chanchito", 4],
    ["Pulga", 5]
]
usuarios.sort()
print(usuarios)

# Si el elemento ordenable no es el primero, se puede definir una función para hacerlo


def ordena(elemento):  # retornara el elemento por el que queremos que el listado sea ordenado
    return elemento[1]


usuarios.sort(key=ordena)
print(usuarios)  # [['Felipe', 1], ['Chanchito', 4], ['Pulga', 5]]

# Otra forma de hacerlo es con una función lambda

# Como argumento primero pasamos el parametro que queremos ordenar y despues el indice.
usuarios.sort(key=lambda el: el[1])
print(usuarios)  # [['Felipe', 1], ['Chanchito', 4], ['Pulga', 5]]
