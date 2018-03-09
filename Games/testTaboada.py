import unittest


from Taboada import Taboada

class TaboadaTest(unittest.TestCase):
    
    def test_ConstrutorInicializado(self):
        t = Taboada()
        self.assertEqual(0, t.getV1())
        self.assertEqual(0, t.getV2())

    def test_Desafio(self):
        t = Taboada()
        t.gerarDesafio()
        self.assertNotEqual(0, t.getV1())
        self.assertNotEqual(0, t.getV2())

    def test_Resultado(self):
        t = Taboada()
        t.gerarDesafio()
        self.assertEqual(t.getV1() * t.getV2(), t.getResultado())

if __name__ == '__main__':
    unittest.main()