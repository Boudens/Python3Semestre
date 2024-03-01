class Pessoa:
    contador = 0
    @classmethod
    def get_qtd_pessoa(cls):
        return cls.contador
    
    def __init__(self,nome="",qtdDependentes=0):
        self.nome = nome
        self.qtdDependentes = qtdDependentes
        Pessoa.contador += 1

    def __str__(self):
        return f"Nome: {self.nome}\nQuantidade de Dependentes: {self.qtdDependentes}"

    def get_nome(self):
        print(self.nome)

    def set_nome(self,novoNome):
        if len(novoNome)<= 0:
            print ("Nome Invalido")
        else:
            self.titulo = novoNome

    def valor_extra(self):
        valor_extra = self.qtdDependentes * 100
        return valor_extra

    def get_qtdDependentes(self):
        print(self.qtdDependentes)

    def set_qtdDependentes(self,novoQtdDependentes):
        if (novoQtdDependentes)<= 0:
            print ("Quantidade Invalida")
        else:
            self.qtdDependentes = novoQtdDependentes

class Professor(Pessoa):
    def __init__(self,nome="",qtdDependentes=0,qtdTurma=0,valorRTurma=0):
        super().__init__(nome,qtdDependentes)
        self.qtdTurma = qtdTurma
        self.valorRTurma = valorRTurma

    def __str__(self):
        return f"Nome: {self.nome}\nQuantidade de Dependentes: {self.qtdDependentes}\nQuantidade de Turmas: {self.qtdTurma}\nValor por Turma:{self.valorRTurma}"
    
    def get_qtdTurma(self):
        print (self.qtdTurma)

    def set_qtdTurma(self,novoQtdTurmas):
        if (novoQtdTurmas)<= 0:
            print ("Quantidade Invalida")
        else:
            self.qtdTurma = novoQtdTurmas

    def aumenta_valorRTurma(self,aumento):
        self.valorRTurma += self.valorRTurma + aumento
    

    def rendimento(self):
        print (f"Rendimento do professor {self.nome}: {self.qtdTurma * self.valorRTurma}\n")

    def mostra_dados(self):
        print(f"Nome: {self.nome}\nQuantidade de Dependentes: {self.qtdDependentes}\nQuantidade de Turmas: {self.qtdTurma}\nValor por Turma:{self.valorRTurma}")

class Funcionario(Pessoa):
    def __init__(self,nome="",qtdDependentes=0,salarioFixo=0):
        super().__init__(nome,qtdDependentes)
        self.salarioFixo = salarioFixo

    def __str__(self):
        return f"Nome: {self.nome}\nQuantidade de Dependentes: {self.qtdDependentes}\nSalário Fixo: {self.salarioFixo})"

    def set_salarioFixo(self,novoSalarioFixo):
        if (novoSalarioFixo)<= 0:
            print ("Quantidade Invalida")
        else:
            self.salarioFixo = novoSalarioFixo

    def salarioTotal (self):
         salarioTotal = self.salarioFixo + self.valor_extra()
         print(f"O salario total do funcionario {self.nome} é {salarioTotal}")

    def mostra_dados(self):
        print(f"Nome: {self.nome}\nQuantidade de Dependentes: {self.qtdDependentes}\nSalário Fixo: {self.salarioFixo})")
        

if __name__ == '__main__':
    pessoa1 = Pessoa("Caio",0)
    prof1 = Professor("Grongos",5000,2,3)
    prof2 = Professor("Rammus",2000)
    prof3 = Professor()
    prof4 = Professor("Bardo",qtdTurma=4000)
    #print(prof1)
    #prof1.aumenta_valorRTurma(70)
    #print(prof1)
    #prof4.set_qtdDependentes(5)   
    #prof1.rendimento()

    func1 = Funcionario("Thiago",6,5000)
    func2 = Funcionario("Guto",56)
    func3 = Funcionario()

    func1.salarioTotal()

    print(Pessoa.get_qtd_pessoa())


