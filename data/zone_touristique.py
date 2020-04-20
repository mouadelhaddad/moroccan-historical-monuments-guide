class zone:
    T = ["rabat-sale","Marrakech"]
    def __init__(self,zone):
        self.zone=zone
    def confirm(self):
        return self.zone in self.T
