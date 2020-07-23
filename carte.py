
"""
Création de la classe Carte,
liaison entre les objets et le fichier du dossier \cartes
"""

class Carte():

    """Transformation du fichier sous forme d'objet carte"""
    
    def __init__(self, nom, chaine):

        self.nom = nom
        self.chaine = chaine
        self.pas = chaine.replace("X", " ")
        self.robot = chaineCarte(chaine)[0]
        self.sortie = chaineCarte(chaine)[1]
        self.obstacles = chaineCarte(chaine)[2]
        self.hauteur = len(chaine.split("\n"))
        self.largeur = len(chaine.split("\n")[0])


    def grille(self, coord):

        """Renvoie la position du robot dans la carte."""

        x, y = coord
        sortie = False

        grille = self.pas.split("\n")
        destination = grille[y][x]
        grille[y] = (grille[y])
        grille[y][x] = "X"
        grille[y] = "".join(grille[y])
        grille = "\n".join(grille)

        return grille
