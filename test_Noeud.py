import unittest
from Noeud import Noeud, swap


class testNoeud(unittest.TestCase):

    def test_Noeud_mvt(self):
        pass

    def test_Noeud_mvSouth(self):
        Noeud.heuristique = print
        Noeud.n = 3
        n = Noeud([0, 1, 2, 3, 8, 5, 6, 7, 4], None, "", 4)
        f = n.mvSouth()
        self.assertEqual(f.etat, [0,1,2,3,7,5,6,8,4])


    def test_Noeud_swap(self):
        etat = [0, 1, 2, 3]
        print(etat)
        print("swaping 0 & 1")
        swap(etat, 0, 1)
        print(etat)
        self.assertEqual(etat, [1, 0, 2, 3])
        