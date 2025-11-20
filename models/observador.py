from abc import ABC, abstractmethod

class Observador(ABC):
    @abstractmethod
    def atualizar(self, conta, acao):
        pass

class LogObservador(Observador):
    def atualizar(self, conta, acao):
        data_hora = conta.movimentacoes[-1].data.strftime('%H:%M:%S')
        print(f"\n[NOTIFICAÇÃO - LOG] Conta {conta.numero} fez '{acao}' às {data_hora}.")
        print(f"Novo Saldo: R$ {conta.saldo:.2f}")