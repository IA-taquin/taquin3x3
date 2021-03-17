import unittest
from Noeud import Noeud


class testNoeud(unittest.TestCase):
    
    def test_Noeud(self):
        n1 = Noeud(pere = None, mvt = "", etat = "init 1", heuristique=print)
        n2 = Noeud(pere = n1, mvt = "N", etat = "init 2 N", heuristique=print)
        n3 = Noeud(pere = n2, mvt = "S", etat = "init 3 S", heuristique=print)
        n4 = Noeud(pere = n3, mvt = "E", etat = "init 4 E", heuristique=print)
        n5 = Noeud(pere = n4, mvt = "O", etat = "init 5 O", heuristique=print)
        chemin = n5.mvts()
        print("chemin = "+chemin)
        self.assertEqual(chemin, "OESN")
        self.assertEqual(len(chemin), 4)