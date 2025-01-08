mascotas = [
    "Wolfgang",
    "Pelusa",
    "Pulga",
    "Felipe",
    "Pulga",
    "Chanchito feliz"
]
# Si quiero agragar un elemento en un idice especifico utilizo .insert()
mascotas.insert(1, "Melvin")  # Inserta Melvin en la posicion 1
print(mascotas)
# Si quiero agregar un elemento al final de la lista utilizo .append()
# Agrega Chanchito triste al final de la lista
mascotas.append("Chanchito triste")
print(mascotas)
# Si quiero eliminar un elemento de la lista utilizo .remove()
# Pero solo elimina la primera ocurrencia, si deseo eliminar todas las ocurrencias debo iterar
mascotas.remove("Pulga")  # Elimina a Pulga de la lista
print(mascotas)
# Si quiero eliminar un elemento de la lista por su indice utilizo .pop() Si no le agrego un indice elimina el ultimo elemento
mascotas.pop()  # Elimina el ultimo elemento de la lista
print(mascotas)
# Si quiero eliminar un elemento por su indice utilizo del
del mascotas[1]  # Elimina el elemento en la posicion 1
print(mascotas)
# Si quiero eliminar todos los elementos de la lista utilizo .clear()
mascotas.clear()  # Elimina todos los elementos de la lista
