from models.conta import Conta

class ContaFactory:
    @staticmethod
    def criar_conta(tipo, numero):
        if tipo == 'simples':
            return Conta(numero)
        else:
            raise ValueError("Tipo de conta desconhecido.")