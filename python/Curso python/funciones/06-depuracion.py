# definimos una funcion para calcular la longitud de un texto

def largo(texto):
    resultado = 0
    for _ in texto:
        resultado += 1
    return resultado


print("Chanchito")
l = largo("Hola mundo")
print(l)
