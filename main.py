class Conta:
    def __init__(self, numero):
        self.__numero = numero
        self.__tipo = "C"
        self.__saldo = 0.0
        

    def exibir_saldo(self):
        return self.__saldo
    
    def exibir_tipo_conta(self):
        return self.__tipo
    
    def creditar(self,valor):
        self.__saldo += valor

    def debitar(self,valor):
        self.__saldo -= valor

    def render(self, juros):
        valor = self.__saldo * (juros / 100)
        self.__saldo += valor

    def mudar_para_poupança(self):
        self.__tipo = "P"   

    def mudar_para_coorente(self):
        self.__tipo = "C"
        