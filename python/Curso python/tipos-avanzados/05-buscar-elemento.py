mascotas = ["Pelusa", "Pulga", "Pelusa", "Felipe", "Chanchito feliz"]

# Buscamos el indice de un elemento, si no esta nos tira un error del programa (crash)
print(mascotas.index("Pulga"))
# para evitar el error podemos hacer lo siguiente
if "Wolfgan" in mascotas:
    print(mascotas.index("Wolfgan"))
else:
    print("No esta en la lista")
# Si elelemento está repetido solo nos devuelve el primer indice
# Para contar cuantas veces se repite un elemento en la lista utilizamos
print(mascotas.count("Pelusa"))
