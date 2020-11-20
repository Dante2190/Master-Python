"""
mostrar todas las tablas de multiplicar del  al 10 
mostrar el titulo de la y luego las multiplicaciones el al 1 al 10 
"""

for cabecera in range(1, 11):
    print("##############################")
    print(F"##### tabla del {cabecera} #####")
    print("##############################")

    for num in range(1,11):
        print(f"{num} x {cabecera} = {num*cabecera}")