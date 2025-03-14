import unittest
from tests.classes_test.test_lecteur import TestLecteurBadge
from src.badge import Badge
from src.systeme_validation import SystemeValidation
from tests.classes_test.test_systeme_porte import TestSystemePorte
import sys
import os

# 1.Présentation du badge au lecteur
# 2.Lecteur interroge le badge
# 3.Lecteur lance un signal d'accès ou de refus
class TestCases(unittest.TestCase):
    
    # Test 
    def test_cas_nominal(self):
    # ETANT DONNE un badge valide présenté au lecteur
        lecteur_badge = TestLecteurBadge()
        lecteur_badge.simuler_detection_badge()

    # ET une porte
        porte = TestSystemePorte()

    # QUAND le lecteur est interrogé
        SystemeValidation([porte], [lecteur_badge]).interroger_lecteur()

    # ALORS la porte reçoit un signal d'ouverture
        self.assertTrue(porte.signal)

    
    def test_sans_detection(self):
        # ETANT DONNE un lecteur n'ayant pas détecté de badge
        lecteur = TestLecteurBadge()
    
        # ET une porte
        porte = TestSystemePorte()
    
        # QUAND le contrôleur interroge ce lecteur
        SystemeValidation(porte, [lecteur]).interroger_lecteur()
    
        # ALORS la porte ne reçoit pas de signal d'ouverture
        self.assertFalse(porte.signal)
 
    def test_sans_interrogation(self):
        # ETANT DONNE un lecteur ayant détecté un badge valide
        lecteur = TestLecteurBadge()
        lecteur.simuler_detection_badge()
    
        # ET une porte
        porte = TestSystemePorte()
    
        # ET un contrôleur
        SystemeValidation(porte, lecteur)
    
        # ALORS la porte ne reçoit pas de signal d'ouverture
        self.assertFalse(porte.signal)

    def test_multiples_portes_badge_valide(self):
        # ETANT DONNE un lecteur associé à plusieurs portes
        lecteur = TestLecteurBadge()
        porte1 = TestSystemePorte()
        porte2 = TestSystemePorte()  

        # QUAND un badge valide est présenté au lecteur
        lecteur.simuler_detection_badge()
        SystemeValidation([porte1, porte2], [lecteur]).interroger_lecteur()

        # ALORS toutes les portes associées s'ouvrent
        self.assertTrue(porte1.signal)
        self.assertTrue(porte2.signal)

    def test_multiples_portes_badge_invalide(self):
        # ETANT DONNE un lecteur associé à un porte
        lecteur = TestLecteurBadge()
        porte1 = TestSystemePorte()
        porte2 = TestSystemePorte()  

        # QUAND un badge non valide est présenté au lecteur
        lecteur.simuler_detection_badge_invalide()
        SystemeValidation([porte1, porte2], [lecteur]).interroger_lecteur()

        # ALORS toutes les portes associées s'ouvrent
        self.assertFalse(porte1.signal)
        self.assertFalse(porte2.signal)

    def test_multiples_lecteurs_badge_valide(self):
        # ETANT DONNE plusieurs lecteurs associés à une porte
        lecteur1 = TestLecteurBadge()
        lecteur2 = TestLecteurBadge()
        porte1 = TestSystemePorte() 

        # QUAND un badge valide est présenté au lecteur
        lecteur1.simuler_detection_badge()
        lecteur2.simuler_detection_badge()
        SystemeValidation([porte1], [lecteur1, lecteur2]).interroger_lecteur()

        # ALORS toutes la porte associée s'ouvrent
        self.assertTrue(porte1.signal)

    def test_multiples_lecteurs_badge_invalide(self):
        # ETANT DONNE plusieurs lecteurs associés à une porte
        lecteur1 = TestLecteurBadge()
        lecteur2 = TestLecteurBadge()
        porte1 = TestSystemePorte() 

        # QUAND un badge non valide est présenté au lecteur
        lecteur1.simuler_detection_badge_invalide()
        lecteur2.simuler_detection_badge_invalide()
        SystemeValidation([porte1], [lecteur1, lecteur2]).interroger_lecteur()

        # ALORS toutes la porte associée reste fermée
        self.assertFalse(porte1.signal)

    def test_multiples_lecteurs_un_badge_invalide_et_un_valide(self):
        # ETANT DONNE plusieurs lecteurs associés à une porte
        lecteur1 = TestLecteurBadge()
        lecteur2 = TestLecteurBadge()
        porte1 = TestSystemePorte() 

        # QUAND un badge valide est présenté au lecteur
        lecteur1.simuler_detection_badge()
        lecteur2.simuler_detection_badge_invalide()
        SystemeValidation([porte1], [lecteur1, lecteur2]).interroger_lecteur()

        # ALORS toutes la porte associée s'ouvre
        self.assertTrue(porte1.signal)


    def test_un_lecteur_un_badge_invalide_et_un_valide(self):
        # ETANT DONNE un lecteur associé à une porte
        lecteur = TestLecteurBadge()
        porte = TestSystemePorte() 

        # QUAND un badge valide et un badge invalide sont présentés au lecteur
        lecteur.simuler_detection_badge()
        lecteur.simuler_detection_badge_invalide()
        SystemeValidation([porte], [lecteur]).interroger_lecteur()

        # ALORS la porte s'ouvre, même si un badge invalide est aussi présenté
        self.assertTrue(porte.signal)


    if __name__ == '__main__':
        unittest.main()


      

