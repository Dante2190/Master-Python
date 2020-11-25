# importar la clase coche como que fuera un modulo y poder utilizarla 

from coche import Coche

# instancias de la clase
carro = Coche("verde", "nissan", "centra", 220)
carro2 = Coche("rojo", "toyota", "hiluk", 220)
carro3 = Coche("amarrilo", "huydai", "rio", 220)
carro4 = Coche("rosado", "honda", "civit", 220)

# emprimir en pantalla la informacion del coche 
print(carro.getInfo())
print(carro2.getInfo())
print(carro3.getInfo())
print(carro4.getInfo())

print(type(carro4))