# Como empaquetar todos los parametros en uno solo

def get_product(**datos):
    print(datos["id"], datos["name"])


get_product(id="23",
            name="iPhone",
            desc="Esto es un iphone")
