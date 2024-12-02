n1 = input("ingrese el primer numero ")
n2 = input("ingrese el segundo numero ")

n1 = int(n1)
n2 = int(n2)

suma = n1 + n2
resta = n1 - n2
producto = n1 * n2
division = n1 / n2

mensaje = f"""
Para los numeros {n1} y {n2},
el resultado de la suma es {suma}
el resultado de la resta es {resta}
el resultado del producto en {producto}
el resultado de la división es {division}
"""

print(mensaje)