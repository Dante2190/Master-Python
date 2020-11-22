"""
listas (arrays)

son colecciones o conjuntos de datos/valores, bajo un unico nombre.
para acceder a esos valores podemos usar un indice numerico.

"""

pelicula = "batman"

#definir lista

peliculas = ["batman", "spiderman", "el señor de los anillos"]
cantantes = list(('2pac', 'drake', 'jennifer lopez'))
year = list(range(20, 50))
variada = ["dante", 30, 4.5, True, "texto"]

"""
print(peliculas)
print(cantantes)
print(year)
print(variada)
"""

# indices

print(peliculas[1])
print(peliculas[-2])
print(cantantes[0:3])

# añadir elementos a la lista 

cantantes.append("ya ya ")
cantantes.append("ye ye ")
cantantes.append("yi yi ")
print(cantantes)

# recorrer listas 

print("###############listado de peliculas ##################")
"""
for pelicula in peliculas:
    print(pelicula)

nueva_pelicula = ""
while nueva_pelicula != "parar":
    nueva_pelicula = input("ntroduce el nombre de la pelicula ")

    if nueva_pelicula != "parar":
        peliculas.append(nueva_pelicula)

for pelicula in peliculas:
    print(f"{peliculas.index(pelicula)+1}. {pelicula}")
"""
# Listas multidimencionales listas dentro de listas 

print("###############listado de contactos ##################")

contactos = [
    [
        'dante',
        'dante.com'
    ],
    [
        'juan',
        'jaun.com'
    ]
]

#mostrar las lista
print(contactos)

#mostrar lsita especifica 

print(contactos[1][1])

# recorrer lista

for contacto in contactos:
    for elemento in contacto:
        if contacto.index(elemento) == 0:
            print("nombre " + elemento)
        else:
            print("email " + elemento)

    print("\n")

