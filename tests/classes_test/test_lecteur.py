from src.lecteur_interface import LecteurBadge

class TestLecteurBadge(LecteurBadge):
    def __init__(self):
        self.__numero_badge_detecte = None
    
    def verifier_badge(self) -> int | None:
            numero_detecte = self.__numero_badge_detecte
            self.__numero_badge_detecte = None
            return numero_detecte
    
    def simuler_detection_badge(self):
            self.__numero_badge_detecte = 0
    
    def simuler_detection_badge_invalide(self):
        self.badge_detecte = True
    def simuler_detection_badge_invalide(self):
        self.badge_detecte = False