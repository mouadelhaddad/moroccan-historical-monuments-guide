from data.zone_touristique import zone
from data.sites_touristique import site
from data.Site_de_production import prod
from data.Musee import musee
from data.Site_de_naturel_remarquable import naturel
from data.Monument_historique import monument
import numpy as np
import sys


zone1=zone()
zone1.name=zone1.T[0]
monument1=monument(zone1.T[0],"tour hassan","Découvrir l’histoire et le patrimoine de la ville de Rabat","Histoire")
monument2=monument(zone1.T[0],"oudaya","Découvrir l’histoire et le patrimoine de la ville de Rabat","Histoire")
monument3=monument(zone1.T[0],"chellah","Découvrir l’histoire et le patrimoine de la ville de Rabat","Histoire")

musee1=musee(zone1.T[0],"Le Musée Mohammed VI", "Rabat centre-ville","Découvrir des œuvres artistiques modernes marocains et étrangers" ,"Art moderne", "Oui", "20 DH")
musee2=musee(zone1.T[0],"Musée Belghazi", "Sidi Bouknadel,Salé","Découvrir la culture marocaine traditionnelle" ,"Ethnographie", "Oui", "50 DH")
musee3=musee(zone1.T[0],"Musée Maroc Télécom", "Hay Riad,Rabat","Avoir une idée sur l’évolution des Télécoms au Marocs" ,"Télécommunications", "Non", "0 DH")

prod1=prod(zone1.T[0],"Village de poterie Oulja","Oulja, Salé","Découvrir et acheter des produits de poterie","Artisanat" ,"Non")
prod2=prod(zone1.T[0],"Ancienne Médina Rabat","Rabat ville","Acheter des produits d’artisanat","Artisanat" ,"Non")

nature1=naturel(zone1.T[0],"Oued Bouregreg","Entre Rabat et Salé"," Faire une balade fluviale en « Flouka »")
nature2=naturel(zone1.T[0],"Jardin exotique","Sidi Bouknadel, Salé"," Faire une balade dans un jardin qui abrite des plantes des cinq coins du monde.")
LZ=[monument1,monument2,monument3,musee1,musee2,musee3,prod1,prod2,nature1,nature2]

def th():
    L=[]
    for i in LZ:
        if hasattr(i,"theme"):
            L.append(i)
    return L
def vis():
    L=[]
    for i in LZ:
        if hasattr(i,"Visit"):
            L.append(i)
    return L

LT= th()
LV=vis()
C=['musee','naturel','prod','monument']

def str_to_class(classname):
    return getattr(sys.modules[__name__], classname)

def bienvenu():
    print('-'*31+"Bienvenu dans mon application "+'-'*31)
    print('-'*92)
    print('-'*92)
    print(' '*25+"Voulez-vous choisir une zone touristiques?"+' '*25)
    print('-' * 92)
    print('*'*32+"Liste des zones disponibles "+'*'*32)
    for i in zone1.T:
        print("zone : " +i)                       #on affiche les zones disponible
    zone_ch=str(input())
    while(zone_ch not in zone1.T):
        print("Oups mauvais choix!! entrer une autre zone parmis les zones deja afficher ^^")
        zone_ch = str(input())
    zone1.name=zone_ch

def affttsite():
    print("Voici la liste de tous les sites touristiques dans la zone que vous avez choisit ^^")
    for i in LZ:
        print("---site touristique :"+i.name)
    print("-"*92)
    print("-"*92)

def afftheme():
    print("Voici les themes proposes")
    O=[]
    for i in LT:
        O.append(i.theme)
    o1=list(set(O))
    for i in range(len(o1)):
        print("----theme :" + o1[i])
    print("Veuillez entrer un theme ^^")
    themeC = str(input())
    while(themeC not in O):
        print("Oups ce theme n'existe pas !! Veuillez entrer un autre theme ^^")
        themeC = str(input())
    for i in LT:
        if i.theme==themeC:
            print("---site touristique :"+i.name)
    print("-"*92)
    print("-"*92)

def cat():
    print("Voici les categories proposes")
    for i in C:
        print("---Categorie :" +i)
    print("Veuillez entrer une categorie ^^")
    Catg=str(input())
    while(Catg not in C):
        print("Oups cette categorie  n'est pas disponible !! Veuillez entrer une autre categorie ^^")
        Catg = str(input())
    for i in LZ:
        if isinstance(i, str_to_class(Catg)):
            print("---site touristique :"+i.name)
    print("-"*92)
    print("-"*92)

def visite():
    print("Voici les sites touristique qui proposent une visite guidée :")
    for i in LV:
        print("---site touristique :"+i.name)
    print("-"*92)
    print("-"*92)


def creation(T1,T2):                             #on cree une liste qui s'alterne entre nom du site et nombre octroie
    T3=[]
    for i in range(len(T1)):
        T3.append(T1[i])               #nom du site
        T3.append(T2[i])               #nombre donne
    return T3

def listToDict(lst):
    op = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}  #on cree un dictionnaire par une liste donne ou les cle et la valeur sont suivit
    return op

def intin():
    print("Veuillez preciser le nombre de sites a visiter : ")
    k=int(input())
    dis=0
    l1=['Tour Hassan','Oudaya','Chellah','Le Muse Mohammed VI','Muse Belghazi','Muse Maroc Tlcom','Village de poterie Oulja','Ancienne Medina Rabat','Oued Bouregreg','Jardin exotique']
    l2=[i for i in range(10)]
    l=creation(l1,l2)
    d=listToDict(l)
    s=[]
    print("Voici la liste des sites disponibles :")
    for i in l1:
        print("----site :" + i)
    for i in range(k):
        print("Veuillez preciser le nom du site touristique à visiter :")
        char=str(input())
        while (char not in d):
            print("Oups mauvais choix!! entrer une autre zone ^^")
            char=str(input())

        s.append(char)
    matrix= np.loadtxt('matrice.txt', usecols=range(10))
    for i in range(len(s)-1):
        dis+=matrix[d[s[i]]][d[s[i+1]]]
    print("la distance de cet intineraire est: " + str(dis) +"km")
    print("-"*92)
    print("-"*92)
