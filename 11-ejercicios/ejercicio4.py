"""
ejercicio 4 
crear un script que tenga 4 variables, una lista, un string, un entero, y un booleano y q imprima un mensaje 
segun el tipo de dato de cada varible. usar funciones 

"""

mi_lista = ["hola mundo", 77]
titulo = "master enee python"
numero = 100
verdadero  = True

def traducirTipo(tipo):
    resultado = None
    if tipo == list:
        resultado = "lista"
    elif tipo == str:
        resultado = "string"
    elif tipo == int:
        resultado = "entero"
    elif tipo == bool:
        resultado = "booleano"
    return resultado

def comprobarTipado(dato, tipo):
    test = isinstance(dato, tipo)
    resultado = ""
    
    if test:
        resultado = f"este dato es del tipo {traducirTipo(tipo)}"
    else:
        resultado = None

    return resultado      

      

print(comprobarTipado(mi_lista, list))
print(comprobarTipado(titulo, str))
print(comprobarTipado(numero, int))
print(comprobarTipado(verdadero, bool))


