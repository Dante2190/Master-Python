"""
Diccionario:
Un tipo de dato que almacena un conjunto de datos.
En formato clave > valor.
Es parecido a un array asociativo o un objeto json.
"""

persona = {
    "nombre": "dante",
    "apellidos": "iraheta",
    "web": "danteapp.com"
}

#usar el diccionario completo
print(persona)

print("\n")

#usar un elemento del diccionario
print(persona["web"])

#lista con diccionarios 

print("\n")
contactos = [
    {
        'nombre': 'dante',
        'email': 'dante@gmail.com'
    },
    {
        'nombre': 'juan de Dios ',
        'email': 'juandeDios@gmail.com'
    },
    {
        'nombre': 'salvador',
        'email': 'salvador @gmail.com'
    }
]


#usar un elemento del diccionario
print(contactos[0]["nombre"])

for contacto in contactos:
    print(f"nombre del contaco: {contacto['nombre']} ")
    print(f"email del contaco: {contacto['email']} ")
    print("---------------------------------------------")

