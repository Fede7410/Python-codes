nombre_curso = "Ultimate Python"
descripcion_curso = """
Ultimate Python,
este curso contempla todos los detalles que necesitas aprender para encontrar un trabajo como programador.
"""
print(nombre_curso, descripcion_curso)  # Imprime dos variables
print(len(nombre_curso))  # Imprime el largo del string
print(nombre_curso[0])  # Imprime el caracter especificado
# Imprime desde el caracter especificado antes de los dos púntos,la cantidad de caracteres
# especificada despues de los puntos#
print(nombre_curso[0:8])
# Imprime desde el caracter especificado hasta el final
print(nombre_curso[9:])
# Imprime desde el comienzo la cantidad de caracteres especificados
print(nombre_curso[:8])
# Imprime los dos valores por defecto, desde el comienzo hasta el final
print(nombre_curso[:])
