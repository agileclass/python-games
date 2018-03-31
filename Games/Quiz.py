import re


class Quiz(object):
    perguntas = None
    respostas = None

    def __init__(self):
        self.perguntas = []
        self.respostas = []

    def verificar_resposta(self, idx, resposta):
        return resposta.upper().strip() == self.respostas[idx].upper().strip()

    def criar_pergunta(self, pergunta, resposta):
        self.perguntas.append(pergunta)
        self.respostas.append(resposta)

    def exibir_ajuda(self):
        print("\n================= Comandos =================")
        print("Para criar uma nova pergunta e resposta, utilize o comando: criar(\"Uma pergunta qualquer\", "
              "\"Resposta para a pergunta\")")
        print("Para listar as perguntas, utilize o comando: listar_perguntas()")
        print("Para listar as respostas, utilize o comando: listar_respostas()")
        print("Para listar as perguntas e respostas, utilize o comando: listar_tudo()")
        print("Para alterar uma pergunta, utilize o comando: alterar_pergunta(posicao, \"Nova pergunta qualquer\")")
        print("Para alterar uma resposta, utilize o comando: alterar_resposta(posicao, \"Nova resposta qualquer\")")
        print("Para testar uma pergunta específica, utilize o comando: testar(posicao)")
        print("Para executar o quiz, utilize o comando: executar_quiz()")
        print("Para finalizar o programa, utilize o comando: sair()")
        print("Para exibir esse menu de ajuda novamente, utilize o comando: ajuda()")
        print("============================================")

    def listar_perguntas(self):
        if len(self.perguntas) == 0:
            print("Nenhuma pergunta foi criada ainda.")
        else:
            for i in range(len(self.perguntas)):
                print("Pergunta: \"" + self.perguntas[i] + "\", posição: " + str(i))

    def listar_respostas(self):
        if len(self.perguntas) == 0:
            print("Nenhuma pergunta foi criada ainda, portanto não há respostas para listar.")
        else:
            for i in range(len(self.respostas)):
                print("Resposta: \"" + self.respostas[i] + "\", posição: " + str(i))

    def listar_tudo(self):
        if len(self.perguntas) == 0:
            print("Nenhuma pergunta foi criada ainda.")
        else:
            for i in range(len(self.perguntas)):
                print(
                    "Pergunta: \"" + self.perguntas[i] + "\", Resposta: \"" + self.respostas[i] + "\", posição: " + str(
                        i))

    def alterar_pergunta(self, posicao, nova_pergunta):
        if len(self.perguntas) == 0:
            print("Nenhuma pergunta foi criada ainda.")
        elif len(self.perguntas) > posicao:
            self.perguntas[posicao] = nova_pergunta
        else:
            print("Não há pergunta na posição " + str(posicao))

    def alterar_resposta(self, posicao, nova_resposta):
        if len(self.perguntas) == 0:
            print("Nenhuma pergunta foi criada ainda, portanto não há respostas para alterar.")
        elif len(self.respostas) > posicao:
            self.respostas[posicao] = nova_resposta
        else:
            print("Não há resposta na posição " + str(posicao))

    def testar(self, posicao):
        if len(self.perguntas) == 0:
            print("Nenhuma pergunta foi criada ainda.")
        elif len(self.perguntas) > posicao:
            resposta = input(self.perguntas[posicao] + "\n")

            if self.verificar_resposta(posicao, resposta):
                print('Resposta correta!\n')
            else:
                print('Reposta errada!\n')
        else:
            print("Não há pergunta na posição " + str(posicao))

    def executar_quiz(self):
        acertos = 0
        erros = []

        if len(self.perguntas) == 0:
            print("Nenhuma pergunta foi criada ainda.")
        else:
            for i in range(0, len(self.perguntas)):
                resposta = input(self.perguntas[i] + "\n")

                if self.verificar_resposta(i, resposta):
                    acertos = acertos + 1
                    print('Resposta correta!\n')
                else:
                    erros.append(i)
                    print('Reposta errada!\n')

            print('------------- RESULTADO ---------------\n')
            if acertos == 1:
                print('Você acertou ' + str(acertos) + ' pergunta.')
            else:
                print('Você acertou ' + str(acertos) + ' perguntas.')

            for n in range(0, len(erros)):
                print(
                    "Você errou a pergunta \"" + self.perguntas[erros[n]] + "\". Resposta: " + self.respostas[erros[n]])

            print('\n------------- FIM ---------------\n')


if __name__ == '__main__':
    quiz = Quiz()

    quiz.exibir_ajuda()

    comando = input("\nComando => ")

    while comando != "sair()":
        if comando == "ajuda()":
            # Comando de ajuda
            quiz.exibir_ajuda()
        elif re.match("^criar\(\".*\" *, *\".*\"\)$", comando):
            # Comando de criar pergunta
            pesquisa = re.search("criar\(\"(.*)\" *, *\"(.*)\"\)", comando)

            if pesquisa:
                pergunta = pesquisa.group(1)
                resposta = pesquisa.group(2)

                quiz.criar_pergunta(pergunta, resposta)
        elif comando == "listar_perguntas()":
            # Comando de listar as perguntas e seus respectivos índices
            quiz.listar_perguntas()
        elif comando == "listar_respostas()":
            # Comando de listar as respostas e seus respectivos índices
            quiz.listar_respostas()
        elif comando == "listar_tudo()":
            # Comando de listar as respostas e as perguntas, e seus respectivos índices
            quiz.listar_tudo()
        elif re.match("^alterar_pergunta\((\d+) *, *\"(.*)\"\)$", comando):
            # Comando de alterar uma pergunta em um dado índice

            pesquisa = re.search("alterar_pergunta\((\d+) *, *\"(.*)\"\)", comando)

            if pesquisa:
                posicao = pesquisa.group(1)
                nova_pergunta = pesquisa.group(2)

                quiz.alterar_pergunta(int(posicao), nova_pergunta)
        elif re.match("^alterar_resposta\((\d+) *, *\"(.*)\"\)$", comando):
            # Comando de alterar uma resposta em um dado índice

            pesquisa = re.search("alterar_resposta\((\d+) *, *\"(.*)\"\)", comando)

            if pesquisa:
                posicao = pesquisa.group(1)
                nova_resposta = pesquisa.group(2)

                quiz.alterar_resposta(int(posicao), nova_resposta)
        elif re.match("^testar\((\d+)\)$", comando):
            # Comando de testar uma pergunta específica dado o seu índice

            pesquisa = re.search("testar\((\d+)\)", comando)

            if pesquisa:
                posicao = pesquisa.group(1)

                quiz.testar(int(posicao))
        elif comando == "executar_quiz()":
            # Comando de jogar o quiz com todas as perguntas
            quiz.executar_quiz()
        else:
            print("Comando " + comando + " não encontrado. Para consultar a lista de comandos digite ajuda()")

        comando = input("\nComando => ")
