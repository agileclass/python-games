import random

class ClassificacaoAnimais(object):
    v1 = None
    v2 = None
    animais = ["Macaco", "Leao", "Jacare", "Elefante", "Cascavel", "Tilapia"]
    respostas = [1,1,2,1,2]

    def __init__(self):
        self.v1=0  
           
if __name__ == '__main__':
    print("BEM VINDO AO JOGO DE CLASSIFICACAO DE ANIMAIS...")
    c = ClassificacaoAnimais()
    acumulador = 0
    elementos = 0
    while elementos < 5:
        print("O Animal " + c.animais[elementos] + " Pertence a qual classificação?") 
        print("1 = Mamifero ")
        print("2 = Reptil ")
        print("3 = Anfibio ")
        resultado = input()
        if str(resultado) == str(c.respostas[acumulador]):
            print("Você acertou!!!!")  
            acumulador = acumulador + 1          
        else:
            print("Você errou!!!")
        elementos = elementos + 1        
    percentual = round((acumulador / 5) * 100, 2)
    if(percentual==0):
        print("Você errou todas as questões fera, tem que estudar mais, porém não desista!!! ")
    else:
        print("Você acertou " + str(percentual) + "% questões!!")
    
        
    