from abc import ABC, abstractmethod
from movimentacao import Movimentacao

class Conta(ABC):
    def __init__(self, numero, saldo_inicial=0):
        self.numero = numero
        self.saldo = saldo_inicial
        self.movimentacoes = []

    def depositar(self, valor, descricao="Depósito"):
        self.saldo += valor
        self.movimentacoes.append(Movimentacao("Depósito", valor, descricao=descricao))
        print(f"O novo saldo da conta é de: R${self.saldo:.2f}")

    def sacar(self, valor, descricao="Saque"):
        if self.saldo >= valor:
            self.saldo -= valor
            self.movimentacoes.append(Movimentacao("Saque", -valor, descricao=descricao))
            print(f"O novo saldo da conta é de: R${self.saldo:.2f}")

    def pagamento(self, valor, destinatario, descricao="Pagamento"):
        if self.saldo >= valor:
            self.saldo -= valor
            destinatario.saldo += valor
            self.movimentacoes.append(Movimentacao("Pagamento", -valor, descricao=descricao))
            destinatario.movimentacoes.append(Movimentacao("Recebimento", valor, descricao=f"De conta {self.numero}"))
            print(f"O novo saldo da conta é de: R${self.saldo:.2f}")
        else:
            print("Saldo insuficiente!")

    def extrato(self):
        print(f"\n=== Extrato da Conta {self.numero} ===")
        for m in self.movimentacoes:
            print(m)
        print(f"Saldo atual: R${self.saldo:.2f}\n")