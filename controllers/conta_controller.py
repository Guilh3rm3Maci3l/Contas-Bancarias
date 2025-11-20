from models.conta_factory import ContaFactory
from models.observador import LogObservador
from models.exceptions import *
from datetime import datetime

class ContaController:
    def __init__(self):
        self.contas = {}
        self.log_system = LogObservador()


    def registranumero(self):
         try:
             numero = int(input("Digite o numero do conta: "))
             return numero
         except ValueError:
             print("ERRO: O número de conta deve ser um valor inteiro")
             return -1

    def criar_conta(self, numero):
        if numero in self.contas:
            return f"ERRO: Conta {numero} já existe."

        try:
            nova_conta = ContaFactory.criar_conta('simples', numero)
            nova_conta.adicionar_observador(self.log_system)

            self.contas[numero] = nova_conta
            return f"Conta {numero} criada com sucesso!"
        except ValueError as e:
            return f"ERRO: {e}"

    def realizar_deposito(self, numero, valor, data, descricao):
        conta = self.contas.get(numero)
        if not conta:
            return f"ERRO: Conta {numero} não encontrada."

        try:
            conta.depositar(valor, data, descricao)
            return f"SUCESSO: Depósito de R$ {valor:.2f} realizado na conta {numero}."
        except (DataRetroativaError, Exception) as e:
            return f"ERRO: {e}"

    def realizar_saque(self, numero, valor, data, descricao):
        conta = self.contas.get(numero)
        if not conta:
            return f"ERRO: Conta {numero} não encontrada."

        try:
            conta.sacar(valor, data, descricao)
            return f"SUCESSO: Saque de R$ {valor:.2f} realizado na conta {numero}."
        except (SaldoInsuficienteError, DataRetroativaError, Exception) as e:
            return f"ERRO: {e}"

    def consultar_saldo(self, numero):
        conta = self.contas.get(numero)
        if conta:
            return f"SALDO: Conta {numero} - R$ {conta.get_saldo():.2f}"
        else:
            return f"ERRO: Conta {numero} não encontrada."

    def mostrar_extrato(self, numero, data_inicial_str):
        conta = self.contas.get(numero)
        if not conta:
            return f"ERRO: Conta {numero} não encontrada."

        try:
            data_inicial = None
            if data_inicial_str:
                data_inicial = datetime.strptime(data_inicial_str, "%d/%m/%Y")

            extrato_info = conta.get_extrato(data_inicial)
            data_display = data_inicial_str if data_inicial_str else "Início"
            return f"EXTRATO Conta {numero} (a partir de {data_display}):\n{extrato_info}"
        except ValueError:
            return "ERRO: Formato de data inválido. Use DD/MM/AAAA."

    def fechar_conta(self, numero):
        conta = self.contas.get(numero)
        if not conta:
            return f"ERRO: Conta {numero} não encontrada."

        try:
            conta.fechar()
            del self.contas[numero]
            return f"SUCESSO: Conta {numero} encerrada."
        except SaldoNaoZeroError as e:
            return f"ERRO: {e}"
        except Exception as e:
            return f"ERRO: {e}"