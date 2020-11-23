"""
programa que compruebe que si una variable esta vacia y si esta vacia, rellenar
con un texto en misnusculasy mostrarlo en mayusculas

"""

texto = "a"

if len(texto.strip()) <= 0:

    texto = "hola soy un texto en minusculas"

    #metodo upper para cambiar el texto a mayusculas 
    print(texto.upper())

else:
    print("la variable tiene contenido ")