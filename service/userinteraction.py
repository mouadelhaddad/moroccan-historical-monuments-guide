from service.gestion import *

def interact():
    l=0
    while(l!=6):
        print("Pour afficher tous les sites de la zone veuillez choisir: 1")
        print("Pour afficher les sites selon un theme donné veuillez choisir : 2")
        print("Pour afficher les sites selon une categorie donné veuillez choisir : 3")
        print("Pour afficher les sites qui proposent une visite guidée veuillez choisir : 4")
        print("Pour afficher la distance d'un intineraire passant par plusieurs villes veuillez choisir : 5")
        print("Pour Quitter le programme tapez : 6")
        l=int(input())
        if l==1:
            affttsite()
        elif l==2:
            afftheme()
        elif l==3:
            cat()
        elif l==4:
            visite()
        elif l==5:
            intin()
        elif l > 5 and l < 1:
            Print("Mauvais choix voici la liste dont vous pouvez choisir ^^")
