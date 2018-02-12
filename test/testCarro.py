import unittest

from exemplos.Carro import Carro

class CarroTest(unittest.TestCase):

   def test_novoCarro(self):
      carro = Carro()
      self.assertEqual('off:0', carro.situacao())


def suite():
    suite = unittest.TestSuite()
    suite.addTest(CarroTest())
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    test_suite = suite()
    runner.run(test_suite)
