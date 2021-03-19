from Noeud import Noeud
from heuristiques import *
import heapq  # https://docs.python.org/fr/3/library/heapq.html
import time


def heuristique(etat): return fct_heuristique(etat, poids[1], coeff_impair, 3)

n = 3

"""
def recherche(etatinitial)
	frontier expansion <= {etat initial}
	ensmble explore <= {etat inital}
	while true{
		if FE==empty return false
		n <= depiler FT
		if n.etat == etat.final return n
		fils <= n.expansion()
		for f in fils{
			si f a déja été exploré on compare g() ancien et g() nouveau, on remplace si ancien g() > nouveau g()
			sinon on ajoute f à exploré et FE
"""

i = 0
def resolve(etatinitial, posvide):
    global i
    # initialisation
    Noeud.heuristique = heuristique
    Noeud.n = n
    frontiere_expansion = []
    ensemble_explore = {}
    racine = Noeud(etat = etatinitial, pere = None, mvt="", posvide= posvide)
    heapq.heappush(frontiere_expansion, racine)
    while True :
        i = i+1
        if (frontiere_expansion==[]): return False
        noeud = heapq.heappop(frontiere_expansion)
        if ( noeud.etat == sorted(noeud.etat) ) : return noeud
        fils = []
        fils.extend(noeud.expand())
        for f in fils:
            deja_explore = ensemble_explore.get(f.adr())
            if deja_explore == None :
                # si non explore on ajoute à EE et FE
                ensemble_explore[f.adr] = f
                heapq.heappush(frontiere_expansion, f)
            else:
                # si deja explore alors
                #comparaison g() "chemnin"
                if deja_explore.g() > f.g() : 
                    deja_explore.pere = f.pere
                    deja_explore.mvt = f.mvt
                    heapq.heapify(frontiere_expansion)

deb = time.time()
n = resolve([1,3,8,5,7,6,4,2,0], 2)
fin = time.time()
print(" |solution trouvee en {} sec".format(fin-deb))
print("%s iterations" %i)
if(n!=False):
    print(n.mvts()[::-1])
    print(n.g())
else:
    print("pas de solution trouvee")