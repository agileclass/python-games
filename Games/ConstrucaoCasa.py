import random

class ConstrucaoCasa(object):

    objetosCasa = None
    coresDisponiveis = None
    comandosDisponiveis = None

    def __init__(self):
        self.objetosCasa=[]
        self.coresDisponiveis=[]
        self.comandosDisponiveis=[]

    def getObjetosCasa(self):
        return self.objetosCasa

    def getCoresDisponiveis(self):
        return self.coresDisponiveis

    def gerarObjetosDisponiveis(self):
        self.objetosCasa.append("Paredes")
        self.objetosCasa.append("Telhado")
        self.objetosCasa.append("Portas")
        self.objetosCasa.append("Janelas")
        self.objetosCasa.append("Chaminé")

    def gerarCoresDisponiveis(self):
        self.coresDisponiveis.append("Amarelo")
        self.coresDisponiveis.append("Azul")
        self.coresDisponiveis.append("Vermelho")
        self.coresDisponiveis.append("Laranja")
        self.coresDisponiveis.append("Roxo")
        self.coresDisponiveis.append("Cinza")
        self.coresDisponiveis.append("Preto")
        self.coresDisponiveis.append("Branco")
        self.coresDisponiveis.append("Rosa")
        self.coresDisponiveis.append("Azul Marinho")

    def gerarComandos(self):
        self.comandosDisponiveis.append("Criar")
        self.comandosDisponiveis.append("Pintar")
        self.comandosDisponiveis.append("Mostrar Casa")
        self.comandosDisponiveis.append("Demolir")

    def gerarDesafio(self):
        self.gerarCoresDisponiveis()
        self.gerarObjetosDisponiveis()
        self.gerarComandos()

    def getObjeto(self, obj):
        return self.objetosCasa[obj]

    def getCor(self, cor):
        return self.coresDisponiveis[cor]

    def getComando(self, cmd):
        return self.comandosDisponiveis[cmd]

if __name__ == '__main__':
    print("BEM VINDO PEQUENO ENGENHEIRO")
    c = ConstrucaoCasa()
    c.gerarDesafio()
    print("Neste jogo possui você irá construir uma casa")
    print("Você poderá construir cada objeto disponível por vez e então pintá-lo")
    print("Para criar, basta dar o comando 'Criar <nome da parte da casa que você quer>'.")
    print("Para pintar, basta dar o comando 'Pintar de <cor que você quiser>'")
    print("Para visualizar como a casa está ficando, basta dar o comando 'Mostrar Casa'")
    print("Caso queira fazer uma casa nova, basta dar o comando 'Demolir'")
    #TODO RESTO