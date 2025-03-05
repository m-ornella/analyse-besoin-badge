import abc


class Porte((abc.ABC)):
    @abc.abstractmethod
    def signal_ouverture_recu(self):
        pass
    def demander_ouverture(self):
        pass