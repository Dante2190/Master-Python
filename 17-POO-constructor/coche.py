class Coche:

    # atributos o propiedades publicos

    color = "rojo"
    marca = "ferrri"
    modelo = "aventador"
    velocidad = 300
    soy_publico = "soy un atributo publico "

     # atributos o propiedades privados
    __soy_privado = "soy un atributo privado "

    def __init__(self, color, marca, modelo, velocidad):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad



    # metodos, son acciones que hace el objeto (coche)
    # Getters y Setters

    # metodo set para establecer parametros

    def getPrivado(self):
        return self.__soy_privado
    def setColor(self, color):
        self.color = color
    
    # metodo get para obtener parametros
    def getColor(self):
        return self.color

    # metodo set para establecer parametros
    def setMarca(self, marca):
        self.marca = marca

    # metodo get para obtener parametros
    def getMarca(self):
        return self.marca

    # metodo set para establecer parametros
    def setModelo(self, modelo):
        self.modelo = modelo

    # metodo get para obtener parametros
    def getModelo(self):
        return self.modelo

        # metodo set para establecer parametros
    def setVelocida(self, velocidad):
        self.velocidad = velocidad

    # metodo get para obtener parametros
    def getVelocidad(self):
        return self.velocidad

    def acelerar(self):
        self.velocidad += 1

    def frenar(self):
        self.velocidad -= 1

    def getVelocidad(self):
        return self.velocidad

    def getInfo(self):
        info = "------ informacion del coche-------"

        info += "\n Color: " + self.getColor()
        info += "\n Marca: " + self.getMarca()
        info += "\n Modelo: " + self.getModelo()
        info += "\n Velocidad: " + str(self.getVelocidad())

        return info


# fin definicion de clase