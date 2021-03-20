from resolve import *
from random import randint

# [temps, nb_iterations, remplacements ]
stats = {
    1: {"temps": 0, "iterations": 0, "remplacements": 0},
    2: {"temps": 0, "iterations": 0, "remplacements": 0},
    3: {"temps": 0, "iterations": 0, "remplacements": 0},
    4: {"temps": 0, "iterations": 0, "remplacements": 0},
    5: {"temps": 0, "iterations": 0, "remplacements": 0},
    6: {"temps": 0, "iterations": 0, "remplacements": 0}
}

n = 3

print("====================DEBUT_TEST=====================")
print("===================================================")
for k in range(1, 101):
    valeurs = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    etat = []
    posvide = 0
    # on cherche un etat qui a une solution
    while True:
        for v in range(0, 9):
            intaleatoire = randint(0, len(valeurs)-1)
            etat.append(valeurs.pop(intaleatoire))
        posvide = randint(0, 8)
        if(aSolution(etat, posvide, n)):
            break
        else:
            valeurs = [0, 1, 2, 3, 4, 5, 6, 7, 8]
            etat = []
    print(etat)
    for i in range(1, 7):
        print("k: %s, i: %s" % (k, i))
        deb = time.time()
        noeud, it, r = resolve(etat,
                               posvide, choix_heuristique(i, n), n)
        fin = time.time()
        temps = fin-deb
        moyenne_temps = (stats[i]["temps"]*(k-1)+temps) / k
        moyenne_iterations = (stats[i]["iterations"]*(k-1)+it) / k
        moyenne_remplacements = (stats[i]["remplacements"]*(k-1)+r) / k
        stats[i]["temps"] = moyenne_temps
        stats[i]["iterations"] = moyenne_iterations
        stats[i]["remplacements"] = moyenne_remplacements

for res in range(1, 7):
    print("===================================================")
    print("temps h%s : %s" % (res, stats[res]["temps"]))
    print("iterations h%s : %s" % (res, stats[res]["iterations"]))
    print("remplacements h%s : %s" % (res, stats[res]["remplacements"]))

print("=======================FIN=========================")
print("===================================================")
