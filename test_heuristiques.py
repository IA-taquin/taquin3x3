import unittest
from heuristiques import *



class testHeuristiques(unittest.TestCase):

    def test_heuristiques(self):
        self.assertEqual(fct_heuristique((1, 3, 8, 5, 7, 6, 4, 2, 0),
                                         poids[1], coeff_impair, 3), 54)
        self.assertEqual(fct_heuristique((1, 3, 8, 5, 7, 6, 4, 2, 0),
                                         poids[2], coeff_pair, 3), 88)
        self.assertEqual(fct_heuristique((1, 3, 8, 5, 7, 6, 4, 2, 0),
                                         poids[3], coeff_impair, 3), 22)
        self.assertEqual(fct_heuristique((1, 3, 8, 5, 7, 6, 4, 2, 0),
                                         poids[4], coeff_pair, 3), 90)
        self.assertEqual(fct_heuristique((1, 3, 8, 5, 7, 6, 4, 2, 0),
                                         poids[5], coeff_impair, 3), 22)
        self.assertEqual(fct_heuristique((1, 3, 8, 5, 7, 6, 4, 2, 0),
                                         poids[6], coeff_pair, 3), 18)
