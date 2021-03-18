import unittest
from Noeud import Noeud, swap


class testNoeud(unittest.TestCase):

    def test_Noeud_mvt(self):
        Noeud.heuristique = print
        n1 = Noeud(pere=None, mvt="", etat="init 1", posvide=5)
        n2 = Noeud(pere=n1, mvt="N", etat="init 2 N", posvide=5)
        n3 = Noeud(pere=n2, mvt="S", etat="init 3 S", posvide=5)
        n4 = Noeud(pere=n3, mvt="E", etat="init 4 E", posvide=5)
        n5 = Noeud(pere=n4, mvt="O", etat="init 5 O", posvide=5)
        chemin = n5.mvts()
        print("chemin = "+chemin)
        self.assertEqual(chemin, "OESN")
        self.assertEqual(len(chemin), 4)

    def test_Noeud_swap(self):
        etat = [0, 1, 2, 3]
        print(etat)
        print("swaping 0 & 1")
        swap(etat, 0, 1)
        print(etat)
        self.assertEqual(etat, [1, 0, 2, 3])
        