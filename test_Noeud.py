import unittest
from Noeud import Noeud, swap


class testNoeud(unittest.TestCase):

    def test_Noeud_mvt(self):
        Noeud.heuristique = print
        n1 = Noeud(pere=None, mvt="", etat="etat 1", posvide=5)
        n2 = Noeud(pere=n1, mvt="N", etat="etat 2 atteint en faisant N", posvide=5)
        n3 = Noeud(pere=n2, mvt="S", etat="etat 3 atteint en faisant S", posvide=5)
        n4 = Noeud(pere=n3, mvt="E", etat="etat 4 atteint en faisant E", posvide=5)
        n5 = Noeud(pere=n4, mvt="O", etat="etat 5 atteint en faisant O", posvide=5)
        chemin = n5.mvts()
        print("chemin de noeud actuel jusqu'à racine = "+chemin)
        self.assertEqual(chemin, "OESN")
        longueur = len(chemin)
        print("longueur = %s" % longueur)
        self.assertEqual(longueur, 4)

    def test_Noeud_swap(self):
        etat = [0, 1, 2, 3]
        print(etat)
        print("swaping 0 & 1")
        swap(etat, 0, 1)
        print(etat)
        self.assertEqual(etat, [1, 0, 2, 3])
        
    def test_Noeud_expand(self):
        Noeud.heuristique = print
        Noeud.n = 3
        n1 = Noeud(etat = [1,3,8,5,7,6,4,2,0], pere = None, mvt="", posvide=2)
        n1_1 = Noeud(etat = [1,8,3,5,7,6,4,2,0], pere = n1, mvt="O", posvide=1)
        n1_2 = Noeud(etat = [1,3,6,5,7,8,4,2,0], pere = n1, mvt="S", posvide=5)
        fils_attendus = [n1_1, n1_2]
        print("---Expand()---")
        fils_generes = n1.expand()
        for f in fils_generes:
            self.assertIn(f, fils_attendus)