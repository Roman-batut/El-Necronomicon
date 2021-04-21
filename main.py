#Imports
import Engine
import GameManager

#Main
if __name__ == "__main__" :

    #Dimensions de la fenêtre
    largeur = 768 
    longueur = 1024

    #Initialise le moteur
    moteur = Engine.Moteur(longueur, largeur)

    #On crée et initialise un manger qui va gérer le flow du jeu
    manager = GameManager.Manager(moteur)
    manager.Setup()

    ''''
    Vie = hauteur de barre qui diminue quand on se fait toucher 
    Power = intérieur de la barre (fluide) qui diminue lorsque utilisé
    moi jsuis pas dakor ça fo lsavoir
    '''

    #On fait tourner le manager
    manager.Run()
    #moteur.Run()

