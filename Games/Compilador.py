# Teste de comentário
# Segundo commit
import random

class Variavel(object):

    nome = None
    valor = None

class Compilador(object):

    arrayList = None
    v1 = None
    v2 = None

    def __init__(self):
        self.v1=0
        self.v2=0
        self.arrayList = []

    def getV1(self):
        return self.v1

    def getV2(self):
        return self.v2

    def getResultado(self):
        return self.v1 * self.v2

if __name__ == '__main__':
    print("BEM VINDO AO JOGO COMPILADOR")
    print("---------------OPÇOES-------------------------")
    print("PARA CRIAR PRIMEIRA VARIAVEL: gaveta1 RECEBE 10;")
    print("PARA CRIAR SEGUNDA VARIAVEL: gaveta2 RECEBE 20;")
   
    print("SUAS OPÇÕES PARA CRIAR SEU COMANDO SÃO: ")

    print("gaveta3 RECEBE gaveta1 SOMA gaveta2;")
    print("gaveta3 RECEBE gaveta1 SUBTRAIA gaveta2;")
    print("gaveta3 RECEBE gaveta1 DIVIDA gaveta2;")
    print("gaveta3 RECEBE gaveta1 MULTIPLICA gaveta2;")

    print("PARA MOSTRAR UMA VARIAVEL: MOSTRA gaveta3;")
    print("----------------------------------------")
    
    comando = input("\nINSIRA SEU COMANDO: ")
        
    strings = comando.split(" ")

    if(strings[1] == "RECEBE"):
        obj = Variavel()
        obj.nome = strings[0]
        obj.valor = strings[2]
        arrayList.append(obj)
        print(arrayList)









   
