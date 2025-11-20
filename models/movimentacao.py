from datetime import datetime

class Movimentacao:
    def __init__(self, tipo, valor, data=None, descricao=""):
        self.tipo = tipo
        self.valor = valor
        self.data = data if data else datetime.now()
        self.descricao = descricao

    def __repr__(self):
        # Formatação correta para exibição no extrato
        data_str = self.data.strftime('%d/%m/%Y %H:%M')
        return f"{data_str} - {self.tipo}: R$ {self.valor:.2f} ({self.descricao})"