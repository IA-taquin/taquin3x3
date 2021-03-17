

class Noeud:

    def __init__(self, etat, heuristique, pere, mvt, posvide):
        self.etat = etat
        self.h = heuristique(etat)
        self.pere = pere
        self.mvt = mvt  # le mvt fait pour passer de pere à self
        self.posvide = posvide  # la position du trou

    # 2 Noeuds sont égaux si leurs états sont égaux
    def __eq__(self, o):
        if(type(self) == type(o)):
            return self.etat == o.etat
        else:
            return False

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
        return tuple(self.etat)

    #TODO: Expansion d'un noeud
    def expand(self):
        """expanse un noeud
        retourne les fils
        """
