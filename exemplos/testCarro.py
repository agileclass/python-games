import unittest

from Carro import Carro

class CarroTest(unittest.TestCase):

   def test_novoCarro(self):
      carro = Carro()
      self.assertEqual('off:0', carro.painel())

   def test_ligar(self):
      carro = Carro()
      carro.ligar();
      self.assertEqual('on:0', carro.painel())

   def test_acelerar(self):
      carro = Carro()
      carro.ligar();
      carro.acelerar()
      self.assertEqual('on:10', carro.painel())