from data.sites_touristique import site
class naturel(site):
    def __init__(self,zone,name,Lieu,INTR):
        site.__init__(self,zone,name)
        self.Lieu=Lieu
        self.INTR=INTR
