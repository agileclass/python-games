import unittest

from Carro import Carro

class CarroTest(unittest.TestCase):

   def test_novoCarro(self):
      carro = Carro()
      self.assertEqual('off:0', carro.painel())

   def test_ligar(self):
      carro = Carro()
      carro.ligar()
      self.assertEqual('on:0', carro.painel())

   def test_delisgar(self):
      carro = Carro()
      carro.desligar()
      self.assertEqual('off:0', carro.painel())

   def test_acelerar(self):
      carro = Carro()
      carro.ligar()
      carro.acelerar()
      self.assertEqual('on:10', carro.painel())

   def test_freiar(self):
      carro = Carro()
      carro.ligar()
      carro.acelerar()
      carro.acelerar()
      carro.acelerar()
      self.assertEqual('on:30', carro.painel())
      carro.freiar()
      self.assertEqual('on:20', carro.painel())
      carro.freiar()
      self.assertEqual('on:10', carro.painel())

if __name__ == '__main__':
    print("main")

