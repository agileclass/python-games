import unittest

from Labirinto import Labirinto

class LaribirintoTest(unittest.TestCase):
    
    def test_ConstrutorInicializado(self):
        l = Labirinto()
        self.assertEqual(4, l.getm())
        self.assertEqual(4, l.getn())

    def test_Matriz(self):
        l = Labirinto()
        self.assertNotEqual(0, l.getm())
        self.assertNotEqual(0, l.getn())

if __name__ == '__main__':
    unittest.main()