# Los diccionarios son un conjunto de datos que se encuentran agrupados por una llave y un valor
# Sonmuy utilizados porque es como las bases de datos nos devuelven los datos
# A la izq va la llave ysiempre es un string, a la derecha cualquier cosa
# Para agregar más llaves se separan por una ','
punto = {"x": 25, "y": 50}
print(punto)
# Para acceder a algun valor específico usamos corchetes
print(punto["x"])
print(punto["y"])
# Puedo agregar llaves a un diccionario
punto["z"] = 45
print(punto)
# Si intentamos acceder a una llave inexistente da error, para evitar eso podemos usar un if
if "lala" in punto:
    print("Encontre lala", punto["lala"])
# Otra forma de acceder a un elemento es con .get
print(punto.get("x"))
# Si intentamos acceder a una llave ineccistente devuelve 'none'
print(punto.get("lala"))
# Si no queremos que devuelva none, podemos indicarle un valor por defecto
print(punto.get("lala", 97))
# Si quiero eleiminar una llave puedo usar 'del', elimina tmb el valor asociado
del punto["x"]
# Tambien hay una función 'del()'
del (punto["y"])
print(punto)
punto["x"] = 25

# también puedo iterar los valores dentro de un diccionario
for valor in punto:
    print(valor, punto[valor])
# hay otra sintaxis posible para acceder a cada elemento del diccionario
for valor in punto.items():
    print(valor)

for llave, valor in punto.items():
    print(llave, valor)

# Ahora vamos a veer un uso real de los diccionarios

usuarios = [
    {"id": 1, "nombre": "Chanchito"},
    {"id": 2, "nombre": "Feliz"},
    {"id": 3, "nombre": "Nicolas"},
    {"id": 4, "nombre": "Felipe"},
]

# para acceder a los nombres debemos iterar los usuarios

for usuario in usuarios:
    print(usuario["nombre"])
