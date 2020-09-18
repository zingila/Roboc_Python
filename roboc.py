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
        with open(chemin, "r") as fichier:
            contenu = fichier.read()
            carte = Carte(nom_carte, contenu)
            cartes.append(carte)
            for key, value in enregistrement.items():
                if carte.nom == key:
                    carte.robot = value
                    partie.append(carte)

print("partie en cours : ", enregistrement)
print("Labyrinthes existants :")
for i, carte in enumerate(cartes):
    print("  {} - {}".format(i + 1, carte.nom ))



# On selectionne une carte parmis la liste
def choix(les_cartes):

    while 1:
        try:
            choix = int(input("\nEntrez un numéro de labyrinthe pour commencer à jouer : "))
            assert choix in range(1, len(les_cartes)+1)
        except ValueError:
            print("Erreur ! Saisir un nombre uniquement")
            continue
        except AssertionError:
            print("Erreur ! Le numero de carte n'existe pas")
            continue
        else:
            index = choix-1
            choix_cartes = les_cartes[index]
            break

    return choix_cartes

# 
if len(partie) > 0:

    # Stockage du choix de l'utilisateur dans 'reprendre'
    while 1:
        try:
            continuer = int(input("\nUne ou des parties en cours, que souhaitez-vous ?\n\n  1 - Continuer une partie\n  2 - Démarrer une nouvelle partie\nChoix : "))
            assert continuer in range(1, 3)
        except ValueError:
            print("Erreur ! Saisissez un nombre")
            continue
        except AssertionError:
            print("Choisissez 1 ou 2...")
        else:
            continuer = True if continuer == 1 else False
            break

# Sinon, reprendre = False (aucune partie en cours)
else:
    continuer = False

if continuer:
    # Affichage des parties en cours
    print("\nParties en cours :\n")
    for i, part in enumerate(partie):
        print("  {0} - {1}".format(i + 1, part.nom))
    carte_choisie = choix(partie)
else:
    # Affichage des cartes existantes
    print("\nCartes existantes :\n")
    for i, carte in enumerate(cartes):
        print("  {0} - {1}".format(i + 1, carte.nom))
    carte_choisie = choix(cartes)



print("Parties en cours : {0}".format(enregistrement, "\n"))

#On affiche le début de la partie
print("{0}DEBUT DE LA PARTIE{0}(carte : {1})".format("\n", carte_choisie.nom))

#On crée l'instanciation d'un robot
robot = Robot(carte_choisie.robot)

#On affiche la carte
print("\n{0}\n".format(carte_choisie.chaine))


# Entrées actions utilisateur
while 1:

    action = input("Action : ").lower()
    pattern = "^q|([neso][1-9]*)$"

    if not re.fullmatch(pattern, action):
        print("Saisie erronée...")
        continue
