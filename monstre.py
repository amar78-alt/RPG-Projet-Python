from creature import Creature

class Monstre(Creature):
    def __init__(self, nom, description, pv, attaque, defense, type_degats, resistances):
      
        super().__init__(nom, description, pv, attaque, defense, type_degats)
        self.attaque = attaque
        self.resistances = resistances

    def appliquer_resistance(self, degats, type_degats):
       
        if type_degats in self.resistances:
            print(f"{self.nom} résiste au {type_degats} !")
            degats = degats // 2
        return degats

# Création des monstres

dragon = Monstre(
    nom="Dragon",
    description="Grand dragon cracheur de feu",
    pv=150,
    attaque=20,
    defense=15,
    type_degats="feu",
    resistances=["feu", "poison"]
)

troll = Monstre(
    nom="Troll",
    description="Troll massif et régénérant",
    pv=120,
    attaque=15,
    defense=10,
    type_degats="physique",
    resistances=["feu"]
)

gobelin = Monstre(
    nom="Gobelin",
    description="Petit monstre sournois",
    pv=60,
    attaque=10,
    defense=8,
    type_degats="poison",
    resistances=["poison"]
)

squelette = Monstre(
    nom="Squelette",
    description="Os animé par magie noire",
    pv=50,
    attaque=8,
    defense=12,
    type_degats="physique",
    resistances=["poison"]
)

LISTE_MONSTRES = [dragon, troll, gobelin, squelette]