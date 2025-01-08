numeros = [1, 2, 3]

# Vamos a desempaquetar la lista

primero, segundo, tercero = numeros
print(primero, segundo, tercero)

# Si queremos desempaquetar solo el primer elemento y el resto en otra variable
# El operador * indica que se desempaqueten los elementos restantes en una lista
primero, *otros = numeros
print(primero)
print(otros)

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Desempaquetamos los primeros dos elementos y el resto en una lista
primero, segundo, *otros = numeros
print(primero, segundo, otros)
print(numeros)  # La lista original no se modifica
primero, *otros, ultimo = numeros
print(primero, otros, ultimo)
