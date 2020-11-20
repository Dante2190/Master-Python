"""
funciones:
una funcion es un conjunto de instrucciones agrupadas bajo 
un nombre que pueden reutilizarse invocando a la funcion 
tantas veces como sea necesario.

def nombreDeMifuncion(parametro):
    conjunto de instrucciones 


nombreDeMifuncion(mi_parametro)
"""

# ejemplo 1

print("ejemplo 1")

#definir funcion

def muestraNombre():
    print("dante")
    print("mael")
    print("juan de Dios")
    print("emerita")

muestraNombre()

print("##################################################################################")

# ejemplo 2 parametros
"""
print("ejemplo 2")

def mostrarNombres(nombre, edad):
    print(f"tu nombre es:{nombre}")

    if edad >= 18:
        print("y eres mayor de edad")
    else:
        print("y eres menor de edad")



nombre = input("introduce tu nombre : ")
edad = int(input("introduce tu edad: : "))

mostrarNombres(nombre, edad)    

print("##################################################################################")
"""
# ejemplo  parametros

print("ejemplo 3")

def tabla(numero):
    print(f"tabla de multiplicar del numero {numero}")

    for contador in range(11):
        operacion = numero*contador
        print(f"{numero} x {contador} = {operacion}")

    print("\n")


tabla(3)
tabla(7)

#ejercicio 3.1

for numero_tabla in range(1,11):
    tabla(numero_tabla)


    print("ejemplo 4")

    #parametros opcionales

    def getEmpleado(nombre, id = None):
        print("EMPLEADO")
        print(f"NOMBRE {nombre}")
        

        if id != None:
            print(f"id: {id}")

    getEmpleado("dante", "444")    


    print("\nejemplo 5")

    #parametros  returno devolver datos 

def saludame(nombre):
    saludo = f"hola, saludos {nombre}"

    return saludo

print(saludame("dante iraheta"))

print("\nejemplo 6")

    #parametros  returno devolver datos 

def calculadora(num1, num2, basicas = False):

    suma = num1 + num2
    resta = num1 - num2
    multi = num1 * num2
    divi = num1 / num2

    cadena = ""
    if basicas != False:
        cadena += "suma: " + str(suma)
        cadena += "\n"
        cadena += "resta: " + str(resta)
        cadena += "\n"
    else:
        cadena += "multiplicacion: " + str(multi)
        cadena += "\n"
        cadena += "division: " + str(divi)

    return cadena

print(calculadora(5,5))

print("\nejemplo 7")
# funcion dentro de otra funcion 

def getNombre(nombre):
    texto = f"el nombre es: {nombre}"
    return texto

def getApellidos(apellidos):
    texto = f"el apellidos es: {apellidos}"
    return texto

def devuelveTodo(nombre, apellidos):
    texto = getNombre(nombre) + "\n" + getApellidos(apellidos)
    return texto

print(devuelveTodo("dante", "iraheta"))


print("\nejemplo 8")
# funcion lambda sirve para operaciones sencillas 

dime_el_year = lambda year: f"el año es {year * 5}"

print(dime_el_year(2045))
    






