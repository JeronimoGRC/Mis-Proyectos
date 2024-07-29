class Coche:

    def __init__(self, color, marca, modelo):
        self.color = color
        self.marca = marca
        self.modelo = modelo
    
    def __str__(self):
        return """El coche es de color: {0} 
La marca es: {1} 
El modelo es: {2}""".format(self.color, self.marca, self.modelo)