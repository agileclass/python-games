import random

class Labirinto(object):

    v1 = None
    v2 = None

    def __init__(self):
        self.v1=0
        self.v2=0

    def gerarDesafio(self):
        self.v1=random.randrange(1, 9)
        self.v2=random.randrange(1, 9)

    def getV1(self):
        return self.v1

    def getV2(self):
        return self.v2

    def getResultado(self):
        return self.v1 * self.v2

if __name__ == '__main__':
    print("BEM VINDO AO JOGO TABOADA")
    t = Labirinto()
    t.gerarDesafio()
    resultado = input("Quanto é: " + str(t.v1) + "x" + str(t.v2) + "? ")
    if resultado == str(t.getResultado()):
        print('Parabéns!')
    else:
        print('Errado, ' + str(t.v1) + "x" + str(t.v2) + " é igual a " + str(t.getResultado()))