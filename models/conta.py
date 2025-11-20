from models.movimentacao import Movimentacao
from models.exceptions import *

class Conta:
    def __init__(self, numero, saldo_inicial=0):
        self.numero = numero
        self.saldo = saldo_inicial
        self.movimentacoes = []
        self.ativa = True
        self.observadores = []

    def registranumero(self):
         try:
             int(input("Digite o numero do conta: "))
         except ValueError:
             print("ERRO: O número de conta deve ser um valor inteiro")

    def adicionar_observador(self, observador):
        self.observadores.append(observador)

    def notificar_observadores(self, acao):
        for observador in self.observadores:
            observador.atualizar(self, acao)

    def _validar_data(self, data_nova):
        if not self.movimentacoes: return
        if data_nova < self.movimentacoes[-1].data:
            raise DataRetroativaError(data_nova, self.movimentacoes[-1].data)

    def depositar(self, valor, data, descricao):
        if not self.ativa: raise Exception("Conta encerrada.")
        if valor <= 0: raise Exception("Valor deve ser positivo.")

        self._validar_data(data)

        self.saldo += valor
        self.movimentacoes.append(Movimentacao("Depósito", valor, data, descricao))

        self.notificar_observadores("Depósito")

    def sacar(self, valor, data, descricao):
        if not self.ativa: raise Exception("Conta encerrada.")
        if valor <= 0: raise Exception("Valor deve ser positivo.")
        if self.saldo < valor: raise SaldoInsuficienteError(self.saldo, valor)

        self._validar_data(data)

        self.saldo -= valor
        self.movimentacoes.append(Movimentacao("Saque", valor, data, descricao))

        self.notificar_observadores("Saque")

    def get_saldo(self):
        return self.saldo

    def get_extrato(self, data_inicial=None):
        if not self.movimentacoes: return "Nenhuma movimentação."
        linhas = []
        for mov in self.movimentacoes:
            if data_inicial is None or mov.data >= data_inicial:
                linhas.append(str(mov))
        return "\n".join(linhas) if linhas else "Nada neste período."

    def fechar(self):
        if self.saldo != 0: raise SaldoNaoZeroError(self.saldo)
        self.ativa = False