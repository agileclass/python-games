import unittest

from exemplos.Calculadora import Calculadora

class CalculadoraTest(unittest.TestCase):
    
    def test_ConstrutorInializado(self):
        c = Calculadora(9.0)
        self.assertEqual(9.0, c.valor)

    def test_ConstrutorVazio(self):
        c = Calculadora()
        self.assertEqual(0.0, c.valor)

    def test_Soma(self):
        c = Calculadora()
        c.soma(4)
        c.soma(10)
        self.assertEqual(14, c.valor)

    def test_Subtracao(self):
        c = Calculadora(10.0)
        c.subtracao(3.0)
        self.assertEqual(7.0, c.valor)

def suite():
    suite = unittest.TestSuite()
    suite.addTest(CalculadoraTest())
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    test_suite = suite()
    runner.run(test_suite)