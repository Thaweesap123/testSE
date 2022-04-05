import unittest

class Calculator_number:
    num1 = 0
    num2 = 0
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
    def Add(self):
        return self.num1 + self.num2
    def Minus(self):
        return self.num1 - self.num2
    def Multiply(self):
        return self.num1 * self.num2
    def Divide(self):
        if self.num1 > 0 and self.num2:
            return self.num1 / self.num2
        else:
            return 'Error'

class TestCalculator(unittest.TestCase):
    def testAdd(self):
        for num1 in range(9):
            for num2 in range(9):
                cal = Calculator_number(num1,num2)
                self.assertEqual(cal.Add(),(num1+num2))
    def testMinus(self):
        for num1 in range(9):
            for num2 in range(9):
                cal = Calculator_number(num1,num2)
                self.assertEqual(cal.Minus(),(num1-num2))
    def testMultiply(self):
        for num1 in range(9):
            for num2 in range(9):
                cal = Calculator_number(num1,num2)
                self.assertEqual(cal.Multiply(),(num1*num2))
    def testDivide(self):
        for num1 in range(9):
            for num2 in range(9):
                cal = Calculator_number(num1,num2)
                if num1 > 0 and num2 > 0:
                    self.assertEqual(cal.Divide(),(num1/num2))
                else:
                    self.assertEqual(cal.Divide(),'Error')
if __name__ == '__main__':
    unittest.main()