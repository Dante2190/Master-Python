"""
ejercicio 3 escribir un program que muestre los cuadrados 
(un numero multiplicado por si mismo ) de los primeros 60 numeros
naturales resolverlo con for y con while
"""
#while
print("While")
contador = 0

while contador <= 60:
    cuadrado = contador*contador
    print(f"el cuadrado de {contador} es {cuadrado}")
    contador += 1

#for
print("For")
for numero in range(61):
    cuadrado = numero*numero
    print(f"el cuadrado de {numero} es {cuadrado}")