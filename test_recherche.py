import unittest
from resolve import *


class testResolve(unittest.TestCase):

    def test_aSolution(self):
        self.assertEqual( aSolution([8,6,7,2,5,4,3,0,1], 0) , False )
        self.assertEqual( aSolution([1,3,8,5,7,6,4,2,0], 2) , True )