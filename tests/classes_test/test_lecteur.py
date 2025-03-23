from src.lecteur_interface import LecteurBadge

class TestLecteurBadge(LecteurBadge):
    def __init__(self):
        self.badge_detecte = None
    
    def verifier_badge(self) -> int | None:
        if self.badge_detecte is True:
            self.badge_detecte = None
            return 0
        return None
    
    def simuler_detection_badge_valide(self):
        self.badge_detecte = True
    def simuler_detection_badge_invalide(self):
        self.badge_detecte = False