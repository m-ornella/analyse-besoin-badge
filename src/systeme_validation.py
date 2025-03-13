from src.lecteur_interface import LecteurBadge
from src.porte_interface import Porte

class SystemeValidation():
    def __init__(self, portes: list[Porte], lecteurs: list[LecteurBadge]):
        self.__lecteurs = lecteurs
        self.__portes = portes
        

    def interroger_lecteur(self):
        for lecteur in self.__lecteurs:
            if lecteur.verifier_badge() is not None:
                for porte in self.__portes:
                    porte.demander_ouverture()


  
