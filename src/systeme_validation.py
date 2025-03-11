from src.lecteur_interface import LecteurBadge
from src.porte_interface import Porte

class SystemeValidation():
    def __init__(self, portes: list[Porte], lecteur: LecteurBadge):
        self.__lecteur = lecteur
        self.__portes = portes
        

    def interroger_lecteur(self):
        if self.__lecteur.verifier_badge() is not None:
            for porte in self.__portes:
                porte.demander_ouverture()

  
