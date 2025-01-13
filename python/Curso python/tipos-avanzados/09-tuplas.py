# Una tupla es una lista que no se pude modificar, pero pueden crearse nuevas tuplas
# en base a otras existentes.
numeros = (1, 2, 3) + (4, 5, 6)  # para definir una tupla utilizamos parentesis
print(numeros)

punto = tuple([1, 2])  # Tuple recive cualquier cosa que sea iterable
print(punto)
# Con una tupla podemos realizar las mismas acciones que con una lista, excepto aquellas
# que nos permiten modificarla
menosNumeros = numeros[:2]
print(menosNumeros)
# Se puede desempaquetar una tupla
primero, segundo, *otros = numeros
print(primero, segundo, otros)
# Se pude iterar una tupla
for n in numeros:
    print(n)
# numeros[0] = 5
# Si necesitamos modificar una tupla creamos una nueva lista.
# Cabe aclarar que lo que se modifica es la lista, no la tupla
listaNumeros = list(numeros)
listaNumeros[0] = "Chanchito feliz"
print(listaNumeros)
