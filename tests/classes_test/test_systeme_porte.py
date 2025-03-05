from src.porte_interface import Porte


class TestSystemePorte(Porte):
    def __init__(self):
        signal = False

    def signal_ouverture_recu(self):
        return self.signal
    
    def demander_ouverture(self):
        self.signal = True
