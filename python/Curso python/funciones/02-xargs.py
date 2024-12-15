# definición de multiples agrumentos para una funcion, sin precisar la cantidad

def suma(*numeros):  # Es importante el asterisco antes de la variable
    # para que la toma como iterable
    """Suma varios numeros"""
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado)


suma(2, 5, 7)
suma(2, 5)
suma(2, 8, 7, 45, 32)
