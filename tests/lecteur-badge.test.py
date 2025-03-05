import unittest
from .lecteur_badge import LecteurBadge
from .badge import Badge
from .systme_validation import SystemeValidation
from .systeme-porte import SystemePorte

# 1.Présentation du badge au lecteur
# 2.Lecteur interroge le badge
# 3.Lecteur lance un signal d'accès ou de refus
class TestLecteurBadge:
    
    def test_cas_nominal(self):
    # ETANT DONNE un badge valide présenté au lecteur
        lecteur_badge = LecteurBadge()
        lecteur_badge.lire_badge()

    # QUAND le lecteur est interrogé
        systeme_validation = SystemeValidation()
        systeme_validation.interroger_badge()

    # ALORS un signal d'ouverture est lancé
        self.AssertEqual(True,systeme_validation.lancer_signal())

    
    def test_badge_non_valide(self):
    # ETANT DONNE un badge non valide présenté au lecteur
        lecteur_badge = LecteurBadge()
        lecteur_badge.lire_badge()

    # QUAND le lecteur est interrogé
        systeme_validation = SystemeValidation()
        systeme_validation.interroger_badge()

    # ALORS le lecteur lance un signal de refus d'accès
        self.AssertEqual(False,systeme_validation.lancer_signal())
       
