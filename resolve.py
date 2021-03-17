from heuristiques import *

heuristique = lambda etat : fct_heuristique(etat, poids[1], coeff_impair, 3)

print(heuristique((1, 3, 8, 5, 7, 6, 4, 2, 0)))