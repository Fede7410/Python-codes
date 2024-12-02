nombre = "Federico"
apellido = "Seoane"
nombre_completo = nombre + " " + apellido
print(nombre_completo)
nombre_completo = "prueba"
print(nombre_completo)
# Función de formateo de strings, dentro de cada llave se puede usar cualquier expresion
nombre_completo = f"{nombre} {apellido}"
print(nombre_completo)
nombre_completo = f"{nombre[0]} {2 + 5}"
print(nombre_completo)