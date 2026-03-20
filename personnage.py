from creature import Creature


class Personnage(Creature):
    def __init__(self, nom, description, pv, defense, typeDegats, argent=10):

        super().__init__(nom, description, pv, None, defense, typeDegats)
        self.arme = None
        self.inventaire = []
        self.argent = argent

    def equiper_arme(self, arme):
        self.arme = arme
        print(f"{self.nom} s'équipe de : {self.arme.nom}")

    def ajouter_objet(self, objet):
        self.inventaire.append(objet)
        print(f"{objet} ajouté à l'inventaire.")

    def afficher_inventaire(self):
        print(f"Argent : {self.argent}")
        print(f"Objets : {self.inventaire}")

    def faire_soin(self, montant):
        self.pv += montant
        print(f"{self.nom} se soigne. PV actuels : {self.pv}")

    def lancer_buff(self, bonus):
        self.defense += bonus
        print(f"Buff activé ! Défense : {self.defense}")


# Création des personnages 
guerrier = Personnage("Guerrier", "Un combattant robuste en armure lourde", 35, 14, "Physique")

mage = Personnage("Mage", "Un maitre des sorts anciens", 20, 8, "Magique")

archer = Personnage("Archer", "Un tireur d'elite rapide", 25, 11, "Physique")

paladin = Personnage("Paladin", "Un chevalier sacre protecteur", 45, 16, "Physique")

voleur = Personnage("Voleur", "Un expert en discretion et poison", 22, 10, "Physique")

LISTE_PERSONNAGES = [guerrier, mage, archer, paladin, voleur]