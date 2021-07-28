import unittest
from unittest import TestLoader

if __name__ == '__main__':
    tests = TestLoader().discover('./tests')
    suite = unittest.TestSuite()
    suite.addTests(tests)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
