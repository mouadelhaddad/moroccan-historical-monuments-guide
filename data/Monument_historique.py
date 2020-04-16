from data.sites_touristique import site
class monument(site):
    def __init__(self,zone,name,INTR,theme):
        site.__init__(self,zone,name)
        self.INTR=INTR
        self.theme=theme
