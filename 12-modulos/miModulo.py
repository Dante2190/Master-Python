# modulo

def holaMundo(nombre):
    return f"hola que tal estas, {nombre}"

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