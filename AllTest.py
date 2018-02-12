#!/usr/bin/python

import unittest as unittest

if __name__ == "__main__":
    all_tests = unittest.TestLoader().discover('test', pattern='*.py')
    unittest.TextTestRunner().run(all_tests)