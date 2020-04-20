import numpy as np
import sys
from exec.creation import *


def str_to_class(classname):              #on convertie le nom d'une class vers le type class
    return getattr(sys.modules[__name__], classname)

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
    for i in o1:
        print("----theme :" + i)
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


def creation(T1,T2):                             #on cree une liste qui s'alterne entre nom du site et nombre associe
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
    dis=0                                       #un compteur de distance
    l1=['Tour Hassan','Oudaya','Chellah','Le Muse Mohammed VI','Muse Belghazi','Muse Maroc Tlcom','Village de poterie Oulja','Ancienne Medina Rabat','Oued Bouregreg','Jardin exotique']
    l11=[i for i in range(len(l1))]
    l2=["Palais Bahia","Palais El Badie","Musée du parfum","Musée Dar si Said","Musée Berbère du jardin Majorelle","Souk Fekharine","Souk Zrabi","La vallée de l'Ourika","Cascades d’ouzoud"]
    l22=[i for i in range(len(l2))]
    l111=creation(l1,l11)
    l222=creation(l2,l22)
    d1=listToDict(l111)        #par la fonction listToDict on va cree un dictionnaire avec les noms comme clef et les nombres comme valeur
    d2=listToDict(l222)
    s=[]
    if zone1.zone=="rabat-sale":
        print("Voici la liste des sites disponibles :")
        for i in l1:
            print("----site :" + i)
        for i in range(k):
            print("Veuillez preciser le nom du site touristique à visiter :")
            char=str(input())
            while (char not in d1):
                print("Oups mauvais choix!! entrer une autre zone ^^")
                char=str(input())
            s.append(char)
        matrix= np.loadtxt('matrice1.txt', usecols=range(10))  #on importe notre matrice a l'aide de numpy pour pouvoire faire des traitements
        for i in range(len(s)-1):
            dis+=matrix[d1[s[i]]][d1[s[i+1]]]
        print("la distance de cet intineraire est: " + str(dis) +"km")
        print("-"*92)
        print("-"*92)
    else:
        print("Voici la liste des sites disponibles :")
        for i in l2:
            print("----site :" + i)
        for i in range(k):
            print("Veuillez preciser le nom du site touristique à visiter :")
            char = str(input())
            while (char not in d2):
                print("Oups mauvais choix!! entrer une autre zone ^^")
                char = str(input())
            s.append(char)
        matrix= np.loadtxt('matrice2.txt', usecols=range(9))
        for i in range(len(s)-1):
            dis+=matrix[d2[s[i]]][d2[s[i+1]]]
        print("la distance de cet intineraire est: " + str(dis) +"km")
        print("-"*92)
        print("-"*92)
