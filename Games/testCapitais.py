import unittest

from Capitais import Capitais

class CapitaisTest(unittest.TestCase):
    def test_desafio(self):
        capitais = Capitais()
        self.assertEqual(len(capitais.perguntas), len(capitais.respostas))

    def test_capitais(self):
        capitais = Capitais()
        self.assertEqual(capitais.verifica_resposta(0, 'Curitiba'), True)
        self.assertEqual(capitais.verifica_resposta(1, 'São Paulo'), True)
        self.assertEqual(capitais.verifica_resposta(2, 'Rio de Janeiro'), True)
        self.assertEqual(capitais.verifica_resposta(3, 'Florianópolis'), True)

if __name__ == '__main__':
    unittest.main()