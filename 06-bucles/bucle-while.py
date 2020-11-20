"""
bucle while 
es una estructura de comtrol que itera o repite la ejecucion de una serie de instruccciones tantas
como sea necesario, hasta que deje de complirse la condicion 

"""
print("ejemplo 1")
contador = 1

while contador <= 100:
    print(f"estoy en el numero {contador}")
    contador += 1


print("ejemplo 2")
contador = 1
muestrame = str(0)

while contador <= 100:
    muestrame = muestrame +", " + str(contador)
    contador += 1

print(muestrame)    

print("ejemplo 3")

num_usuario = int(input("de que numero quieres la tabla: "))

if num_usuario < 1:
    num_usuario = 1

contador = 1
while contador <=10:
    print(F"{num_usuario} x {contador} = {num_usuario*contador}")
    contador += 1
else:
    print("tabla termina")

