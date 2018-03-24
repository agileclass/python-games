import random

class Capitais(object):

    perguntas = None
    respostas = None

    def __init__(self):
        self.perguntas=[]
        self.respostas=[]

        self.perguntas.append("do Paraná")
        self.perguntas.append("de São Paulo")
        self.perguntas.append("do Rio de Janeiro")
        self.perguntas.append("de Santa Catarina")
        
        self.respostas.append("Curitiba")
        self.respostas.append("São Paulo")
        self.respostas.append("Rio de Janeiro")
        self.respostas.append("Florianópolis")
        
    def verifica_resposta(self, idx, resposta):
        if resposta.upper().strip() == self.respostas[idx].upper().strip():
            return True

if __name__ == '__main__':
    acertos = 0
    erros=[]

    capitais = Capitais()
        
    for i in range(0, len(capitais.perguntas)):
        resposta = input("Qual a capital " + capitais.perguntas[i] + "? => ")

        if capitais.verifica_resposta(i, resposta):
            acertos = acertos + 1
            print('Resposta correta!\n')
        else:
            erros.append(i)
            print('Reposta errada! Volte para a escola...\n')

    print('------------- RESULTADO ---------------\n')
    print('Você acertou ' + str(acertos) + ' perguntas.')

    for n in range(0, len(erros)):
        print("Você errou a capital " + capitais.perguntas[erros[n]] + " que é " + capitais.respostas[erros[n]] )
    
    print('\n------------- FIM ---------------\n')

