from copy import copy
from logging import exception

# https://docs.python.org/3/library/operator.html


def swap(etat, i, j):
    """permute les valeurs à la pos i et j
    """
    tmp = etat[i]
    etat[i] = etat[j]
    etat[j] = tmp

###########################################################################
###########################################################################


class Noeud:
    n = None  # nb de lignes/colonnes
    heuristique = None

    def __init__(self, etat, pere, mvt, posvide):
        self.etat = etat
        self.h = Noeud.heuristique(etat)
        self.pere = pere
        self.mvt = mvt  # le mvt fait pour passer de pere à self NESO
        self.posvide = posvide  # la position du trou

    # 2 Noeuds sont égaux si leurs états sont égaux
    def __eq__(self, o):
        if(type(self) == type(o)):
            return self.etat == o.etat
        else:
            return False

    def __lt__(self, o):
        if type(o) == type(self):
            return self.f() < o.f()
        else:
            raise exception("Types differents, impossible de comparer")

    def mvts(self):
        """donne le chemin de l'etat actuel jusqu'à l'état initial
        """
        if (self.pere == None):
            return ""
        else:
            return self.mvt + self.pere.mvts()

    def g(self):
        """la longueur du plus chemin de l'etat actuel jusqu'à la racine
        """
        return len(self.mvts())

    def f(self):
        """fonction d'evaluation
        """
        return self.g() + self.h

    def adr(self):
        """retourne l'adr du noeud
        """
        return tuple(self.etat)

#######Deplacements################

    def mvSouth(self):
        """deplacement du trou vers le Sud
        retourne un nouveau noeud
        """
        etatfils = copy(self.etat)
        nvpos = self.posvide+3
        swap(etatfils, self.posvide, nvpos)
        fils = Noeud(etat=etatfils, pere=self, mvt="S", posvide=nvpos)
        return fils

    def mvNorth(self):
        """deplacement du trou vers le Nord
        retourne un nouveau noeud
        """
        etatfils = copy(self.etat)
        nvpos = self.posvide-3
        swap(etatfils, self.posvide, nvpos)
        fils = Noeud(etat=etatfils, pere=self, mvt="N", posvide=nvpos)
        return fils

    def mvEast(self):
        """deplacement du trou vers l'Est
        retourne un nouveau noeud
        """
        etatfils = copy(self.etat)
        nvpos = self.posvide+1
        swap(etatfils, self.posvide, nvpos)
        fils = Noeud(etat=etatfils, pere=self, mvt="E", posvide=nvpos)
        return fils

    def mvWest(self):
        """deplacement du trou vers l'ouest
        retourne un nouveau noeud
        """
        etatfils = copy(self.etat)
        nvpos = self.posvide-1
        swap(etatfils, self.posvide, nvpos)
        fils = Noeud(etat=etatfils, pere=self, mvt="O", posvide=nvpos)
        return fils

########################################

    def expand(self):
        """expanse un noeud
        retourne les fils
        """
        x = self.posvide % Noeud.n
        y = self.posvide // Noeud.n

        fils = []

        # match disponible dans python 3.10 mais pas 3.9 :(
        if(x == Noeud.n-1):  # (n-1, y)
            if(y == Noeud.n-1):  # (n-1, n-1)
                # move N, O
                fils.append(self.mvNorth())  # N
                fils.append(self.mvWest())  # O
                return fils
            elif(y == 0):  # (n-1, 0)
                # move O, S
                fils.append(self.mvWest())  # O
                fils.append(self.mvSouth())  # S
                return fils
            else:  # (n-1, _)
                # move N, S, O
                fils.append(self.mvNorth())  # N
                fils.append(self.mvSouth())  # S
                fils.append(self.mvWest())  # O
                return fils
        elif (x == 0):  # (0, y)
            if(y == 0):  # (0, 0)
                # move S, E
                fils.append(self.mvSouth())  # S
                fils.append(self.mvEast())  # E
                return fils
            elif(y == Noeud.n-1):  # (0, n-1)
                # move N, E
                fils.append(self.mvNorth())  # N
                fils.append(self.mvEast())  # E
                return fils
            else:  # (0, _)
                # move N, S, E
                fils.append(self.mvNorth())  # N
                fils.append(self.mvSouth())  # S
                fils.append(self.mvEast())  # E
                return fils
        else:  # (_, y)
            if(y == Noeud.n-1):  # (_, n-1)
                # move N, O, E
                fils.append(self.mvNorth())  # N
                fils.append(self.mvWest())  # O
                fils.append(self.mvEast())  # E
                return fils
            elif(y == 0):  # (_, 0)
                # move S, O, E
                fils.append(self.mvSouth())  # S
                fils.append(self.mvWest())  # O
                fils.append(self.mvEast())  # E
                return fils
            else:  # (_, _)
                # move N,S, E, O
                fils.append(self.mvNorth())  # N
                fils.append(self.mvSouth())  # S
                fils.append(self.mvWest())  # O
                fils.append(self.mvEast())  # E
                return fils
