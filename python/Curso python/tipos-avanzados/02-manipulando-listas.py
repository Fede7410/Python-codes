mascotas = ["Wolfgang", "Pelusa", "Pulga", "Copito"]
# Imprimimos el elemento de la lista que queremos, siendo el primero el 0
print(mascotas[0])
mascotas[0] = "Bicho"
print(mascotas)
# Imprime desde el elemento 0 la cantidad de elementos que le indicamos en el segundo indice.
# Si omitimos el primer indice se toma por defecto el valor de 0.
# Si omitimos el indice de la derecha, por defecto se toma hasta el ultimo elemento.
# Si colocamos un indice negativo, va a ir hacia la izq, -1 seria el ultimo elemento.
print(mascotas[0:3])
# Lo que hace es tomar solo los elementos en ubicación par, en realidad lo que hace es indicar
# que solo tome 1 de cada dos elementos (salta el primero, toma el que sigue)
print(mascotas[::2])
# ahora vamos a realizar lo mismo, pero le vamos a indicar desde donde debe comenzar, hasta que
# elemento tomar y cada cuanto tomarlos
print(mascotas[1:2:2])

numeros = list(range(21))
print(numeros)
print(numeros[::2])
print(numeros[1::2])
print(numeros[::3])
print(numeros[:10:2])
