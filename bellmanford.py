#!/usr/bin/python
# -*- coding: utf-8 -*-

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import pylab


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
    # si on arrive à la fin, on affiche la distance et les peres

   # print('etape -->', etape)
   # print('fin -->', fin)
    if etape == fin:
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
            # on effectue les changements si cela donne un chemin plus court
            if candidat_dist < dist_voisin:
                dist[voisin] = candidat_dist
                pere[voisin] = etape
    # on a regardé tous les voisins : le noeud entier est visité
    visites.append(etape)
    # on cherche le sommet *non visité* le plus proche du départ
    non_visites = dict((s, dist.get(s, float('inf'))) for s in graphe if s not in visites)
    noeud_plus_proche = min(non_visites, key=non_visites.get)
    # on applique récursivement en prenant comme nouvelle étape le sommet le plus proche 
    return plus_court(graphe, noeud_plus_proche, fin, visites, dist, pere, depart)


def dij_rec(graphe, debut, fin):
    return plus_court(graphe, debut, fin, [], {}, {}, debut)


if __name__ == "__main__":
    g4 = {'a': {'d': 5, 'e': 7, 'b': 2},
          'b': {'e': 4, 'c': 9},
          'c': {'e': 4, 'g': 6},
          'd': {'e': 3, 'f': 5},
          'e': {'f': 3, 'g': 4},
          'f': {'h': 5},
          'g': {'h': 3},
          'h': {}
          }
    l4, c4 = dij_rec(g4, 'a', 'h')
    print('Plus court chemin ex4 : ', c4, ' de longueur :', l4)
    arrayKey = []
    for clee in g4:
        arrayKey.append(clee)
    print(arrayKey)
    for clee in g4.values():
        print('clee', clee)  # clee
        print('valeur', clee)  # value
        for cle, valeur in clee.items():
            print('valeur', valeur)
            print('cle', cle)

G = nx.DiGraph()

G.add_edges_from([('A', 'B')], weight=2)
G.add_edges_from([('D', 'E'), ('E', 'F'), ('G', 'H')], weight=3)
G.add_edges_from([('B', 'E'), ('C', 'E'), ('E', 'G')], weight=4)
G.add_edges_from([('A', 'D'), ('D', 'F'), ('F', 'H')], weight=5)
G.add_edges_from([('C', 'G')], weight=6)
G.add_edges_from([('A', 'E')], weight=7)
G.add_edges_from([('C', 'G')], weight=9)

edge_labels = dict([((u, v,), d['weight'])
                    for u, v, d in G.edges(data=True)])
red_edges = [('C', 'D'), ('D', 'A')]
edge_colors = ['black' if not edge in red_edges else 'red' for edge in G.edges()]

pos = nx.spring_layout(G)
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
nx.draw_networkx(G, pos, node_size=2500, edge_color=edge_colors, edge_cmap=plt.cm.Reds)
# pylab.show()
"""
Réponse :
Plus court chemin ex3 :  ['e', 'c', 'f', 's']  de longueur : 10
Plus court chemin ex4 :  ['a', 'b', 'e', 'g', 'h']  de longueur : 13
"""
