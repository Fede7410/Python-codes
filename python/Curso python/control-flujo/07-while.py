# Repite mientras se de una condición dada

# En este ejemplo vamos a duplicar un numero hasta que supere el valor de 100

numero = 1
while numero < 100:
    print(numero)
    numero *= 2

# Acá vamos a entrar en un lopp hasta que el usuario escriba salir

comando = ""

while comando.lower() != "salir":
    comando = input("$ ")
    print(comando)

# Genera un bucle infinito pero le da la condición de salida con el if
# Otra forma de realizar lo anterior

while True:
    comando = input("$ ")
    print(comando)
    if comando.lower() == "salir":
        break
