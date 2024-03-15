import math

from abc import ABC, abstractclassmethod

class FormaGeometrica(ABC):
    contador = 0
    def __init__(self):
        FormaGeometrica.contador +=1
        
    @abstractclassmethod
    def area(self):
        ...
    @abstractclassmethod
    def perimetro(self):
        pass
    
    @classmethod
    def get_qtd_formas(cls):
        return cls.contador
    
    def mensagem(self):
        print("Fui chamado")
        print("Chamado por: ",self.__class__.__name__)
    


class Quadrado(FormaGeometrica):
    def __init__(self,lado):
        super().__init__()
        self.lado = lado

    def area(self):
        return pow(self.lado,2)
    
    def perimetro(self):
        return 4*self.lado
    
    def get_lado(self):
        print(self.lado)
    
    def set_lado(self,novoLado):
        if(novoLado<=0):
            print("Tamanho inválido")
        else:
            self.lado = novoLado

class Circulo(FormaGeometrica):
    def __init__(self,raio):
        super().__init__()
        self.raio = raio
    
    def area(self):
        return "{:.2f}".format(math.pi * pow(self.raio,2))
    
    def perimetro(self):
        return "{:.2f}".format(2 * math.pi * self.raio)
    
    def get_raio(self):
        print(self.raio)
    
    def set_raio(self,novoRaio):
        if(novoRaio<=0):
            print("Tamanho inválido")
        else:
            self.raio = novoRaio


if __name__ == '__main__':
    
    quad1 = Quadrado(2)
    print(quad1.area())
    print(quad1.perimetro())

    quad1.set_lado(4)
    print(quad1.area())
    print(quad1.perimetro())
    
    circ1 = Circulo(12)
    print(circ1.area())
    print(circ1.perimetro())
    circ1.mensagem()
    print(FormaGeometrica.get_qtd_formas())

