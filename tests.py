import unittest
from main import user_input_features_test, X

class MyTestCase(unittest.TestCase):
    
    def test_user_input_feature(self):
       Age, GrLivArea, LotFrontage, LotArea, GarageArea, Fence, Pool= user_input_features_test()
       self.assertEqual(Age, '35')
       self.assertEqual(GrLivArea, '1522')
       self.assertEqual(LotFrontage, '70')
       self.assertEqual(LotArea, '10610')
       self.assertEqual(GarageArea, '478')
       self.assertFalse(Fence, False)
       self.assertFalse(Pool, False)

if __name__ == '__main__':
    unittest.main()
