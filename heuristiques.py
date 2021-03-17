# dictionnaire ième heuristique : [poids élément i]
poids = {1: [36, 12, 12, 4, 1, 1, 4, 1, 0],
         2: [8, 7, 6, 5, 4, 3, 2, 1, 0],
         3: [8, 7, 6, 5, 4, 3, 2, 1, 0],
         4: [8, 7, 6, 5, 3, 2, 4, 1, 0],
         5: [8, 7, 6, 5, 3, 2, 4, 1, 0],
         6: [1, 1, 1, 1, 1, 1, 1, 1, 0]
         }

# coefficients de normalisation p1=p3=p5=4, p2=p4=p6=1
coeff_impair = 4
coeff_pair = 1


def heuristique(etat, poids, coeff, n):
    """calcule l'heuristique

    parametres
    ---
    etat : etat actuel du taquin
    poids : le poids a etre utilisé, ie: poids[5] pour h5
    coeff : coeff de normalisation
    n : nb lignes taquin
    """
    # somme
    som = 0
    for i, v_i in enumerate(etat):
        # i = pos actuel, v_i pos fianl
        terme = poids[v_i]*dist_elmtr(i, v_i, n)
        som = som + terme
    # reduction somme <=> div coeff
    res = som // coeff
    return res


def dist_elmtr(i, v_i, n):
    """calcule la distance elementaire = nb de déplacements pour arriver à l'etat final

    parametres
    ---
    i : la position de l'element
    v_i : la valeur de l'element <=> sa pos final
    n : nb de lignes(=colonnes) du taquin(N*N)
    """
    # deplacements= abs(pos actuel - pos final)
    x = abs(i % n - v_i % n)
    y = abs(i//n - v_i//n)
    return x+y
