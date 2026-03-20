Projet : Simulateur de combat RPG

Groupe :

NDAW Ndeye Sokhna

AMINOU Imane

LEYE Baye Cheikh

MBENGUE Mouhamadou Lamine

AMAR Alle

Description :
Ce projet est un programme Python qui permet de simuler des combats au tour par tour comme dans Donjons et Dragons. Le but est d'aider un Maître du Jeu (MJ) à gérer les lancers de dés et les points de vie des joueurs et des monstres automatiquement.

Comment le jeu fonctionne :

Mise en place : Au début, le programme demande le nombre de héros. Pour chaque héros, on lui donne un nom et on lui choisit une arme dans notre liste (Épée, Arc, Marteau, etc.). Ensuite, on choisit les monstres.

L'Initiative : Le programme lance un dé 20 pour chaque personnage. Celui qui fait le plus gros score commence à jouer.

Le Combat : À chaque tour, on choisit une action :

Attaque : On lance un dé 20. Si c'est plus haut que la défense de la cible, on touche et on lance les dés de dégâts de l'arme.

Soin : Pour redonner des PV à un allié.

Buff : Pour augmenter la défense d'un personnage.

Fin de partie : Le jeu s'arrête quand une équipe n'a plus de PV.

Points techniques (POO) :

On a utilisé une classe parente Creature pour les bases (nom, PV, défense).

Les classes Personnage et Monstre héritent de Creature mais ont des spécificités (l'inventaire pour le personnage, les résistances pour le monstre).

Les armes sont des objets à part avec leurs propres dés de dégâts (ex: 1d10 pour le marteau).

Nos ajouts personnels :
On a ajouté un système d'argent et un inventaire pour les personnages. Chaque héros commence avec 10 pièces d'or. On a aussi créé plusieurs types d'armes avec des lancers de dés différents pour équilibrer le jeu (certaines font des petits dégâts garantis, d'autres des gros dégâts risqués).
Fonctionnalité supplémentaire – Mort Subite

Pendant le combat, un événement aléatoire peut se produire à chaque tour :

Un KDO empoisonné tombe sur un héros au hasard parmi ceux qui sont encore vivants.

Le héros touché subit de lourds dégâts (50 PV) instantanément.

Cet événement peut provoquer la mort soudaine d’un personnage, ajoutant un élément de surprise et de danger supplémentaire pendant le combat.

L’effet est géré par la fonction evenement_mort_subite(joueurs) dans main.py, appelée au début de chaque tour.

Cette fonctionnalité rend le jeu plus imprévisible et oblige le joueur à adapter sa stratégie à tout moment.


Il faut lancer le fichier main.py avec Python 3.


LIEN GIT
https://github.com/amar78-alt/RPG-Projet-Python/tree/main

