# Capturar exepciones y manejar errores en codigo
# susceptibles a fallo/errores

"""
try:
    nombre = input("Cual es tu nombre?: ")

    if len(nombre) > 1:
        nombre_usuario = "el nombre es " + nombre
        
    print(nombre_usuario)
except:
    print("Ha ocurrido un error, mete bien el nombre")
else:
    print("todo ha ido bien")
finally:
    print("fin de la iteracion")
"""

# multiples execepciones 
"""
try:
    numeros = int(input("dime el numero para elevarlo al cuadrado: "))
    print("el cuadrado es: " + str(numeros*numeros))
except TabError:
    print("deber convertir tus cadenas a enteros en el codigo ")    
except ValueError:
    print("introduce un numero correcto")
except Exception as e:
    print("ha ocurrido un error: ", type(e).__name__)
    """

# Execepciones personalizadas o lanzar execepcion

try:
    nombre = input("introduce el nombre")
    edad = int(input("introduce la edad"))

    if edad < 5 or edad > 100:
        raise ValueError("la edad introducida no es real")
    elif len(nombre) <= 1:
        raise ValueError("el nombre no esta completo")
    else:
        print(f"todo correcto {nombre}")
except ValueError:
    print("introduce los datos correctamente")
except Exception as e:
    print("Exixte un error", e)

