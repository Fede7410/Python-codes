# podemos agregar cosas, numeros, caracteres, y otras listas (algo asi como sublistas)

# la lista es todo lo que se encuentra entre corchetes.
# Podemos agregar la cantidad de elementos que querramos, pero siempre separados por una ",".
numeros = [1, 2, 3]
print(numeros)
letras = ["a", "b", "c"]
print(letras)
palabras = ["chanchito", "feliz"]
palabrasFelices = ["chanchito", "feliz", "Felipe", "alumno"]
print(palabras)
print(palabrasFelices)
booleans = [True, False, True, True]
print(booleans)
matriz = [[0, 1], [1, 0]]  # Una matriz es un listado que contiene listados
print(matriz)
ceros = [0] * 10  # podemos multiplicar el contenido de la lista
# la cant de veces que querramos que aparezca dentro de la lista
print(ceros)
# agrega el contenido de cada lista dentro de una lista mayor
alfanumerico = numeros + letras
print(alfanumerico)
# list crea una lista con el argumento que le coloquemos
# usamos range para listar del 0 al 9
rango = list(range(10))
print(rango)
# le decimos desde donde y hasta donde queremos que enliste
rango2 = list(range(1, 11))
# el aultimo numero no lo alcanza
print(rango2)
# Va a contener los caracteres de un string que le vamos a pasar
char = list("hola mundo")
print(char)
