# Programacion orientada a objetos (POO o OOP)

# definir una clase (molde para crear mas objetos de ese mismo tipo
# (coche) con caracteristicas similares)

class Coche:

    color = "rojo"
    marca = "ferrri"
    modelo = "aventador"
    velocidad = 300

    # metodos, son acciones que hace el objeto (coche)

    # Getters y Setters

    # metodo set para establecer parametros
    def setColor(self, color):
        self.color = color
    
    # metodo get para obtener parametros
    def getColor(self):
        return self.color

    # metodo set para establecer parametros
    def setModelo(self, modelo):
        self.modelo = modelo

    # metodo get para obtener parametros
    def getModelo(self):
        return self.modelo



    def acelerar(self):
        self.velocidad += 1

    def frenar(self):
        self.velocidad -= 1

    def getVelocidad(self):
        return self.velocidad

# fin definicion de clase

# crear objetos o instanciar la clase 

# coche 1
coche = Coche()
print("coche 1")
coche.setColor("amarrilo")
coche.setModelo("murcielago")


print(coche.marca, coche.getColor(), coche.getModelo())
print("Velocidad actual", coche.getVelocidad())

coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.frenar()

print("Velocidad actual", coche.getVelocidad())
print("-----------------------------------------")

# crear mas objetos 

# coche 2
print("coche 2")
coche2 = Coche()

coche2.setColor("negro")
coche2.setModelo("mamalodon")

print(coche2.marca, coche2.getColor(), coche2.getModelo())

