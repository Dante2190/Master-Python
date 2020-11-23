"""
SET es un tipo de dato, para tener una coleccion de valores, pero no tiene ni indice ni orden 

"""

personas = {
    "dante",
    "juan de Dios",
    "emerita"
}

# agregar un elemento al set
personas.add("calin")

#remover un elemento del set
personas.remove("dante")

#comprabar el dato

print(type(personas))

print(personas)