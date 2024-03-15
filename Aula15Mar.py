from abc import ABC, abstractclassmethod
class Carro(ABC):
    precoLocacao=100
    contador = 0
    def __init__(self,modelo):
        self.modelo = modelo
        Carro.contador += 1
    def get_modelo(self):
        return self.modelo
    def set_modelo(self,novo_modelo):
        self.modelo = novo_modelo

    @abstractclassmethod
    def preco_diaria(self):
        pass
    @classmethod
    def get_precoLocacao(self):
        return self.precoLocacao
    def set_precoLocacao(self,novoPrecoLocacao):
        self.precoLocacao = novoPrecoLocacao

    @classmethod
    def get_qtd_carros(cls):
        return cls.contador

class Economico(Carro):
    def __init__(self, modelo):
        super().__init__(modelo)

    def preco_diaria(self):
        return self.precoLocacao + (self.precoLocacao * 0.05)

class Intermediario(Carro):
    def __init__(self, modelo):
        super().__init__(modelo)

    def preco_diaria(self):
        return self.precoLocacao + (self.precoLocacao * 0.10)



if __name__ == '__main__':
    carro1 = Economico("teste")
    
    #carro1.set_precoLocacao(200)
    print(carro1.preco_diaria())

    carro2 = Intermediario("Corsa")
    print(carro2.preco_diaria())

    print(Carro.get_qtd_carros())
