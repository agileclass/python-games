class Labirinto(object):

    n = None
    m = None
    mensagem = None
    countErro = None
    isAcerto = None

    def __init__(self):
        self.n=4
        self.m=4
        self.countErro=1
        self.isAcerto=False

    def getn(self):
        return self.n

    def getm(self):
        return self.m

    def getmensagem(self):
        return self.mensagem

    def getcounterro(self):
        return self.countErro

    def getisacerto(self):
        return self.isAcerto

if __name__ == '__main__':
    print("BEM VINDO AO JOGO LABIRINTO")
    l = Labirinto()

    while not l.isAcerto:
        a = [0] * l.n
        for i in range(l.n):
            a[i] = ['-'] * l.m
        a[0][0] = '*'
        a[3][3] = 'X'
        for t in range(l.n):
            print(a[t])

        testVar = input("ENTRE A SEQUENCIA PARA MOVER O * ATÉ O X:")
        cima = testVar.count('C')
        baixo = testVar.count('B')
        direita = testVar.count('D')
        esquerda = testVar.count('E')
        y = direita - esquerda
        x = baixo - cima
        if x < 0 or y < 0:
            l.mensagem = 'Que pena! Tente novamente'
            l.isAcerto = False
            l.countErro = l.countErro + 1
        if y == 3 and x == 3:
            l.mensagem = 'Parabens! Voce atingiu o objetivo. Você acertou em '+ str(l.countErro) + ' tentativas'
            l.isAcerto = True
        else:
            l.mensagem = 'Que pena! Tente novamente'
            l.isAcerto = False
            l.countErro = l.countErro + 1
        if x >= 0 and y >= 0:
            a[x][y] = '*' 
        a[0][0] = '-'
        for t in range(l.n):
            print(a[t])
        print(l.mensagem)