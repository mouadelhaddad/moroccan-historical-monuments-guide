from data.sites_touristique import site
class prod(site):
    def __init__(self,zone,name,Lieu,INTR,theme,Visit):
        site.__init__(self,zone,name)
        self.Lieu=Lieu
        self.INTR=INTR
        self.theme=theme
        self.Visit=Visit
