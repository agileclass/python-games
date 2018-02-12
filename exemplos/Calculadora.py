class Calculadora(object):

    valor = None

    def __init__(self, valorInicial=0.0):
        self.valor = valorInicial

    def soma(self, v):
        self.valor = self.valor + v

    def subtracao(self, v):
        self.valor = self.valor - v