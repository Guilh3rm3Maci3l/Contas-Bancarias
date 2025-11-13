from abc import ABC
from models.movimentacao import Movimentacao
from models.exceptions import *
from datetime import datetime

class Conta(ABC):
    def __init__(self, numero, saldo_inicial=0):
        self.numero = numero
        self.saldo = saldo_inicial
        self.movimentacoes = []

    def adicionar_movimentacao(self, tipo, valor, descricao=""):
        self.movimentacoes.append(Movimentacao(tipo, valor, descricao=descricao))
