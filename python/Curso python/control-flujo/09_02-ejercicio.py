# Vamos a realizar una calculadora
print("""Bienvenido a la calculadora
      Para salir escribe "salir"
      las operaciones son suma, resta, multi y div""")
num1 = ""
if num1 == "":
    num1 = input("Ingrese el primer numero: ")
    num1 = float(num1)
while num1 != "":
    oper = input("Ingrese la operación: ")
    if oper.lower() == "salir":
        print("Muchas gracias por usar la calculadora")
        break
    num2 = input("Ingrese el otro numero: ")
    num2 = float(num2)
    if "suma" in oper.lower() or "+" in oper.lower():
        num1 += num2
        print("El resultado es ", num1)
    elif "resta" in oper.lower() or "-" in oper.lower():
        num1 -= num2
        print("El resultado es ", num1)
    elif "multi" in oper.lower() or "*" in oper.lower():
        num1 *= num2
        print("El resultado es ", num1)
    elif ("div" in oper.lower() or "/" in oper.lower()) and num2 != 0:
        num1 /= num2
        print("El resultado es ", num1)
    else:
        print("La operación indicada no es valida.")
        break
