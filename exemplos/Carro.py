class Carro(object):

    ligado = None
    velocidade = 0

    def __init__(self):
        self.ligado = 'off'
        self.velocidade = 0;

    def ligar(self):
        self.ligado = 'on'

    def desligar(self):
        self.ligado = 'off'
    
    def acelerar(self):
        if self.ligado == 'on':
            self.velocidade += 10
            return self.velocidade
        else:
            return -1
    
    def freiar(self):
        if self.ligado == 'on':
            self.velocidade -= 10
            return self.velocidade
        else:
            return -1

    def painel(self):
        #return self.ligado + ":" + self.velocidade
        return self.ligado + ":"+ str(self.velocidade)