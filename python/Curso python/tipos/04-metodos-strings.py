animal = "  chanCHito feliz  "
# Pasar a mayusculas el contenido de animal
print(animal.upper())
# Pasar a minusculas en contenido de animal
print(animal.lower())
# Tomar el primer caracter y pasarlo a mayuscula, el resto en minuscula
print(animal.capitalize())
# Tomar la primera letra de cada palabra contenida en animal y pasarla a mayuscula,
# el resto dejarla en minusculas
print(animal.title())
# Remover los espacios en blanco a la izq y a la derecha de nuestro string
print(animal.strip())
# Primero remover los espacios y luego pasar a mayuscula el primer caracter
print(animal.strip().capitalize())
# Sacar los espacios de la izq de mi string
print(animal.lstrip())
# sacar los espacios de la derecha de mi string
print(animal.rstrip())
# Encontrar el indice de una cadena que buscamos dentro de nuestra variable,
# si devuelve -1 es porque no existe
print(animal.find("cH"))
# reemplazar determinados caracteres por otros, el primero es el que buscamos,
# el segundo el que queremos que quede
print(animal.replace("nCH", "j"))
# Saber si una cadena de caracteres se encuentra en el string, devolviendo un boolean
print("nCH" in animal)
# Saber si una cadena de caracteres NO se encuentra en el string, devolviendo un boolean
print("nCH" not in animal)
