# Troy Tural 404
# TP3

import random

# fonction pour effectuer le combat en lançant les dés ; input : force du monstre et output: 'victoire' ou 'défaite'
def combat (force):
    de1 = random.randint (1, 6)
    de2 = random.randint (1, 6)
    resultat = de1 + de2
    if resultat > force:
        return "VICTOIRE!!!"
    return "Echec..."

#Ces variables servent comme base du combat des monstres
nb_vies = 20
monstres = 0
nbr_combat = 0
nbr_victoires_de_suite = 0
force_de_base = 2
force_maximale = 11
monstres = random.randint(force_de_base, force_maximale)
#Cette condition va faire en sorte que tant que nos nombres de vies restants est plus que 0, on pourra jouer au jeu
while nb_vies > 0:
    monstres = random.randint(force_de_base, force_maximale)
    choix = input ("Que desirez-vous faire?" \
         "1- Combattre\n"
         "2- Contourner et aller ouvrir une autre porte\n" \
         "3- Revoir les règles du jeu\n" \
         "4- Arrêter le jeu")

#Choix 1 est ce qui determine le fonctionnement des combats
    if choix == str(1):
        print("Vos vies:",nb_vies)
        print("Vis de l'adversaire:",monstres)
        de1 = random.randint(1, 6)
        de2 = random.randint(1, 6)
        resultat = de1 + de2
        if resultat > monstres:
            nb_vies = nb_vies + monstres
            print("Resultat des 2 dees:", resultat)
            print("Victoire!")
            print("Vos nouvelles vies:",nb_vies )
        if resultat <= monstres:
            nb_vies -= monstres
            print("Resultat des 2 dees:", resultat)
            print("Defaite...")
            print("Vos vies restants:", nb_vies)
        if nbr_victoires_de_suite > 2:
                    print("Vous allez maintenant combattre un monstre plus fort jusqu'a votre prochaine defaite")
#Choix 2 fait en sorte qu'on peut eviter un combat, mais en fesant ceci, on perd 1 vie et les vies peuvent descendre jusqu'a 0.
    if choix == str(2):
        nb_vies -= 1
        monstres += 1
        print("Vous vous echappez du combat! Mais en consequence, vous perdez une vie...")
        print(nb_vies)
        monstres = random.randint(force_de_base, force_maximale)
#Choix 3 est pour si on desire revoir les regles du jeu
    if choix == str(3):
        print("Pour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de l’adversaire.  Dans ce cas, le niveau de vie de l’usager est augmenté de la force de l’adversaire."
              "Une défaite a lieu lorsque la valeur du dé lancé par l’usager est inférieure ou égale à la force de l’adversaire.  Dans ce cas, le niveau de vie de l’usager est diminué de la force de l’adversaire."
              "La partie se termine lorsque les points de vie de l’usager tombent sous 0." )
#Choix 4 est si on desire quitter le jeu si on n'a plus envie de jouer
    if choix == str(4):
        Quit = input('Voulez-vous quitter? y/n')
        if Quit == 'y':
            print("Merci d'avoir joué!!")
            print("votre score est: ",nb_vies)
            nb_vies = 0
#Cette partie du code fait en sorte que si nos nombres de vies descendent a 0 ou moins, la partie se terminera automatiquement
    if nb_vies == 0:
        print (nb_vies)
        print ("Merci d'avoir joué!")
