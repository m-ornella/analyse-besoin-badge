from src.porte_interface import Porte


class TestSystemePorte(Porte):
    def __init__(self):
        self.signal = False
    
    def demander_ouverture(self):
        self.signal = True
        return self.signal
