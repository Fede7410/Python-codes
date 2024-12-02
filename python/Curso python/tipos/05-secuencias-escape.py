# se pone primero comillas simple para que después se interprete la comilla doble como parte del string
curso = 'Ultimate "Python"'
print(curso)
# Al usar la barra al revés le dice que el siguiente simbolo es parte del string y no un simbolo reservado
curso = "Ultimate \"Python\""
print(curso)
curso = "Ultimate \nPython\"" # \n lleva el string que sigue a la linea siguiente
print(curso)