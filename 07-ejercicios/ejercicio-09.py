"""
hacer un programa que pida numeros al usuario indifinidamente hastameter el numerro 111
"""

contador = 1

while contador < 100:
    num = int(input("introduce un numero: "))
    if num ==  111:
        print("correcto")
        break
    else:
        print(F"has introducido el.: {num}")