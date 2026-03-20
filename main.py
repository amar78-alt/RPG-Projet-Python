from personnage import Personnage, LISTE_PERSONNAGES
from monstre import Monstre, LISTE_MONSTRES
from arme import LISTE_ARMES
from action import Attaque, Soin, Buff, Poison, appliquer_etats_debut_tour


def afficher_separateur():
    print("=" * 50)


def demander_nombre(message, min_val, max_val):
    while True:
        try:
            valeur = int(input(message))
            if min_val <= valeur <= max_val:
                return valeur
            print("Erreur.")
        except:
            print("Erreur.")
def creer_equipe_joueurs():
    afficher_separateur()
    print("=== EQUIPE HEROS ===")

    equipe = []
    nb = demander_nombre("Combien de heros desirez-vous ? (1-3): ", 1, 3)

    for i in range(nb):
        print("\nVeuillez choisir vos  personnages :")
        
       
        for idx, p in enumerate(LISTE_PERSONNAGES):
            print(f"\n{idx+1}. {p.nom}")
            p.afficher_caracteristiques()

        choix = demander_nombre("Choix: ", 1, len(LISTE_PERSONNAGES)) - 1
        base = LISTE_PERSONNAGES[choix]

        perso = Personnage(
            base.nom,
            base.description,
            base.pv,
            base.defense,
            base.typeDegats
        )

        print("\nChoix arme :")
        for idx, a in enumerate(LISTE_ARMES):
            print(f"{idx+1}. {a.nom}")

        choix_arme = demander_nombre("Choix: ", 1, len(LISTE_ARMES)) - 1
        perso.equiper_arme(LISTE_ARMES[choix_arme])

        equipe.append(perso)

    return equipe

# =========================
# CREATION EQUIPE MONSTRES
# =========================
def creer_equipe_monstres():
    afficher_separateur()
    print("=== MONSTRES ===")

    equipe_monstres = []
    nb = demander_nombre("Combien de  de monstres desirez-vous (1-4): ", 1, 4)

    for i in range(nb):
        # Affiche la liste des monstres disponibles
        for idx, m in enumerate(LISTE_MONSTRES):
            print(f"{idx+1}. {m.nom}")

        choix = demander_nombre("Choix: ", 1, len(LISTE_MONSTRES)) - 1
        base = LISTE_MONSTRES[choix]

        # Création du monstre avec tous les arguments dans le bon ordre
        monstre = Monstre(
            base.nom,
            base.description,
            base.pv,
            base.attaque,        # ATTENTION : attaque avant defense
            base.defense,
            base.typeDegats,
            base.resistances.copy()
        )

        equipe_monstres.append(monstre)

    #  Affichage des caractéristiques de tous les monstres choisis
    afficher_separateur()
    print("=== CARACTÉRISTIQUES DES MONSTRES ===")
    for monstre in equipe_monstres:
        monstre.afficher_caracteristiques()

    return equipe_monstres

# =========================
# INITIATIVE
# =========================
def lancer_initiatives(joueurs, monstres):
    tous = joueurs + monstres

    for c in tous:
        c.lancer_initiative()

    tous.sort(key=lambda x: x.initiative, reverse=True)
    return tous


# =========================
# CHOIX ACTION
# =========================
def choisir_action(participant, ennemis, allies):

    print(f"\nTour de {participant.nom}")

    if isinstance(participant, Personnage):
        print("1. Attaque")
        print("2. Soin")
        print("3. Buff")

        choix = demander_nombre("Choix: ", 1, 3)

        if choix == 1:
            return "attaque", choisir_cible(ennemis)
        elif choix == 2:
            return "soin", choisir_cible(allies)
        else:
            return "buff", choisir_cible(allies)

    else:
        print("1. Attaque")
        print("2. Poison")

        choix = demander_nombre("Choix: ", 1, 2)

        if choix == 1:
            return "attaque", choisir_cible(ennemis)
        else:
            return "poison", choisir_cible(ennemis)


def choisir_cible(liste):
    vivants = [c for c in liste if c.est_vivante()]

    for i, c in enumerate(vivants):
        print(f"{i+1}. {c.nom} ({c.pv} PV)")

    choix = demander_nombre("Cible: ", 1, len(vivants)) - 1
    return vivants[choix]


# =========================
# EXECUTION ACTION
# =========================
def executer_action(participant, action_type, cible):

    if action_type == "attaque":
        Attaque(participant, cible).executer()

    elif action_type == "soin":
        Soin(participant, cible).executer()

    elif action_type == "buff":
        Buff(participant, cible).executer()

    elif action_type == "poison":
        Poison(participant, cible).executer()
#=========FONCTIONNALITE SUPPLEMENTAIRE=====================

def evenement_mort_subite(joueurs):
    import random
    if random.randint(1, 10) == 1:
        cible = random.choice([j for j in joueurs if j.est_vivante()])
        print("\n💀 Un KDO empoisonné tombe sur", cible.nom, "!")
        cible.subir_degats(50)


# =========================
# COMBAT
# =========================
def jouer_combat():
    joueurs = creer_equipe_joueurs()
    monstres = creer_equipe_monstres()

    ordre = lancer_initiatives(joueurs, monstres)

    tour = 1

    while True:
        print(f"\n TOUR {tour} ")
        
        evenement_mort_subite(joueurs)

        for perso in ordre:

            if not appliquer_etats_debut_tour(perso):
                continue

            if not perso.est_vivante():
                continue

            if isinstance(perso, Personnage):
                ennemis = monstres
                allies = joueurs
            else:
                ennemis = joueurs
                allies = monstres

            action, cible = choisir_action(perso, ennemis, allies)

            if cible:
                executer_action(perso, action, cible)

            # victoire
            if all(not m.est_vivante() for m in monstres):
                print("Victoire !!!!")
                return

            if all(not j.est_vivante() for j in joueurs):
                print("Défaite...")
                return

        tour += 1
        input("Entrée pour continuer...")


if __name__ == "__main__": jouer_combat()