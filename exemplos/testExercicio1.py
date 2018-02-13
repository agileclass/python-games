import unittest

import Exercicio1

class Exercicio1Test(unittest.TestCase):
    
    def test_ConstrutorInicializado(self):
        l = Exercicio1.ex_01_ler_arquivo_csv()
        self.assertEqual(20, len(l))