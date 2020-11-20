"""
ejercicio 2 escribir un script que nos muestre por pantalla 
todos los numeros par del 1 al 120 

"""

contador = 1

for contador in range(1, 120):
    if contador%1 == 0:
        print(contador)