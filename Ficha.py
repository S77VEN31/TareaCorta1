from Dado import *

class Ficha:
    color = ""
    posicion = 0

    #no era parte del modelo, pero la Ficha necesita usar un dado
    #este atributo se define cuando definimos relaciones entre clases
    #lo que veremos más adelante en el curso
    dado = Dado(6)
    
    
    def __init__(self, color):
        self.color = color
        self.posicion = 0

    def getColor(self):
        return self.color
        
    def avanzar(self):
        #aquí se vuelve claro por qué necesitamos un dado
        pasos = self.dado.lanzar()
        self.posicion += pasos
        return (print("Le salió el número: ",pasos," en el dado."))
    



        


