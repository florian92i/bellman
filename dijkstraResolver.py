from random import randrange
import sys

sys.setrecursionlimit(5000)

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import pylab

# alphabet = { 1 : 'a', 2 : 'b', 3 : 'c', 4 : 'd', 5 : 'e', 6 : 'f', 7 : 'g', 8 : 'h', 9 : 'i', 10 : 'j', 11 : 'k', 12 : 'l', 13 : 'm', 14 : 'n', 15 : 'o', 16 : 'p', 17 : 'q', 18 : 'r', 19 : 's', 20 : 't', 21 : 'u', 22 : 'v', 23 : 'W', 24 : 'x', 25 : 'y', 26 : 'z' }
# diagrammeFinal = {}
# nombrePoints = randrange(2, 26)
# # print("nombre de points : ", nombrePoints)
# pointActuel = 1
# while pointActuel != nombrePoints + 1:
#     nombreCorrespondances = randrange(1, nombrePoints)
#     correspondanceActuel = 1
#     diagrammeFinal[alphabet[pointActuel]] = {}
#     while correspondanceActuel != nombreCorrespondances:
#         # if alphabet[pointActuel] != alphabet[correspondanceActuel] and not diagrammeFinal[alphabet[pointActuel]].has_key(alphabet[correspondanceActuel]):
#         if alphabet[pointActuel] != alphabet[correspondanceActuel]:
#             distance = randrange(1, 10)
#             diagrammeFinal[alphabet[pointActuel]].update({ alphabet[correspondanceActuel] : distance })
#         correspondanceActuel = correspondanceActuel + 1
#     pointActuel = pointActuel + 1
# print(diagrammeFinal)


# ---------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------


def affiche_peres(pere, depart, extremite, trajet):
    """
    À partir du dictionnaire des pères de chaque sommet on renvoie
    la liste des sommets du plus court chemin trouvé. Calcul récursif.
    On part de la fin et on remonte vers le départ du chemin.

    """
    if extremite == depart:
        return [depart] + trajet
    else:
        return (affiche_peres(pere, depart, pere[extremite], [extremite] + trajet))


def plus_court(graphe, etape, fin, visites, dist, pere, depart):
    """
    Trouve récursivement la plus courte chaine entre debut et fin avec l'algo de Dijkstra
    visites est une liste et dist et pere des dictionnaires
    graphe  : le graphe étudié                                                               (dictionnaire)
    étape   : le sommet en cours d'étude                                                     (sommet)
    fin     : but du trajet                                                                  (sommet)
    visites : liste des sommets déjà visités                                                 (liste de sommets)
    dist    : dictionnaire meilleure distance actuelle entre départ et les sommets du graphe (dict sommet : int)
    pere    : dictionnaire des pères actuels des sommets correspondant aux meilleurs chemins (dict sommet : sommet)
    depart  : sommet global de départ                                                        (sommet)
    Retourne le couple (longueur mini (int), trajet correspondant (liste sommets))

    """

    if etape == fin:
        fin = len(pere)
        print(affiche_peres(pere, depart, fin, []))

        return dist[fin], affiche_peres(pere, depart, fin, [])
    # si c'est la première visite, c'est que l'étape actuelle est le départ : on met dist[etape] à 0
    if len(visites) == 0: dist[etape] = 0
    # on commence à tester les voisins non visités
    for voisin in graphe[etape]:
        if voisin not in visites:
            # la distance est soit la distance calculée précédemment soit l'infini
            dist_voisin = dist.get(voisin, float('inf'))
            # on calcule la nouvelle distance calculée en passant par l'étape
            candidat_dist = dist[etape] + graphe[etape][voisin]
            
            if candidat_dist < dist_voisin:
                dist[voisin] = candidat_dist
                pere[voisin] = etape

    # on a regardé tous les voisins : le noeud entier est visité
    visites.append(etape)
    # on cherche le sommet *non visité* le plus proche du départ
    non_visites = dict((s, dist.get(s, float('inf'))) for s in graphe if s not in visites)
    if non_visites:
        # print(non_visites)
        noeud_plus_proche = min(non_visites, key=non_visites.get)
        # on applique récursivement en prenant comme nouvelle étape le sommet le plus proche
        return plus_court(graphe, noeud_plus_proche, fin, visites, dist, pere, depart)


def dij_rec(graphe, debut, fin):
    return plus_court(graphe, debut, fin, [], {}, {}, debut)


def createRandomDijkstraDict( nombrePoints, nombreArc):

    diagrammeFinal = {}

    pointActuel = 1
    
    while pointActuel != int(nombrePoints) + 1:
    
        nombreCorrespondances = nombreArc
        correspondanceActuel = 1
        diagrammeFinal[pointActuel] = {}

        while correspondanceActuel < nombreCorrespondances:

            distance = randrange(1, 200)
            
            correspondanceValeur = randrange(1, int(nombrePoints))

            if correspondanceValeur not in diagrammeFinal[pointActuel]:
            
                diagrammeFinal[pointActuel].update({ correspondanceValeur : distance })
                correspondanceActuel = correspondanceActuel + 1

        pointActuel = pointActuel + 1

    return diagrammeFinal

    
nombreParametre = sys.argv[1]
nombreArc = sys.argv[2]

if nombreParametre not in ['0','1','2']:

    lenghtParam = int(nombreParametre)
    lenghtArc = int(nombreArc)
    g4 = createRandomDijkstraDict(lenghtParam, lenghtArc)

else:

    print("Il faut au moins 3 points")
    sys.exit()


if __name__ == "__main__":

    # print("")
    # print("#################### Diagramme #################### ")
    # print("")

    # print(g4)

    # print("")
    # print("#################### Tri #################### ")
    # print("")

    l4, c4 = dij_rec(g4, 1, lenghtParam)
    print('Plus court chemin : ', c4, ' de longueur :', l4)