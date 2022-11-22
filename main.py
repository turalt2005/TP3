# Troy Tural 404
# TP3

import random

Quit = 'n'
nb_vies = 20
monstres = random.randint (1, 5)
de = random.randint (1, 6)
regles_jeu = "Bienvenue! Dans cette aventure, tu auras l'option de combattre des monstres avec des vies montant de 1 à 5.\n" \
             "Tu as 20 vies. Si tu decide de le combattre avec le nombre 1,tu laceras 2 dés avec des valeurs de 1 à 6 chancun.\n" \
             "Si le resulat est plus bas que le nbr de vies du monstre, tu perdera des vies egale aux vies du monstre. Perd tous les 20 et c`est partie terminée!\n"\
             "Quand tu gagne, tu gangera des points egale au vies du monstre battue.\n" \
             "Si tu decide de cliquer 2, tu echappera le combat, mais si tu decide de faire cela, tu perdera une vie.\n" \
             "Clique 3 et tu pourra voir ce message\n" \
             "Clique 4, et tu quitter le jeu.\n" \
             "BONNE PARTIE!!! :D"
while Quit == 'n':
    choix = input("Que desirez-vous faire?" \
                   "1- Combattre\n"
                   "2- Contourner et aller ouvrir une autre porte\n" \
                   "3- Revoir les règles du jeu\n" \
                   "4- Arrêter le jeu")

    if choix == 1:
        print(nb_vies)
        print(monstres)
        if de > monstres:
            nb_vies = nb_vies + monstres
            print("Victoire!")
        if de <= monstres:
            nb_vies = nb_vies - monstres


    if choix == 2:
        nb_vies - 1
        print("Vous vous echappez du combat! Mais en consequence, vous perdez une vie...")

    if choix == 3:
        print(regles_jeu)

    if choix ==4:

