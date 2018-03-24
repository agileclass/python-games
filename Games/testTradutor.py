import unittest

from Tradutor import Tradutor

class TradutorTest(unittest.TestCase):
    
    def test_ConstrutorInicializado(self):
        t = Tradutor()
        self.assertEqual(0, len(t.getCoresIngles()))
        self.assertEqual(0, len(t.getCoresPortugues()))

    def test_Desafio(self):
        t = Tradutor()
        t.gerarDesafio()
        self.assertEqual(len(t.getCoresIngles()), len(t.getCoresPortugues()))

    def test_Cores(self):
        t = Tradutor()
        t.gerarDesafio()
        self.assertEqual(t.compararReposta(0, 'yellow'), True)

if __name__ == '__main__':
    unittest.main()