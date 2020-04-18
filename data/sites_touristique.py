from data.zone_touristique import zone
class site(zone):
    def __init__(self,zone,name):
        zone.__init__(self,zone)
        self.name=name
