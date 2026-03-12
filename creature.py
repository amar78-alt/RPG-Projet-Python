from des import lancer_d20

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

# Lance un jet d'initiative (1d20) pour déterminer l'ordre de jeu.
    def lancer_initiative(self):
        self.initiative = lancer_d20()
        print(f"{self.nom} lance l'initiative: {self.initiative}")
        return self.initiative 
    
#Affiche toutes les caractéristiques de la créature.   
def afficher_caracteristiques(self):
        print("|---| " + self.nom + " |---|")
        print("  Description: " + self.description)
        print("  PV: " + str(self.pv) + " / " + str(self.pv_max))
        print("  Défense: " + str(self.defense))
        print("  Type de degats: " + str(self.type_degats))







