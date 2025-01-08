mascotas = ["Pelusa", "Pulga", "Felipe", "Chanchito feliz"]
# las listas son iterables, también, lo son los strings y el resultado de range()
for mascota in mascotas:
    print(mascota)
# enumerate() devuelve una tupla con el índice y el valor
for mascota in enumerate(mascotas):
    print(mascota)
for indice, mascota in enumerate(mascotas):  # desempaquetando la tupla
    print(indice, mascota)
