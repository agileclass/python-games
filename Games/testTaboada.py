import unittest

from Taboada import Taboada

class TaboadaTest(unittest.TestCase):
    
    def test_ConstrutorInicializado(self):
        c = Taboada(9.0)
        self.assertEqual(9.0, c.valor)

    def test_ConstrutorVazio(self):
        c = Taboada()
        self.assertEqual(0.0, c.valor)

    def test_Soma(self):
        c = Taboada()
        c.soma(4)
        c.soma(10)
        self.assertEqual(14, c.valor)

    def test_Subtracao(self):
        c = Taboada(10.0)
        c.subtracao(3.0)
        self.assertEqual(7.0, c.valor)

if __name__ == '__main__':
    unittest.main()