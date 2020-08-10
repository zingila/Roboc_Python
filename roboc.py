# -*-coding:Utf-8 -*

"""Ce fichier contient le code principal du jeu."""

import os
import re

from labyrinthe import *
from carte import *


# On charge les cartes existantes
try:
    with open("enregistrement", "rb") as fichier:
        enregistrement = pickle.load(fichier)
except FileNotFoundError:
    with open("enregistrement", "wb") as fichier:
        a = pickle.Pickler(fichier)
        a.dump(dict())
    enregistrement = dict()


# On affiche les cartes existantes
cartes = []
partie = []

for fichier in os.listdir("cartes"):
    if fichier.endswith(".txt"):
        chemin = os.path.join("cartes", fichier)
        nom_carte = fichier[:-4]
        nom_carte = nom_carte[0].upper() + nom_carte[1:].lower()




















