import unittest
from fractions import Fraction


target = __import__('mysum')
sum = target.sum


class TestSum(unittest.TestCase):
    def test_list_int(self):
       
        data = [1, 2, 3]
        result = sum(data)
        print(result)
        self.assertEqual(result, 6)
        
        
    def test_list_fraction(self):
        
        data = [Fraction(2, 10), Fraction(4, 10), Fraction(2, 5)]
        result = sum(data)
        print(result)
        self.assertEqual(result, 1)
    
        
        
        
        
if __name__ == '__main__':
    unittest.main()

