import unittest

from exemplos.Calculadora import Calculadora

class AllTest (unittest.TestCase):

    def runTest(self):
        """ Test addition and succeed. """

        self.assertTrue(1+1 == 2)

def suite():
    suite = unittest.TestSuite()
    suite.addTest(AllTest())
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    test_suite = suite()
    runner.run(test_suite)
