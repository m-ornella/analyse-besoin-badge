from src.porte_interface import Porte


class TestSystemePorte(Porte):
    def __init__(self, nbre_badges_requis=1):
        self.nbre_badges_requis = nbre_badges_requis
        self.signal = False
    
    def demander_ouverture(self):
        if not self.signal:
            self.signal = True
        return self.signal
