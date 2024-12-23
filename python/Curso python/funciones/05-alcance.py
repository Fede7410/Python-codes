def saludar():
    saludo = "Hola mundo"


def saludaChanchito():
    # esta variable saludo es diferente de la de la funcón anterior, sen guardan en lugares diferentes de memoria
    saludo = "Hola Chanchito"


# Aquí tira el error de que no esta definida porque esta se definio dentro del alcance
# de la función, pero no en el contexto global. solo es interna. Si quisiera usar una variable
# del contexto global dentro de mi funcion (lo cual es una mala practica),
# tengo que utilizar la plabra reservada global antes de la variable
print(saludo)
