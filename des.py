import random

def lancer_des(nb_des, nb_faces):
    total = 0
    for i in range(nb_des):
        resultat = random.randint(1, nb_faces)
        total += resultat
    return total


def lancer_d4(nb_des=1):
    return lancer_des(nb_des, 4)




def lancer_d6(nb_des=1):
    return lancer_des(nb_des, 6)


def lancer_d8(nb_des=1):
    return lancer_des(nb_des, 8)


def lancer_d10(nb_des=1):
    return lancer_des(nb_des, 10)


def lancer_d12(nb_des=1):
    return lancer_des(nb_des, 12)


def lancer_d20(nb_des=1):
    return lancer_des(nb_des, 20)



def formater_des(nb_des, nb_faces):
    return f"{nb_des}d{nb_faces}"
 
 
