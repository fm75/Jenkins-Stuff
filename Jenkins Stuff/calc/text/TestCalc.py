'''
Created on Aug 3, 2013

@author: fred
'''
import unittest
from calc.calculator import Calculator

class Test(unittest.TestCase):

  def testAdd(self):
    calculator = Calculator ()
    self.assertEqual(4, calculator.add (a=1, b=3))

  def testSub (self):
    calculator = Calculator ()
    self.assertEqual(2, calculator.sub(b=3,a=1))
     
  def testMultiply (self):
    calculator = Calculator ()
    self.assertEqual(3, calculator.Multiply(b=3,a=1))
     
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()