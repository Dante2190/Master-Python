"""
mostrar todos los numeros impares entre 2 numeros q decida el usuario 

"""

num1 = int(input("ingrese el primer numero: "))
num2 = int(input("ingrese el segundo  numero: "))

if num1 < num2:

    for contador in range(num1, (num2 + 1)):
        if contador%2 == 0:
            print(f"{contador} es par")
        else:
            print(f"{contador} es impar")
else:
    print("el numero 1 debe ser menor al numero 2")  