from des import lancer_d20
from des import lancer_d8

class Action:
    def __init__(self, nom, lanceur, cible):
        self.nom = nom
        self.lanceur = lanceur
        self.cible = cible

    def executer(self):
        pass

class Attaque(Action):
    def __init__(self, lanceur, cible):
        super().__init__("Attaque basique", lanceur, cible)

    def executer(self):
        jet_attaque = des.lancer_d20()
        print(f"[{self.lanceur.nom}] def na jet d'attaque bu: {jet_attaque}")

        if jet_attaque == 1:
            print("Échec critique ! (Ndoggal la !)")
            degats_rate = 5
            self.lanceur.pv -= degats_rate
            print(f"{self.lanceur.nom} am na gañ-gañ ci bopam ! Mu ñakk {degats_rate} PV.")

        elif jet_attaque == 20:
            print("Réussite critique ! (Fóot na ko !)")
            degats_critique = 10 * 2
            self.cible.pv -= degats_critique
            print(f"{self.cible.nom} ñakk na {degats_critique} PV !")

        elif jet_attaque > self.cible.defense:
            print("Attaque réussie ! (Door na ko mu àgg !)")
            degats = 10
            self.cible.pv -= degats
            print(f"{self.cible.nom} ñakk na {degats} PV !")

        else:
            print("Attaque ratée... (Laalu ko !)")

class Soin(Action):
    def __init__(self, lanceur, cible):
        super().__init__("Soin", lanceur, cible)

    def executer(self):
        soin_valeur = des.lancer_d8(2)
        self.cible.pv += soin_valeur
        print(f"{self.lanceur.nom} faj na {self.cible.nom} ! Mu yokk {soin_valeur} PV.")
        print(f"-> {self.cible.nom} am na léegi {self.cible.pv} PV.")

class Buff(Action):
    def __init__(self, lanceur, cible):
        super().__init__("Bouclier Magique (Buff)", lanceur, cible)

    def executer(self):
        bonus_defense = 2
        self.cible.defense += bonus_defense
        print(f"{self.lanceur.nom} jox na {self.cible.nom} dolé ! Karàngem (Défense) yokku na +{bonus_defense}.")
        print(f"-> {self.cible.nom} am na léegi {self.cible.defense} CA.")

class Poison(Action):
    def __init__(self, lanceur, cible):
        super().__init__("Jet de Poison", lanceur, cible)

    def executer(self):
        if "empoisonné" not in self.cible.etats:
            self.cible.etats.append("empoisonné")
            print(f"{self.cible.nom} dafa am poison léegi ! (Il est empoisonné).")
        else:
            print(f"{self.cible.nom} am na poison ba pare ! (Il est déjà empoisonné).")

def appliquer_etats(creature):
    peut_jouer = True

    if "empoisonné" in creature.etats:
        degats_poison = 3
        creature.pv -= degats_poison
        print(f"{creature.nom} dafa am poison ! Mu ñakk {degats_poison} PV ci début tour bi. (Reste: {creature.pv} PV)")

    if "paralysé" in creature.etats:
        print(f"{creature.nom} dafa paralysé ! Mënul def dara ci tour bi (Il passe son tour).")
        peut_jouer = False

    return peut_jouer