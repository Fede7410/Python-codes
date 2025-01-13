# Set significa grupo o conjunto.
# Es una colección de datos que no se puede repetir y que no está ordenada
# Estan duplicados para demostrar que python los elimina automaticamente
primer = {1, 1, 2, 2, 3, 4}
print(primer)
# Se puede trabajar al igual que las listas
primer.add(5)
primer.remove(1)
print(primer)
primer = {1, 1, 2, 2, 3, 4}
segundo = [3, 4, 5]
# Vamos a crear un set de la lista anterior
segundo = set(segundo)
print(segundo)
# para unir dos set's usamos el operador |(alt 124) llamado unión.
print(primer | segundo)
# para intercectar dos sets usamos &
print(primer & segundo)
# Para hacer la diferencia utilizamos -.
# Lo que hace es mostrar los elementos del conjunto de la izq luego de quitarle los de la derecha
print(primer - segundo)
# Tambien podemos utilizar la diferencia simetrica con el operador ^
# Lo que hace es devovler los elementos que se encuentran en al menos uno de los conjuntos
# pero no en los dos
print(primer ^ segundo)
# El problema de los sets es que no se encuentran ordenado
# y no pueda acceder a un elemento específico.
# Si podemos buscar si un elemento se encuentra en el set.
if 5 in segundo:
    print("hola mundo")
