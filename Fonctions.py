def poucrentage_couleur(lego: list[str], couleur: str) -> float():
    """
    Fonction qui reçoit une liste de legos et une couleur et qui retourne le pourcentage de blocs de cette couleur
    :param lego: liste de lego
    :param couleur: couleur recherchée
    :return: pourcentage de lego de la couleur recherchée
    """
    pourcent_couleur=(lego.count(couleur)/len(lego))*100
    return pourcent_couleur









def attaque(attaque: list[int], defense: list[int]):
    """
    Fonction qui calcule des dégats recu par l'adversaire
    :param attaque: dégats infligé
    :param defense: liste de point de défense et de vie
    :return: vie du défendeur
    """
    vie_defendeur = 1000
    attaque = input("Combien de dégats vous posé sur le défendeur ?")


def moyenne_couleur_legos(liste_couleur_legos: list[str]):
    """
    fonction calculant la moyenne du nombre de blocs il y a par couleur
    :param liste_couleur_legos: liste comprenant la couleur de tout les legos
    :return:la moyenne
    """
    liste_nb_legos_couleur = []

    for i in range(len(liste_couleur_legos)):
        couleur = liste_couleur_legos[i]
        liste_nb_legos_couleur.append(liste_couleur_legos.count(couleur))
        while True:
            if couleur in liste_couleur_legos:
                liste_couleur_legos.remove(couleur)
            else:
                break

    somme = sum(liste_nb_legos_couleur)
    moyenne = somme//len(liste_nb_legos_couleur)
    return moyenne

#liste_couleur_legos = ["bleu","bleu","rouge","mauve","vert","rouge","rose","mauve","or","rose","bleu","rouge","vert","argent"]
#print(moyenne_couleur_legos(liste_couleur_legos))