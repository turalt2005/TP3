# Troy Tural 404
# TP3

import random


def combat (force):
    de1 = random.randint (1, 6)
    de2 = random.randint (1, 6)
    resultat = de1 + de2
    if resultat > force:
        return "VICTOIRE!!!"
    return "Echec..."


nb_vies = 20
monstres = 0
nbr_combat = 0
nbr_victoires_de_suite = 0
force_de_base = 2
force_maximale = 11
monstres = random.randint(force_de_base, force_maximale)
while nb_vies > 0:
    monstres = random.randint(force_de_base, force_maximale)
    choix = input ("Que desirez-vous faire?" \
         "1- Combattre\n"
         "2- Contourner et aller ouvrir une autre porte\n" \
         "3- Revoir les règles du jeu\n" \
         "4- Arrêter le jeu")


    if choix == str(1):
        print(nb_vies)
        print(monstres)
        de1 = random.randint(1, 6)
        de2 = random.randint(1, 6)
        resultat = de1 + de2
        if resultat > monstres:
            nb_vies = nb_vies + monstres
            print("Victoire!")
        if resultat <= monstres:
            print("Defaite...")
            nb_vies -= monstres
        if nbr_victoires_de_suite > 2:
                    print("Vous allez maintenant combattre un monstre plus fort jusqu'a votre prochaine defaite")

    if choix == str(2):
        nb_vies -= 1
        monstres += 1
        print("Vous vous echappez du combat! Mais en consequence, vous perdez une vie...")
        print(nb_vies)
        monstres = random.randint(force_de_base, force_maximale)

    if choix == str(3):
        print("Pour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de l’adversaire.  Dans ce cas, le niveau de vie de l’usager est augmenté de la force de l’adversaire."
              "Une défaite a lieu lorsque la valeur du dé lancé par l’usager est inférieure ou égale à la force de l’adversaire.  Dans ce cas, le niveau de vie de l’usager est diminué de la force de l’adversaire."
              "La partie se termine lorsque les points de vie de l’usager tombent sous 0." )

    if choix == str(4):
        Quit = input('Voulez-vous quitter? y/n')
        if Quit == 'y':
            print("Merci d'avoir joué!!")
            print("votre score est: ",nb_vies)
            nb_vies = 0

    if nb_vies == 0:
        print (nb_vies)
        print ("Merci d'avoir joué!")
