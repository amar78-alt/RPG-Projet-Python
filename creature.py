class Creature:
    def __init__(self, nom, description, pv, defense, typeDegats):
        self.nom = nom                   
        self.description = description   
        self.pv = pv                     
        self.defense = defense           
        self.typeDegats = typeDegats     
        self.initiative = 0              
        self.liste_actions = []          
        self.etats = []                  
