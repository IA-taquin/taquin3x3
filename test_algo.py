import unittest
from algo import aSolution


class testResolve(unittest.TestCase):

    def test_aSolution(self):
        self.assertFalse( aSolution([8,6,7,2,5,4,3,0,1], 0))
        self.assertTrue( aSolution([1,3,8,5,7,6,4,2,0], 2))