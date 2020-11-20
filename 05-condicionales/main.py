#condicionales 
#ejemplo 1

print("############ EJEMPLO 1 #################")

color = "rojo"
#color = input("adivina cual es mi colo favorito ")
 
if color == "rojo":
    print("el color es rojo ")
else:
    print("color incorrecto")    

"""    
operadores de comparacion

== igual
!= diferente
< menor que 
> mayor que 
<= menor o igual que 
>= mayor o igual que 

#operadores logicos 

and = y
or  = o
!   = negacion 
not = no 
"""

print("############ EJEMPLO 2 #################")

year = 2021

#year = int(input("en que año estmos "))
if year >= 2021:
    print("estamos de 2021 en adelante ")
else:
    print("es un año anterio a 2021")    

print("############ EJEMPLO 3 #################")
#if aninados
nombre = "Dante iraheta "
ciudad = "tierra blanca"
continente = "America"
edad = 30
mayoria_edad = 18

if edad >= mayoria_edad:
    print(f"{nombre}  eres mayor de edad")

    if continente != "America":
        print("{no eres de america ")
    else:
        print(f"eres de america y de {ciudad}")    

else:
    print(f"{nombre} no eres mayor de edad")

print("############ EJEMPLO 4 #################")    

#dia = int(input("introduce el dia de la semana: "))
dia = 2
"""
if dia == 1:
    print("es lunes")
else:
    if dia == 2:
            print("es martes")   
    else:
        if dia == 3:
            print("es miercoles")   
        else:
            if dia == 4:
                print("es jueves")   
            else:
                 if dia == 5:
                    print("es viernes ")   
                 else:
                    if dia == 6:
                     print("es sabado")   
                    else:
                       print("es fin de semana 7")
  """
#elif

if dia ==1:
    print("es lunes ")
elif dia == 2:
    print("es martes")
elif dia == 3:
    print("es miercoles")    
elif dia == 4:
    print("es jueves")           
elif dia == 5:
    print("es viernes")
else:
    print("es fin de semana ")    

print("############ EJEMPLO 5 #################")     

edad_minima = 18
edad_maxima = 65
edad_ofical =  18
#edad_ofical = int(input("Tienes edad de trabajr" ))
"and"
if edad_ofical >= 18 and edad_ofical <= 65:
    print("estas en la edad de trabajar !!")
else:
    print("no estas en la edad de trabajar ")    

print("############ EJEMPLO 6 #################")     

pais = "El Salvador"
#or
if pais == "Mexico" or pais == "España" or pais == "Colombia":
    print(f"{pais} es un pais de habla hispana ")
else:
    print(f"{pais} no es un pais de habla hispana ")    

print("############ EJEMPLO 7 #################")    

pais = "El Salvador"
#negacion
if not (pais == "Mexico" or pais == "El Salvador" or pais == "Colombia"):
    print(f"{pais} no es un pais de habla hispana ")
else:
    print(f"{pais} si es un pais de habla hispana ")     

print("############ EJEMPLO 8 #################")    

pais = "El Salvador"
#comparacion 
if pais != "Mexico" and pais != "El Salvador" and pais != "Colombia":
    print(f"{pais} no es un pais de habla hispana ")
else:
    print(f"{pais} si es un pais de habla hispana ")         