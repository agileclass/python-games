import unittest
import _io
import sys
import unittest.mock

from .Quiz import Quiz

class QuizTest(unittest.TestCase):

    def setUp(self):
        self.quiz = Quiz()

    def get_captura_saida(self):
        captura_saida = _io.StringIO()
        sys.stdout = captura_saida

        return captura_saida

    def criar_pergunta_resposta_para_teste(self):
        self.pergunta = "Verdadeiro ou falso? Python também é o nome de uma linguagem de programação."
        self.resposta = "Verdadeiro"
        self.quiz.criar_pergunta(self.pergunta, self.resposta)

    # Quando o jogo é iniciado, então não há perguntas e respostas ainda, e perguntas e respostas já foram inicializados
    def test_init(self):
        self.assertEqual(0, len(self.quiz.perguntas))
        self.assertEqual(0, len(self.quiz.respostas))
        self.assertIsNotNone(self.quiz.perguntas)
        self.assertIsNotNone(self.quiz.respostas)

    # Quando crio uma pergunta e resposta, então a quantidade de perguntas e respostas deixa de ser zero
    def test_criar(self):
        self.criar_pergunta_resposta_para_teste()

        self.assertGreater(len(self.quiz.perguntas), 0)
        self.assertGreater(len(self.quiz.respostas), 0)

    # Quando listo as perguntas sem ter criado nenhuma ainda, então uma mensagem apropriada é exibida
    def test_listar_perguntas_nenhuma_pergunta_criada(self):
        saida = self.get_captura_saida()
        self.quiz.listar_perguntas()
        self.assertEqual("Nenhuma pergunta foi criada ainda.", saida.getvalue().strip())

    # Quando listo as perguntas após já ter criado alguma, então elas são exibidas normalmente
    def test_listar_perguntas_pergunta_criada(self):
        self.criar_pergunta_resposta_para_teste()

        saida = self.get_captura_saida()
        self.quiz.listar_perguntas()
        self.assertEqual(f"Pergunta: \"{self.pergunta}\", posição: 0", saida.getvalue().strip())

    # Quando listo as respostas sem ter criado nenhuma ainda, então uma mensagem apropriada é exibida
    def test_listar_respostas_nenhuma_pergunta_criada(self):
        saida = self.get_captura_saida()
        self.quiz.listar_respostas()
        self.assertEqual("Nenhuma pergunta foi criada ainda, portanto não há respostas para listar.",
                         saida.getvalue().strip())

    # Quando listo as respostas após já ter criado alguma, então elas são exibidas normalmente
    def test_listar_respostas_pergunta_criada(self):
        self.criar_pergunta_resposta_para_teste()

        saida = self.get_captura_saida()
        self.quiz.listar_respostas()
        self.assertEqual(f"Resposta: \"{self.resposta}\", posição: 0", saida.getvalue().strip())

    # Quando listo tudo sem ter criado nenhuma pergunta ainda, então uma mensagem apropriada é exibida
    def test_listar_tudo_nenhuma_pergunta_criada(self):
        saida = self.get_captura_saida()
        self.quiz.listar_tudo()
        self.assertEqual("Nenhuma pergunta foi criada ainda.", saida.getvalue().strip())

    # Quando listo as tudo após já ter criado alguma pergunta, então elas são exibidas normalmente
    def test_listar_tudo_pergunta_criada(self):
        self.criar_pergunta_resposta_para_teste()

        saida = self.get_captura_saida()
        self.quiz.listar_tudo()
        self.assertEqual(f"Pergunta: \"{self.pergunta}\", Resposta: \"{self.resposta}\", posição: 0", saida.getvalue().strip())

    # Quando tento alterar uma pergunta sem ter criado alguma antes, então uma mensagem apropriada é exibida
    def test_alterar_pergunta_nenhuma_pergunta_criada(self):
        saida = self.get_captura_saida()
        self.quiz.alterar_pergunta(0, "Minha nova pergunta?")

        self.assertEqual("Nenhuma pergunta foi criada ainda.", saida.getvalue().strip())

    # Quando tento alterar uma pergunta numa posição válida, então ela é alterada com sucesso
    def test_alterar_pergunta_posicao_valida(self):
        self.criar_pergunta_resposta_para_teste()

        nova_pergunta = "Essa é minha nova pergunta?"
        posicao = 0

        self.quiz.alterar_pergunta(posicao, nova_pergunta)

        self.assertEqual(self.quiz.perguntas[posicao], nova_pergunta)

    # Quando tento alterar uma pergunta numa posição inválida, então uma mensagem apropriada é exibida
    def test_alterar_pergunta_posicao_invalida(self):
        self.criar_pergunta_resposta_para_teste()

        nova_pergunta = "Essa é minha nova pergunta?"
        posicao = 1

        saida = self.get_captura_saida()
        self.quiz.alterar_pergunta(posicao, nova_pergunta)

        self.assertEqual(f"Não há pergunta na posição {posicao}", saida.getvalue().strip())

    # Quando tento alterar uma resposta sem ter criado alguma antes, então uma mensagem apropriada é exibida
    def test_alterar_resposta_nenhuma_pergunta_criada(self):
        saida = self.get_captura_saida()
        self.quiz.alterar_resposta(0, "Minha nova resposta")

        self.assertEqual("Nenhuma pergunta foi criada ainda, portanto não há respostas para alterar.",
                         saida.getvalue().strip())

    # Quando tento alterar uma resposta numa posição válida, então ela é alterada com sucesso
    def test_alterar_resposta_posicao_valida(self):
        self.criar_pergunta_resposta_para_teste()

        nova_resposta = "Essa é minha nova resposta"
        posicao = 0

        self.quiz.alterar_resposta(posicao, nova_resposta)

        self.assertEqual(self.quiz.respostas[posicao], nova_resposta)

    # Quando tento alterar uma resposta numa posição inválida, então uma mensagem apropriada é exibida
    def test_alterar_resposta_posicao_invalida(self):
        self.criar_pergunta_resposta_para_teste()

        nova_resposta = "Essa é minha nova resposta"
        posicao = 1

        saida = self.get_captura_saida()
        self.quiz.alterar_resposta(posicao, nova_resposta)

        self.assertEqual(f"Não há resposta na posição {posicao}", saida.getvalue().strip())

    # Quando tento testar uma pergunta sem ter criado alguma antes, então uma mensagem apropriada é exibida
    def test_testar_pergunta_nenhuma_pergunta_criada(self):
        saida = self.get_captura_saida()
        self.quiz.testar(0)

        self.assertEqual("Nenhuma pergunta foi criada ainda.", saida.getvalue().strip())

    # Quando executo o quiz e respondo corretamente, então uma mensagem de resumo de acertos é exibida ao final
    @unittest.mock.patch('builtins.input', return_value="Verdadeiro")
    def test_executar_quiz_resposta_correta(self, input):
        self.criar_pergunta_resposta_para_teste()

        saida = self.get_captura_saida()

        self.quiz.executar_quiz()

        self.assertEqual("Resposta correta!\n\n------------- RESULTADO ---------------\n\nVocê acertou 1 pergunta.\n\n"
                         "------------- FIM ---------------".strip(), saida.getvalue().strip())

    # Quando executo o quiz e respondo erroneamente, então uma mensagem de resumo de acertos é exibida ao final
    @unittest.mock.patch('builtins.input', return_value="Uma resposta errada")
    def test_executar_quiz_resposta_errada(self, input):
        self.criar_pergunta_resposta_para_teste()

        saida = self.get_captura_saida()

        self.quiz.executar_quiz()

        self.assertEqual("Resposta errada!\n\n------------- RESULTADO ---------------\n\nVocê acertou 0 perguntas.\n"
                         f"Você errou a pergunta \"{self.pergunta}\". Resposta: {self.resposta}\n\n------------- FIM ---------------",
                         saida.getvalue().strip())

    # Quando tento testar uma pergunta numa posição inválida, então uma mensagem apropriada é exibida
    def test_testar_pergunta_posicao_invalida(self):
        self.criar_pergunta_resposta_para_teste()

        posicao = 1

        saida = self.get_captura_saida()
        self.quiz.testar(posicao)

        self.assertEqual(f"Não há pergunta na posição {posicao}", saida.getvalue().strip())

    # Quando verifico a resposta e ela está correta, então retorna True
    def test_verificar_resposta_certa(self):
        self.criar_pergunta_resposta_para_teste()

        self.assertEqual(self.quiz.verificar_resposta(0, self.resposta), True)

    # Quando verifico a resposta e ela está errada, então retorna False
    def test_verificar_resposta_errada(self):
        self.criar_pergunta_resposta_para_teste()

        self.assertEqual(self.quiz.verificar_resposta(0, "Resposta errada"), False)

    # Quando tento executar o quiz sem ter criado alguma pergunta, então uma mensagem apropriada é exibida
    def test_executar_quiz_nenhuma_pergunta(self):
        saida = self.get_captura_saida()

        self.quiz.executar_quiz()

        self.assertEqual("Nenhuma pergunta foi criada ainda.", saida.getvalue().strip())

if __name__ == '__main__':
    unittest.main()