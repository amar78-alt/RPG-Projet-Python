from des import lancer_d20, lancer_des, lancer_d8, lancer_d6

class Action:
    def __init__(self, nom, lanceur, cible):
        self.nom = nom
        self.lanceur = lanceur
        self.cible = cible

    def executer(self):
        pass

class Attaque(Action):
    def __init__(self, lanceur, cible):
        super().__init__("Attaque", lanceur, cible)

    def executer(self):
        jet_attaque = lancer_d20()
        print(f"[{self.lanceur.nom}] tente une attaque... Jet : {jet_attaque}")

        if jet_attaque == 1:
            print("Échec critique !")
            self.lanceur.subir_degats(5)
            return

        if hasattr(self.lanceur, "arme") and self.lanceur.arme is not None:
            arme = self.lanceur.arme
            degats_base = lancer_des(arme.nb_des, arme.nb_faces)
            type_degats = getattr(self.lanceur, "typeDegats", "physique")
        else:
            degats_base = getattr(self.lanceur, "attaque", 5)
            type_degats = getattr(self.lanceur, "typeDegats", "physique")

        if jet_attaque == 20:
            print("Réussite critique ! Dégâts doubles.")
            self.cible.subir_degats(degats_base * 2)
        elif jet_attaque >= self.cible.defense:
            print("L'attaque touche la cible.")
            self.cible.subir_degats(degats_base)
        else:
            print("L'attaque échoue.")

class Soin(Action):
    def __init__(self, lanceur, cible):
        super().__init__("Soin", lanceur, cible)

    def executer(self):
        valeur_soin = lancer_d8(2)
        self.cible.pv += valeur_soin
        if self.cible.pv > self.cible.pv_max:
            self.cible.pv = self.cible.pv_max
        print(f"{self.lanceur.nom} soigne {self.cible.nom} de {valeur_soin} PV.")

class Buff(Action):
    def __init__(self, lanceur, cible):
        super().__init__("Bouclier Magique", lanceur, cible)

    def executer(self):
        self.cible.defense += 2
        print(f"{self.lanceur.nom} augmente la défense de {self.cible.nom} de 2 points.")

class Poison(Action):
    def __init__(self, lanceur, cible):
        super().__init__("Jet de Poison", lanceur, cible)

    def executer(self):
        self.cible.ajouter_etat("empoisonne")
        print(f"{self.lanceur.nom} empoisonne {self.cible.nom} !")

def appliquer_etats_debut_tour(creature):
    peut_jouer = True

    if not creature.est_vivante():
        return False

    if "empoisonne" in creature.etats:
        print(f"Le poison blesse {creature.nom} !")
        creature.subir_degats(3)

    if "paralyse" in creature.etats:
        print(f"{creature.nom} est paralysé et ne peut pas bouger.")
        peut_jouer = False

    return peut_jouer