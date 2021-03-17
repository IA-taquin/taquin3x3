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

    def test_Noeud_expand_NSEO(self):
        res_attendu = [[0, 8, 2, 3, 1, 5, 6, 7, 4],
                       [0, 1, 2, 3, 7, 5, 6, 8, 4],
                       [0, 1, 2, 3, 5, 8, 6, 7, 4],
                       [0, 1, 2, 8, 3, 5, 6, 7, 4]
                       ]
        Noeud.n = 3
        Noeud.heuristique = print
        n = Noeud(etat=[0, 1, 2, 3, 8, 5, 6, 7, 4],
                  pere=None, mvt="", posvide=4)
        fils = n.expand()
        fils_etats = []
        for x in fils:
            fils_etats.append(x.etat)
        self.assertEqual(fils_etats, res_attendu)

    def test_Noeud_expand_NSE_O(self):
        res_attendu = [[0, 8, 2, 3, 1, 5, 6, 7, 4],
                       [0, 1, 2, 3, 7, 5, 6, 8, 4],
                       [0, 1, 2, 3, 5, 8, 6, 7, 4]
                       ]
        Noeud.n = 3
        Noeud.heuristique = print
        n = Noeud(etat=[0, 1, 2, 3, 8, 5, 6, 7, 4],
                  pere=None, mvt="O", posvide=4)
        fils = n.expand()
        fils_etats = []
        for x in fils:
            fils_etats.append(x.etat)
        self.assertEqual(fils_etats, res_attendu)

    def test_Noeud_expand_NSEO_o(self):
        res_attendu = [
            [0, 1, 2, 6, 3, 5, 8, 7, 4],
            [0, 1, 2, 3, 8, 5, 6, 7, 4],
            [8, 1, 2, 0, 3, 5, 6, 7, 4]
        ]
        Noeud.n = 3
        Noeud.heuristique = print
        n = Noeud(etat=[0, 1, 2, 3, 8, 5, 6, 7, 4],
                  pere=None, mvt="", posvide=4)
        fils1 = n.expand()
        for e in fils1:
            if e.etat == [0, 1, 2, 8, 3, 5, 6, 7, 4]:
                fils = e.expand()
        fils_etats = []
        for x in fils:
            fils_etats.append(x.etat)
        for l in fils_etats:
            self.assertIn(l, res_attendu)
