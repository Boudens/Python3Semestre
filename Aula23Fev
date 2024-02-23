class Livro:
    contador = 0
    def __init__(self,titulo,autor,paginas,preco=0.0):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.preco = preco 
        conjuntoLivros.append(self)
        Livro.contador+=1



    def __str__(self):
        return f"Titulo: {self.titulo}, Autor: {self.autor}, Paginas: {self.paginas}, Preço: {self.preco}"

    def get_titulo(self):
        print(self.titulo)

    def set_Titulos(self,novoTitulo):
        if len(novoTitulo)<= 0:
            print ("Titulo Invalido")
        else:
            self.titulo = novoTitulo
        
    def aumenta_preco(self,aumento):
        self.preco = self.preco + aumento

    def get_preco(self):
        print(self.preco)

    def mostra_dados(self):
        print(f"Titulo: {self.titulo}, Autor: {self.autor}, Paginas: {self.paginas}, Preço: {self.preco}")

    def aumento_porcentagem(self,porcentagem):
        self.preco += self.preco*(porcentagem/100)

    def promocao(self,promocao):
        self.preco -= self.preco*(promocao/100)

    def mostra_lista(Lista):
        for i in Lista: 
            print (f"{(conjuntoLivros.index(i) +1)} - {i}")

if __name__ == '__main__':
    conjuntoLivros = []
    livro1 = Livro("Peixe Koi e o labirinto de ramish","Matheus Guto",900,20.0)
    livro2 = Livro("Evelynn e suas malvadezas","Alessandra",3)

    #print(livro1)
    #print(livro2)
    #livro1.set_Titulos("Peixe Koi e o Labirinto de Feras")
    #livro1.get_titulo()

    #livro2.set_Titulos("")
    #livro2.get_titulo()
    #livro1.aumenta_preco(50.0)
    #livro1.get_preco()

    #livro1.promocao(10)
    #livro1.get_preco()

    Livro.mostra_lista(conjuntoLivros)

    print("Quantidade de Livros: " ,Livro.contador)





