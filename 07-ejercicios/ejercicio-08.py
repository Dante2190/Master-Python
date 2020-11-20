"""
cuanto es el x % de x numero 
"""

num1 = int(input("ingrese el  numero: "))
porcentaje = int(input(f"que porcenta quieres sacar del {num1}?  "))


operacion = (num1 * (porcentaje/100))
print(f"el {porcentaje}% de {num1} es: {operacion}")