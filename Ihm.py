from resolve import *

print("RESOLUTION TAQUIN N*N")
n = int(input("N? "))
i = int(input("Heuristique? "))
etatinitial = []
for case in range(0, n*n):
    val = int(input("Valeur case%s? " % case))
    etatinitial.append(val)
posvide = int(input("Trou à la case? "))
print("Verification taquin soluble...")
if aSolution(etatinitial, posvide, n):
    print("  Ce taquin admet des solutions")
    deb = time.time()
    noeud, it, r = resolve(etatinitial,
                           posvide, choix_heuristique(i, n), n)
    fin = time.time()
    print("Solution trouvee en {} sec".format(fin-deb))
    print("  %s iterations, %s remplacements" % (it, r))
    print("chemin: %s" %noeud.mvts()[::-1])
    nbmvts = noeud.g()
    print("%s mouvements" %nbmvts)
    noeud_chemin = noeud
    for i in range(0, nbmvts):
        print("=======================")
        print("Mouvement%s: %s" % (nbmvts-i, noeud_chemin.mvt))
        print(" %s \n %s \n %s" % (
            noeud_chemin.etat[:3], noeud_chemin.etat[3:6], noeud_chemin.etat[6:9]))
        print("=======================")
        noeud_chemin = noeud_chemin.pere
    print(" %s \n %s \n %s" % (
            etatinitial[:3], etatinitial[3:6], etatinitial[6:9]))
else:
    print("ce taquin n'a pas de solution")
