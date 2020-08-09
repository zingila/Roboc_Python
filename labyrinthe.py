"""
Ce fichier contient la class robot qui gère les sauvegardes
et coordonnées du robot.
"""

import pickle

class Robot():
    
    """Creation d'une instance robot et sa position."""
    
    def __init__(self, coord):
        
        self.coord = coord
        
    def def_position(self, mouvement):

        """
        Methode retourne l'action effectué par le robot sous
        forme d'une lettre puis un ou des chiffres (facultatif).
        """

        x, y = self.coord[0], self.coord[1]

        chemin, vitesse = mouvement[0], mouvement[1:]

        vitesse = 1 if vitesse == "" else int(vitesse)

        if chemin == "o":
            x = x - vitesse
        elif chemin == "e":
            x = x + vitesse
        elif chemin == "n":
            y = y - vitesse
        elif chemin == "s":
            y = y + vitesse
        else:
            pass

        return x, y

        

    def position(self, coord, coord_trouver, nom_carte):

        """
        Methode qui enregistre les dernières informations
        de la carte et la position du robot dans un fichier.
        """

        position = dict()
        x, y = coord

        with open("enregistrement", "rb") as fichier:
            position = pickle.load(fichier)

        if coord == coord_trouver:
            del position[nom_carte]
        else:
            position[nom_carte] = coord

        with open("enregistrement", "wb") as fichier:
            a = pickle.Pickler(fichier)
            a.dump(position)
