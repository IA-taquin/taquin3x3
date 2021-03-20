from Noeud import Noeud, swap, copy
from heuristiques import *
import heapq  # https://docs.python.org/fr/3/library/heapq.html
import time


def choix_heuristique(i, n):
    """retourne un fct f(etat) qui correspond a l'heuristique h_i
    """
    poids_i = poids[i]
    if i%2==0 : coeff = coeff_pair
    else: coeff = coeff_impair
    return lambda etat : fct_heuristique(etat, poids_i, coeff, n)


def aSolution(etat, posvide, n):
    """retourne vrai si un taqui a une solution, faux sinon
    """
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



def resolve(etatinitial, posvide, heuristique, n):
    """renvoi un noeud qui correspond a l'etat de but et qui peut donc etre utiliser pour reconstruire la solution
    renvoi (noeud, i, r) où i=nb iterations, r=nb remplacements dans la file priorite    
    """
    i = 0 #nb iterations boucle while
    r = 0 #nb de remplacements
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
        if ( noeud.etat == [0,1,2,3,4,5,6,7,8] ) : return noeud, i, r
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
                if  f.g() < deja_explore.g() :
                    r += 1 
                    deja_explore.pere = f.pere
                    deja_explore.mvt = f.mvt
                    heapq.heapify(frontiere_expansion)

