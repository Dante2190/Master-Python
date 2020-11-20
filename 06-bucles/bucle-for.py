#bucle for

contador = 0
resultado = 0
print("ejemplo 1")
for contador in range(0,10):
    print(f"voy por el {contador}")
  #  print("voy por el "+ str(contador))
    resultado = resultado + contador

print(f"el resulado es: {resultado}")    

#tablas de multiplicar
print("ejemplo 2")

num_usuario = int(input("de que numero quieres la tabla: "))

if num_usuario < 1:
    num_usuario = 1

print(f"tabla de multiplicar del numero {num_usuario}")    

for num_tabla in range(1,11):
    print(F"{num_usuario} x {num_tabla} = {num_usuario*num_tabla}")
else:
    print("tabla termina")

