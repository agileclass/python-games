import unittest

from Carro import Carro

class CarroTest(unittest.TestCase):

   def test_novoCarro(self):
      carro = Carro()
      self.assertEqual('off:0', carro.situacao())
