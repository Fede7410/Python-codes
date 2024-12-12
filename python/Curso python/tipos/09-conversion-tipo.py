# por defecto todo lo que ingrese el usuario será ingresado como string,
# luego hay que convertirlo al tipo deseado o necesario.
# tenemos funciones para eso
#       int()       pasa a un integer
#       str()       pasa a un string
#       float()     pasa a un float
#       bool()      pasa a un boolean, pero antes evalúa la experesión para saber si es true o false
#                   existe los conceptos de truthy y falsy, y quiere decir que determinados datos
#                   seran evaluados como true y otros como false.
#                   los falsy son: "" (string vacío), 0 y el objeto None


x = input("")
print(bool(""))
print(bool("0"))
print(bool(None))
print(bool(" "))
print(bool(0))
