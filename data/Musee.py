from data.sites_touristique import site
class musee(site):
    def __init__(self,zone,name,Lieu,INTR,theme,Visit,tarif):
        site.__init__(self,zone,name)
        self.Lieu=Lieu
        self.INTR=INTR
        self.theme=theme
        self.Visit=Visit
        self.tarif=tarif
