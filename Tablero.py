from Ficha import *

class Tablero:

    #Defina aquí los atributos de Tablero
    #inicialice aquí todos los atributos
    #no olvide usar self.atributo para acceder el atributo de la clase
    
    casillas = 70

    #también va a necesitar una lista de Fichas (puede asumir un número de Fichas fijo si le parece más fácil), 
    #y un mecanismo para saber quién sigue en el turno
    
    lFichas = [Ficha("red"),Ficha("blue"),Ficha("green"),Ficha("yellow")]
    
    def __init__(self):
        self.game(self.casillas)

    #agregue parámetros necesarios después de self
    #para iniciar los valores de sus atributos
    #defina aquí los métodos de Tablero
    #recuerde que el primer parámetro de cada método es siempre self
        
    def ronda(self,numeroRonda,casillas):
        print("")
        print("El número de ronda es:",numeroRonda)
        print("")
        for ficha in self.lFichas:
            print("Es turno de:",ficha.getColor())
            a = ficha.avanzar()
            if ficha.posicion >= casillas:
                print("")
                print("")
                print("El jugador avanza  a la posición: ", ficha.posicion)
                print("El jugador",ficha.getColor(),"ganó.")
                return False
            print("El jugador avanza  a la posición: ", ficha.posicion)
            print("")
    def game(self,casillas):
        contador = 1
        maximo = True
        while maximo:
            if self.ronda(contador,casillas) == False:
                maximo = False
            contador += 1
            
a = Tablero()
