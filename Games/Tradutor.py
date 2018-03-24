import random

class Tradutor(object):

    coresIngles = None
    coresPortugues = None
    indexCoresErradas = None

    def __init__(self):
        self.coresIngles=[]
        self.coresPortugues=[]
        self.indexCoresErradas=[]

    def getCoresIngles(self):
        return self.coresIngles

    def getCoresPortugues(self):
        return self.coresPortugues

    def gerarCoresIngles(self):
        self.coresIngles.append("Yellow")
        self.coresIngles.append("Blue")
        self.coresIngles.append("Red")
        self.coresIngles.append("Orange")
        self.coresIngles.append("Purple")
        self.coresIngles.append("Grey")
        self.coresIngles.append("Black")
        self.coresIngles.append("White")
        self.coresIngles.append("Pink")
        self.coresIngles.append("Navy Blue")

    def gerarCoresPortugues(self):
        self.coresPortugues.append("Amarelo")
        self.coresPortugues.append("Azul")
        self.coresPortugues.append("Vermelho")
        self.coresPortugues.append("Laranja")
        self.coresPortugues.append("Roxo")
        self.coresPortugues.append("Cinza")
        self.coresPortugues.append("Preto")
        self.coresPortugues.append("Branco")
        self.coresPortugues.append("Rosa")
        self.coresPortugues.append("Azul Marinho")

    def gerarDesafio(self):
        self.gerarCoresIngles()
        self.gerarCoresPortugues()

    def getPalavraIngles(self, idx):
        return self.coresIngles[idx]

    def getPalavraPortugues(self, idx):
        return self.coresPortugues[idx]

    def compararReposta(self, idx, resposta):
        if resposta.upper().strip() == self.getPalavraIngles(idx).upper().strip():
            return True

        self.indexCoresErradas.append(idx)
        return False 

if __name__ == '__main__':
    print("BEM VINDO AO JOGO TRADUTOR")
    t = Tradutor()
    t.gerarDesafio()
    print("--Este jogo possui " + str(len(t.coresIngles)) + " perguntas--")
    
    for x in range(0, len(t.coresIngles)): 
        resultado = input("Qual é a tradução para a cor " + t.getPalavraPortugues(x) + "? ")
        if t.compararReposta(x, resultado):
            print('Resposta correta!')
        else:
            print('Errrrooou! A resposta ficará para o final do questionario.')

    print('Você acertou ' + str(len(t.coresIngles) - len(t.indexCoresErradas)) + ' de ' + str(len(t.coresIngles)) + ' cores!')

    if len(t.indexCoresErradas) > 0:
        print('Aqui estão as respostas corretas dos erros:')
        for x in range(0, len(t.indexCoresErradas)):
            indexCorErrada = t.indexCoresErradas[x]
            print(str(t.getPalavraPortugues(indexCorErrada)) + ' = ' + str(t.getPalavraIngles(indexCorErrada)))
    else:
        print('Parabéns por gabaritar!')