# Recordatorio de funciones
print("Hola mundo")
# Vamos a crear nuestra propia funcion. Para eso usamos la palabra reservada def,
# luego indicamos el nombre que tendra la función, abrimos y cerramos parentesis y luego dos puntos.


def hola():
    print("Hola mundo!")
    print("Ultimate python")


# Hasta aca la definimos, pero si corremos el programa no hará nada, es necesario llamar a la funcion
hola()
hola()
# Esta función hará siempre lo mismo, pero podemos modificarla para que no lo haga


def hola(nombre):  # esta variable nombre solo puede ser utilizada en el contexto de mi funcion,
    # fuera de ella no. estas variables son obligatorias, es decir que siempre tenemos que darle
    # un valor para que esta funcione. Cuando definimos la funcion esa variable toma el valor de parametro
    print("Hola mundo!")
    print(f"Bienvenido {nombre}")


# acá le asignamos el string de Federico a la variable nombre para que sea usada.
# Cuando le damos un valor a ese parametro comienza a llamarse argumento
hola("Federico")
hola("Chanchito feliz")

# si quiero mas de un parametro, lo separo con comas


def hola(nombre, apellido):
    print("Hola mundo!")
    print(f"Bienvenido {nombre} {apellido}")


hola("Federico", "Seoane")
hola("Chanchito", "feliz")

# si quiero darle a un parametro un valor defecto en caso que
# no le pase el argumento correspondiente, a la derecha del parametro pongo igual y el valor que deseo


def hola(nombre, apellido="Feliz"):
    print("Hola mundo!")
    print(f"Bienvenido {nombre} {apellido}")


hola("Federico", "Seoane")
hola("Chanchito")


# si quiero pasar los argumentos en otro orden debo nombrarlos,
# pero si nombro uno, debo nombrarlos todos
def hola(nombre, apellido="Feliz"):
    print("Hola mundo!")
    print(f"Bienvenido {nombre} {apellido}")


hola(apellido="Seoane", nombre="Federico")
hola(nombre="Chanchito")
