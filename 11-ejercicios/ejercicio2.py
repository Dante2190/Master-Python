"""
escribir un programa que añada valores a una lista 
mientras que su longitud sea menor a 120 y luego mostrarla 
plus usar while  for 

"""

coleccion = []

x = 0

while x < 120:
    coleccion.append(f"elemento- {x}")
    print("mostando el " + coleccion[x])
    x += 1

print(coleccion)    


"""
for contador in range(0, 120):
   coleccion.append(f"elemnto-{contador}")
   print("mostrando el: " + coleccion[contador])

print(coleccion)
"""