import os
os.system('cls')


class Titular:
    def __init__(self,nomeTitular,sobrenomeTitular,cpfTitular,):
        self.nomeTitular = nomeTitular
        self.sobrenomeTitular = sobrenomeTitular
        self.cpfTitular = cpfTitular

    def get_nomeTitular(self):
        return self.nomeTitular
    
    def set_nomeTitular(self,novoNomeTitular):
        if(len(novoNomeTitular)<=0):
            print("Nome Inválido")
        else:
            self.nomeTitular = novoNomeTitular
    
    def get_sobrenomeTitular(self):
        return self.sobrenomeTitular
    
    def set_sobrenomeTitular(self,novoSobrenomeTitular):
        if(len(novoSobrenomeTitular)<=0):
            print("Sobrenome Inválido")
        else:
            self.sobrenomeTitular = novoSobrenomeTitular        
    
    def get_cpfTitular(self):
        return self.cpfTitular
    
    def __str__(self) :
        return f"Nome: {self.nomeTitular}\nSobrenome: {self.sobrenomeTitular}\nCPF: {self.cpfTitular}"
    

class Conta():
    def __init__(self,numeroConta,saldoConta,obj_titular = Titular,vl_limite = 1000.0):
        self.numeroConta = numeroConta
        self.saldoConta = saldoConta
        self.vl_limte = vl_limite
        self.obj_titular = obj_titular

    def get_numeroConta(self):
        return self.numeroConta
    
    def set_numeroConta(self,novoNumeroConta):
        if(novoNumeroConta <= 0):
            print("Número da conta inválido")
        else:
            self.numeroConta = novoNumeroConta

    def get_saldoConta(self):
        return self.saldoConta
    
    def set_saldoConta(self,novoSaldoConta):
        if(novoSaldoConta <0):
            print("Saldo da conta não pode ser negativo.")
        else:
            self.saldoConta = novoSaldoConta

    def get_vl_limite(self):
        return self.vl_limte
    
    def set_vl_limite(self,novo_vl_limite):
        if(novo_vl_limite <0):
            print("Valor limite não pode ser menor que zero.")
        else:
            self.vl_limte = novo_vl_limite

    def extratoReduzido(self):
        print(f"Número da Conta: {self.numeroConta}\nSaldo da Conta:{self.saldoConta}")
    
    def extratoNormal(self):
        print(f"Nome: {self.obj_titular.get_nomeTitular()}\nSobrenome: {self.obj_titular.get_sobrenomeTitular()}\nCPF: {self.obj_titular.get_cpfTitular()}\nNúmero da conta: {self.numeroConta}\nSaldo da Conta: {self.saldoConta}")

    def mostrarDadosTitular(self):
        print(f"Nome: {self.obj_titular.get_nomeTitular()}\nSobrenome: {self.obj_titular.get_sobrenomeTitular()}\nCPF: {self.obj_titular.get_cpfTitular()}")

    def deposito(self,quantiaDeposito):
        if(quantiaDeposito<=0):
            print("Não é possivel fazer o depósito de um valor menor ou igual a zero.")
        else:           
            self.saldoConta = self.saldoConta + quantiaDeposito
            print(f"Depósito de {quantiaDeposito} realizado com sucesso.")

    def saque(self,quantiaSaque):
        if(quantiaSaque > self.saldoConta):
            print("Não há saldo disponível para realizar o saque.")
        else:
            self.saldoConta = self.saldoConta - quantiaSaque
            print(f"Saque realizado com sucesso.")

    def transferencia(self,contaDestino : "Conta",qtdTransferencia) -> float:
        if(qtdTransferencia <=0 ):
            print("Não é possível realizar uma transferência menor ou igual a zero.")
        else:
            self.saldoConta = self.saldoConta - qtdTransferencia
            contaDestino.saldoConta = contaDestino.saldoConta + qtdTransferencia 


    def __str__(self) :
        return f"Nome: {self.obj_titular.get_nomeTitular()}\nSobrenome: {self.obj_titular.get_sobrenomeTitular()}\nCPF: {self.obj_titular.get_cpfTitular()}\nNúmero da conta: {self.numeroConta}"


if __name__ == '__main__':
    t1 = Titular("Caio","Boudens","05432")
    t2 = Titular("Ana","Zaranza","02423")
    #print(t1)
   
    conta1 = Conta("0001",1000,t1)
    conta2 = Conta("0002",1000,t2)
    #t1.set_nomeTitular("Jonas")
    #conta1 = Conta("0001","1000",t1)
    #print(conta1) 
    # conta1.deposito(5000)
    #conta1.extratoNormal()
    #conta1.saque(900)
    conta1.extratoNormal()
    '''
    conta1.transferencia(conta2,500)
    print("\n")
    conta1.extratoNormal()
    print("\n")
    conta2.extratoNormal()
    '''
