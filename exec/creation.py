from data.zone_touristique import zone
from data.sites_touristique import site
from data.Site_de_production import production
from data.Musee import musee
from data.Site_de_naturel_remarquable import naturel
from data.Monument_historique import monument


zone1=zone("default")
LZ=[]

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
    while(zone1.confirm()):
        print("Oups mauvais choix!! entrer une autre zone parmis les zones deja afficher ^^")
        zone_ch = str(input())
    zone1.zone=zone_ch


if zone1.zone==zone1.T[0]:
    monument1=monument(zone1.zone,"tour hassan","Découvrir l’histoire et le patrimoine de la ville de Rabat","Histoire")
    monument2=monument(zone1.zone,"oudaya","Découvrir l’histoire et le patrimoine de la ville de Rabat","Histoire")
    monument3=monument(zone1.zone,"chellah","Découvrir l’histoire et le patrimoine de la ville de Rabat","Histoire")

    musee1=musee(zone1.zone,"Le Musée Mohammed VI", "Rabat centre-ville","Découvrir des œuvres artistiques modernes marocains et étrangers" ,"Art moderne", "Oui", "20 DH")
    musee2=musee(zone1.zone,"Musée Belghazi", "Sidi Bouknadel,Salé","Découvrir la culture marocaine traditionnelle" ,"Ethnographie", "Oui", "50 DH")
    musee3=musee(zone1.zone,"Musée Maroc Télécom", "Hay Riad,Rabat","Avoir une idée sur l’évolution des Télécoms au Marocs" ,"Télécommunications", "Non", "0 DH")

    prod1=production(zone1.zone,"Village de poterie Oulja","Oulja, Salé","Découvrir et acheter des produits de poterie","Artisanat" ,"Non")
    prod2=production(zone1.zone,"Ancienne Médina Rabat","Rabat ville","Acheter des produits d’artisanat","Artisanat" ,"Non")

    nature1=naturel(zone1.zone,"Oued Bouregreg","Entre Rabat et Salé"," Faire une balade fluviale en « Flouka »")
    nature2=naturel(zone1.zone,"Jardin exotique","Sidi Bouknadel, Salé"," Faire une balade dans un jardin qui abrite des plantes des cinq coins du monde.")
    LZ=[monument1,monument2,monument3,musee1,musee2,musee3,prod1,prod2,nature1,nature2]
else:
    monument1=monument(zone1.zone,"Palais Bahia","Explorer l’une des œuvres architecturales les plus importantes de Marrakech",	"Histoire")
    monument2=monument(zone1.zone,"Palais El Badie","Rappeler l’histoire de la défaite des Portugais à Oued al-Makhazen (la Bataille des Trois Rois)","Histoire")

    musee1=musee(zone1.zone,"Musée du parfum" ,"Marrakech Medina","Dédié à l’art et à l’histoire du parfum au Maroc. il propose des activités ludiques et des ateliers pour mieux appréhender cet univers si particulier","L’aromathérapie","Oui" ,"40 DH")
    musee2=musee(zone1.zone,"Musée Dar si Said","Marrakech -Derb Albania","Découvrir l’art populaire de Marrakech et des villages berbères environnants","l’art architectural domestique","Oui"," 15 DH")
    musee3=musee(zone1.zone,"Musée Berbère du jardin Majorelle","Marrakech - Gueliz","Savoir l’histoire et la géographie des Berbères (Amazighs) du Maroc","Art berbere","Oui","30 dhs")

    prod1=production(zone1.zone,"Souk Fekharine","Marrakech-medina","Découvrir l’art de la poterie marocaine","Poterie","Oui")
    prod2=production(zone1.zone,"Souk Zrabi","Marrakech-medina","Découvrir la diversité des tapis marocains" ,"Tapis et maroquinerie","Oui")

    nature1=naturel(zone1.zone,"La vallée de l'Ourika","30 km de Marrakech","Profiter des montagnes rocheuses , de l’air frais , partir en promenade sur les hauteurs de Setti-Fatma")
    nature2=naturel(zone1.zone,"Cascades d’ouzoud","150 km de Marrakech" ,"Un endroit majestueux , proposant une ballade dans les embarcations et un déjeuner avec une superbe vue")
    LZ=[monument1,monument2,musee1,musee2,musee3,prod1,prod2,nature1,nature2]


def th():                           #on cree une liste qui contien tous les sites avec une theme
    L=[]
    for i in LZ:
        if hasattr(i,"theme"):
            L.append(i)
    return L

def vis():                          #on cree une liste qui contien tous les sites avec une visite guidée
    L=[]
    for i in LZ:
        if hasattr(i,"Visit") and i.Visit=="Oui":
            L.append(i)
    return L

LT= th()
LV=vis()
C=['musee','naturel','production','monument'] #liste des categorie disponibles
