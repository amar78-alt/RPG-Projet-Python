import des


class Arme:
    def __init__(self, nom, nb_des, nb_faces):
        self.nom = nom
        self.nb_des = nb_des
        self.nb_faces = nb_faces

    def get_description(self):
        return f"{self.nom} ({self.nb_des}d{self.nb_faces})"


LISTE_ARMES = [
    Arme("Épée", 1, 6),
    Arme("Dague", 1, 4),
    Arme("Bâton", 2, 4),
    Arme("Arc long", 1, 8),
    Arme("Marteau de guerre", 1, 10)
]