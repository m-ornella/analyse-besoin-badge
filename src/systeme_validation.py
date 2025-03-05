from lecteur_interface import LecteurBadge
from porte_interface import Porte

class SystemeValidation():
    def __init__(self, porte: Porte, lecteur: LecteurBadge):
        self.__lecteur = lecteur
        self.__porte = porte

    def interroger_lecteur(self):
        if self.__lecteur.verifier_badge() is not None:
            self.__porte.demander_ouverture() 

  
