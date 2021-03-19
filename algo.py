from Noeud import Noeud, swap, copy
from heuristiques import *
import heapq  # https://docs.python.org/fr/3/library/heapq.html
import time

# changer les heuristiques
n = 3
def heuristique(etat): return fct_heuristique(etat, poids[1], coeff_impair, 3)


def aSolution(etat, posvide):
    global n
    l = copy(etat)
    e_posvide = dist_elmtr(posvide, etat[posvide], n)
    cpt = 0
    permutation = True
    while permutation:
        permutation = False
        for i in range(0, len(l)-1):
            if(l[i]>l[i+1]):
                swap(l, i, i+1)
                cpt +=1
                permutation =True
    return (cpt%2 == e_posvide%2)



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
        if ( noeud.etat == [0,1,2,3,4,5,6,7,8] ) : return noeud
        fils = []
        fils.extend(noeud.expand())
        for f in fils:
            deja_explore = ensemble_explore.get(f.adr())
            if deja_explore == None :
                # si non explore on ajoute à EE et FE
                ensemble_explore[f.adr()] = f
                heapq.heappush(frontiere_expansion, f)
            else:
                # si deja explore alors
                #comparaison g() "chemnin"
                if deja_explore.g() > f.g() : 
                    deja_explore.pere = f.pere
                    deja_explore.mvt = f.mvt
                    heapq.heapify(frontiere_expansion)


deb = time.time()
n = resolve([8,6,7,2,5,4,3,0,1], 0)
fin = time.time()
print(" |solution trouvee en {} sec".format(fin-deb))
print("%s iterations" %i)
if(n!=False):
    print(n.mvts()[::-1])
    print(n.g())
else:
    print("pas de solution trouvee")
