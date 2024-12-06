# Se utiliza para iterar elementos, para buscar elementos, realizar operaciones matemáticas

# Range crea una secuencia de numeros que vamos a usar en nuestro for (0,1,2,3,4).
for numero in range(5):
    # Numero va a tomar el valor de cada uno de los elementos que se encuentran en range.
    # Range es un iterable, también lo son las listas, tuplas y los strings
    print(numero, numero * 'hola mundo ')

# for else

buscar = 10
for numero in range(5):
    print(numero)
    if numero == buscar:
        print("Encontrado", buscar)
        break  # rompe el bucle una vez encontrado el numero para que deje de iterar
else:  # si no encuentra el numero lo informa
    print("no encontre el numero buscado")

for char in "Ultimate python":
    print(char)
