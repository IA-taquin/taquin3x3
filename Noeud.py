from copy import copy


def swap(etat, i, j):
    """permute les valeurs à la pos i et j
    """
    tmp = etat[i]
    etat[i] = etat[j]
    etat[j] = tmp


class Noeud:
    n = None  # nb de lignes/colonnes
    heuristique = None

    def __init__(self, etat, pere, mvts, posvide):
        self.etat = etat
        self.h = Noeud.heuristique(etat)
        self.pere = pere
        self.mvts = mvts  # les mvts faits pour passer de etat initial à self
        self.posvide = posvide  # la position du trou

    # 2 Noeuds sont égaux si leurs états sont égaux
    def __eq__(self, o):
        if(type(self) == type(o)):
            return self.etat == o.etat
        else:
            return False

    def g(self):
        """la longueur du plus court chemin de l'etat actuel jusqu'à la racine
        """
        return len(self.mvts)

    def f(self):
        """fonction d'evaluation
        """
        return self.g() + self.h

    def adr(self):
        """retourne l'adr du noeud
        """
        return tuple(self.etat)

#######Deplacements################
# TODO : deplacements

    def mvSouth(self):
        """deplacement du trou vers le Sud
        retourne un nouveau noeud
        """
        etatfils = copy(self.etat)
        nvpos = self.posvide+Noeud.n
        swap(etatfils, self.posvide, nvpos)
        fils = Noeud(etat=etatfils, pere=self, mvts=self.mvts+"S", posvide=nvpos)
        return fils

    def mvNorth(self):
        """deplacement du trou vers le Nord
        retourne un nouveau noeud
        """
        etatfils = copy(self.etat)
        nvpos = self.posvide-Noeud.n
        swap(etatfils, self.posvide, nvpos)
        fils = Noeud(etat=etatfils, pere=self, mvts=self.mvts+"N", posvide=nvpos)
        return fils

    def mvEast(self):
        """deplacement du trou vers l'Est
        retourne un nouveau noeud
        """
        etatfils = copy(self.etat)
        nvpos = self.posvide+1
        swap(etatfils, self.posvide, nvpos)
        fils = Noeud(etat=etatfils, pere=self, mvts=self.mvts+"E", posvide=nvpos)
        return fils

    def mvWest(self):
        """deplacement du trou vers l'ouest
        retourne un nouveau noeud
        """
        etatfils = copy(self.etat)
        nvpos = self.posvide-1
        swap(etatfils, self.posvide, nvpos)
        fils = Noeud(etat=etatfils, pere=self, mvts=self.mvts+"O", posvide=nvpos)
        return fils

########################################

    # TODO: Expansion d'un noeud

    def expand(self):
        """expanse un noeud
        retourne les fils
        """
        x = self.posvide % Noeud.n
        y = self.posvide // Noeud.n

        # match disponible dans python 3.10 mais pas 3.9 :(
        if(x == Noeud.n-1):  # (n-1, y)
            if(y == Noeud.n-1):  # (n-1, n-1)
                # move N, O, E
                # TODO verifier si noeud fils a deja ete explore
                # si oui, alors comparer g()
                # si non ajouter à exploré et frontiere de expansion
                pass
            elif(y == 0):  # (n-1, 0)
                # move O, S
                # TODO verifier si noeud fils a deja ete explore
                # si oui, alors comparer g()
                # si non ajouter à exploré et frontiere de expansion
                pass
            else:  # (n-1, _)
                # move N, S, O
                # TODO verifier si noeud fils a deja ete explore
                # si oui, alors comparer g()
                # si non ajouter à exploré et frontiere de expansion
                pass
        elif (x == 0):  # (0, y)
            if(y == 0):  # (0, 0)
                # move S, E
                # TODO verifier si noeud fils a deja ete explore
                # si oui, alors comparer g()
                # si non ajouter à exploré et frontiere de expansion
                pass
            elif(y == Noeud.n-1):  # (0, n-1)
                # move N, E
                # TODO verifier si noeud fils a deja ete explore
                # si oui, alors comparer g()
                # si non ajouter à exploré et frontiere de expansion
                pass
            else:  # (0, _)
                # move N, S, E
                # TODO verifier si noeud fils a deja ete explore
                # si oui, alors comparer g()
                # si non ajouter à exploré et frontiere de expansion
                pass
        else:  # (_, y)
            if(y == Noeud.n-1):  # (_, n-1)
                # move N, O, E
                # TODO verifier si noeud fils a deja ete explore
                # si oui, alors comparer g()
                # si non ajouter à exploré et frontiere de expansion
                pass
            elif(y == 0):  # (_, 0)
                # move S, O, E
                # TODO verifier si noeud fils a deja ete explore
                # si oui, alors comparer g()
                # si non ajouter à exploré et frontiere de expansion
                pass
            else:  # (_, _)
                # move N,S, E, O
                # TODO verifier si noeud fils a deja ete explore
                # si oui, alors comparer g()
                # si non ajouter à exploré et frontiere de expansion
                pass
            pass


