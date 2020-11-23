"""
Ejercicio 1. Hacer un programa que tenga una lista
de 8 numeros enteros y haga lo siguiente:
- Recorrer la lista mostrada
- Hacer una funciona que recorra listas de numeros y devuelva  un string
- Ordenarla y mostrarla
- Buscar algun elemento que el usuario pida por teclado 

"""
# crear la lista 
numeros = [10,3,20,4,60,5,8,70]

# crear funcion que recorra la lista y devuelva un string
def mostrarLista(lista):
    resultado = ""

    for elemento in lista:
        resultado += "elemento " + str(elemento)
        resultado += "\n"
    return resultado

# recorrer y mostrar 
print("########## recorrer y mostrar ########")

"""
for numero in numeros:
    print(numero)
"""

print(mostrarLista(numeros))

# mostrar su longitud 
print("##########  mostrar su longitud  ########")

print(len(numeros))

# busqueda en la lista 

buscar =  int(input("introduce el numero "))

comprobar = isinstance(buscar, int)

while not comprobar or buscar <= 0:
    buscar =  int(input("introduce el numero "))
else:
    print(f"has introducido el {buscar}")    

print(f"buscar en la lista el numero {buscar}")

search = numeros.index(buscar)

print(f"el numero existe en la lista, es el indice: {search}")




