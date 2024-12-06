# and, or, not

gas = True
encendido = False
edad = 18

if gas and encendido and edad > 17:
    print("Puedes avanzar")

if gas and (encendido or edad > 17):  # Primero resuelve parentesis
    print("Puedes avanzar")

# OPERACIONES DE CORTO-CIRCUITO  python ejecuta de ezq a derecha,
# si la primera evaluación alcanza para que todo lo demas sea verdadero o falso, no ejecuta lo demas
# por ejemplo si son todos and y la primer evaluacion es false, el resultado siempre va a ser false
# si son todos or y la primer evaluacion es true, todo va a ser true, y el resto de evaluaciones no
# se ejecutará

# and, or, not

gas = False
encendido = True
edad = 18

if not gas and encendido and edad > 17:
    print("Puedes avanzar")
