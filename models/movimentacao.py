from abc import ABC, abstractmethod
from datetime import datetime

class Movimentacao(ABC):
    def __init__(self, tipo, valor, data=None, descricao=""):
        self.tipo = tipo
        self.valor = valor
        self.data = data or datetime.now()
        self.descricao = descricao

        def __repr__(self):
            return f"{self.data.strftime('%d/%m/%Y')} - {self.tipo}: R${self.valor:.2f} ({self.descricao})"
