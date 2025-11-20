class ContaError(Exception):
    pass

class SaldoInsuficienteError(ContaError):
    def __init__(self, saldo_atual, valor_saque):
        super().__init__(f"Saldo R$ {saldo_atual:.2f} insuficiente para saque de R$ {valor_saque:.2f}.")

class SaldoNaoZeroError(ContaError):
    def __init__(self, saldo_atual):
        super().__init__(f"Não é possível fechar a conta. Saldo atual: R$ {saldo_atual:.2f}.")

class DataRetroativaError(ContaError):
    def __init__(self, data_nova, data_ultima):
        super().__init__(f"Data {data_nova} retroativa. Última movimentação em {data_ultima}.")