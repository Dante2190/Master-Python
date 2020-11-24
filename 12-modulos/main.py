"""
Modulos: son funcionalidades ya hechas para reutilizar.

En python hay muchos modulos, que los puedes consultar aqui:
https://docs.python.org/es/3/tutorial/modules.html

Podemos conseguir modulos que ya vienen en el lenguaje,
modulos en internet y tambien podemos crear nuestros propios modulos 
"""

# Importar modulo propio 

# Importar todo el modulo 
import miModulo

# Importar una funcion espesifica del modulo 
from miModulo import holaMundo

# Importar todas las funciones del modulo y la hora de llmar
#  el las funciones solo se pone el nombre de la funcion 
from miModulo import *

# llamar por el modulo completo
print(miModulo.holaMundo("dante iraheta"))
print(miModulo.calculadora(3, 5, False))

#llamar unicamente la funcion del modulo 
print(holaMundo("Juan de Dios"))

# Modulos de fecha 

import datetime

print(datetime.date.today())

fecha_completa = datetime.datetime.now()

print(fecha_completa)
print(fecha_completa.year)
print(fecha_completa.month)
print(fecha_completa.day)
print(fecha_completa.hour)
print(fecha_completa.minute)


#formatear la fecha segun nuestra necesidad

fecha_personalizada = fecha_completa.strftime("%d/%m/%Y, %H:%M:%S")

print("mi fecha personalizada", fecha_personalizada)

