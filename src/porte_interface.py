import abc


class Porte((abc.ABC)):
    @abc.abstractmethod
    def __init__(self, nbre_badges_requis=1):
        self.nbre_badges_requis = nbre_badges_requis
        self.signal = False

    def demander_ouverture(self):
        pass