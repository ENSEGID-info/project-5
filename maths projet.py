# -*- coding: utf-8 -*-
"""
Created on Wed Nov 12 15:25:14 2025

@author: ctouge
"""


import numpy as np
import matplotlib.pyplot as plt
import csv
#import pandas as pd

## FONCTIONS


    
    
def cerveau_de_l_operation ():
    g = input('glacier:')
    a= input ('année:')
    # Récupération des données voulues
    lectureMesures('test.csv')
    print(recuperation_ligne (g))
    print(valeur_glacier_annee_x (g,a))
    evolution_totale_glacier (g)




## Lecture des données d'un fichier au format csv
def lectureMesures(nomFich):
    
# Lecture d'un fichier
    f = open (nomFich)
    
# Format csv
    fcsv = csv.reader(f, delimiter=';')
    
# Récupération des entêtes
    for E in fcsv:
        break
    
# Suppression du 1er elt = 'Observations'
    E = E[1:]
    
# Récupération de la matrice des données quantitatives
    LL = []
    I = []
    for ligne in fcsv:
# Changement du séparateur décimal (virgule en point)
        n = len(ligne)
        for i in range(n):
            ligne[i] = ligne[i].replace(',','.')
        I.append(ligne[0])
        LL.append(ligne[1:])
    M = np.array(LL, dtype=float)
    
# Fermeture du fichier
    f.close()
        
    return M, I, E






# Récupération de la ligne corespondant au glacier

fichier = 'test.csv'

def recuperation_ligne (g):
    ligne_cible = g

    # On crée des variables, liste et tableau
    tableau_ligne_a2 = []
    tableau_ligne_a2_complet=[]

    #On parcourt les lignes et on garde seulement la ligne_cible
    with open(fichier, newline='') as csvfile:
        lecteur = csv.reader(csvfile)  # lecture en mode tableau (liste de listes)
    
        # Récupérer les en-têtes
        entetes = next(lecteur)
    
        # Parcourir chaque ligne
        for row in lecteur:
            if row[0] == ligne_cible:  # On suppose que la première colonne contient le nom
                tableau_ligne_a2.append(row)

    # Ajouter les en-têtes si tu veux garder le tableau complet
    tableau_ligne_a2_complet = [entetes] + tableau_ligne_a2

    # Affichage
    return(tableau_ligne_a2_complet)





# On récupère la valeur correspondant à l'année

def valeur_glacier_annee_x (glacier,annee):
    # annee est un str
    tableau = recuperation_ligne (glacier)
    num_colone = tableau[0].index(annee)
    print (num_colone)
    return(tableau[1][num_colone])


def evolution_totale_glacier (glacier):
    #glacier est un str
    tableau_de_travail = recuperation_ligne (glacier)
    X= tableau_de_travail[0][1:]
    Y= tableau_de_travail[1][1:]
    print(X,Y)
    plt.plot(X,Y)
    plt.show()
    


    
    
    