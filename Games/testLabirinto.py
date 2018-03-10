import unittest

from Labirinto import labirinto

class LaribirintoTest(unittest.TestCase):
    
    def test_ConstrutorInicializado(self):
        t = Labirinto()
        self.assertEqual(0, t.getV1())
        self.assertEqual(0, t.getV2())

    def test_Desafio(self):
        t = Labirinto()
        t.gerarDesafio()
        self.assertNotEqual(0, t.getV1())
        self.assertNotEqual(0, t.getV2())

    def test_Resultado(self):
        t = Labirinto()
        t.gerarDesafio()
        self.assertEqual(t.getV1() * t.getV2(), t.getResultado())

if __name__ == '__main__':
    unittest.main()