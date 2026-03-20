from des import lancer_d20


class Creature:

    def __init__(self, nom, description, pv, defense, typeDegats, attaque=None):
        self.nom = nom
        self.description = description
        self.pv = pv
        self.pv_max = pv
        self.defense = defense
        self.typeDegats = typeDegats
        self.attaque = attaque
        self.typeDegats = typeDegats
        self.initiative = 0
        self.liste_actions = []
        self.etats = []
        self.est_ko = False


# Lance un jet d'initiative (1d20)
    def lancer_initiative(self):
        self.initiative = lancer_d20()
        print(self.nom + " lance l'initiative: " + str(self.initiative))
        return self.initiative


# Affiche les caractéristiques de la créature
        print("|---| " + self.nom + " |---|")
        print("Description: " + self.description)
        print("PV: " + str(self.pv) + " / " + str(self.pv_max))
        print("Défense: " + str(self.defense))
        print("Type de degats: " + self.typeDegats)

        if len(self.etats) == 0:
            print("Etats: Aucun")
        else:
            print("Etats:", self.etats)


# Affiche les actions disponibles
    def afficher_actions(self):
        if len(self.liste_actions) == 0:
            print("Aucune action disponible")
        else:
            print("Actions disponibles :")
            for i, action in enumerate(self.liste_actions, 1):
                print(str(i) + ". " + action)


# Faire subir des dégâts
    def subir_degats(self, degats):
        self.pv = self.pv - degats
        print(self.nom + " subit " + str(degats) + " degats")

        if self.pv <= 0:
            self.pv = 0
            self.est_ko = True
            print(self.nom + " est KO !")


# Vérifier si la créature est vivante
    def est_vivante(self):
     return self.pv > 0

# Ajouter un état 
    def ajouter_etat(self, etat):
        if etat not in self.etats:
            self.etats.append(etat)
            print(self.nom + " est maintenant " + etat)


# Retirer un état
    def retirer_etat(self, etat):
     if etat in self.etats:
        self.etats.remove(etat)
        print(self.nom + " n'est plus " + etat)

# Vérifie si la créature peut être attaquée
    def attaquable(self):
        if self.est_ko:
            return False
        if "paralysé" in self.etats:
            return False
        return True