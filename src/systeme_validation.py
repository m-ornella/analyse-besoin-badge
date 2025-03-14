from src.lecteur_interface import LecteurBadge
from src.porte_interface import Porte

class SystemeValidation():
    def __init__(self, portes: list[Porte], lecteurs: list[LecteurBadge]):
        self.__lecteurs = lecteurs
        self.__portes = portes
        

    def interroger_lecteur(self):
    # Count the number of valid badges detected by all readers
        nbr_badges_valides = sum(1 for lecteur in self.__lecteurs if lecteur.verifier_badge() is not None)

        # Iterate over each door
        for porte in self.__portes:
            # Open the door if the required number of valid badges is met
            if nbr_badges_valides >= porte.nbre_badges_requis:  # Use the requirement for each door
                porte.demander_ouverture()  # Open the door
  
