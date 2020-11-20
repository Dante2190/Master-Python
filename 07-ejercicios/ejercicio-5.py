"""
ejercicio 5. hacer un programa que muestre todos los numeros entre numeros q diga el usuario 
"""

num1 = int(input("ingrese el primer numero: "))
num2 = int(input("ingrese el segundo  numero: "))

if num1 < num2:

    for contador in range(num1, (num2 + 1)):
        print(contador)

else:
    print("el numero 1 debe ser menor al numero 2")        