edad = 60
if edad > 64:
    print("Puede ver la pelicula con un super descuento")
elif edad > 54:   # el codigo se ejecuta de arriba hacia abajo hasta la primer condición true,
                # mientras siga siendo false sigue bajando sin ejecutar, cuadno encuentra una true ejecuta solo esa parte
    print("puede ver la pelicula con descuento")
elif edad > 17:  # se pueden anidar la cantidad de elif que se desee.
    print("Puede ver la pelicula")
else:
    print("No puedes entrar")

print("Listo")
