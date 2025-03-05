import unittest
from tests.classes_test.test_lecteur import TestLecteurBadge
from src.badge import Badge
from src.systeme_validation import SystemeValidation
from tests.classes_test.test_systeme_porte import TestSystemePorte
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

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
        systeme_porte = TestSystemePorte()

    # QUAND le lecteur est interrogé
        SystemeValidation(systeme_porte, lecteur_badge).interroger_lecteur()

    # ALORS la porte reçoit un signal d'ouverture
        self.assertTrue(systeme_porte.signal_ouverture_recu)

    


    # def test_sans_detection(self):
    #         # ETANT DONNE un lecteur n'ayant pas détecté de badge
    #         lecteur = TestLecteurBadge()
    
    #         # ET une porte
    #         porte = TestSystemePorte()
    
    #         # QUAND le contrôleur interroge ce lecteur
    #         SystemeValidation(porte, lecteur).interroger_lecteur()
    
    #         # ALORS la porte ne reçoit pas de signal d'ouverture
    #         self.assertFalse(porte.signal_ouverture_reçu)
 
    # def test_sans_interrogation(self):
    #         # ETANT DONNE un lecteur ayant détecté un badge valide
    #         lecteur = TestLecteurBadge()
    #         lecteur.simuler_detection_badge()
    
    #         # ET une porte
    #         porte = TestSystemePorte()
    
    #         # ET un contrôleur
    #         SystemeValidation(porte, lecteur)
    
    #         # ALORS la porte ne reçoit pas de signal d'ouverture
    #         self.assertFalse(porte.signal_ouverture_reçu)

    # # Test 
    # def test_signal_validation_envoyé_au_systeme_porte(self):
    # # ETANT DONNE un systeme qui envoit un signal d'accès
    #     systeme_validation = SystemeValidation()

    # # QUAND le lecteur est interrogé
    #     systeme_validation.lancer_signal()
    #     systeme_porte = SystemeValidation()

    # # ALORS le système de validation lance un signal d'autorisation d'accès
    #     self.AssertEqual(True,systeme_porte.recevoir_signal())


    # # Test 
    # def test_signal_refus_envoyé_au_systeme_porte(self):
    # # ETANT DONNE un systeme qui envoit un signal d'accès
    #     systeme_validation = SystemeValidation()

    # # QUAND le lecteur est interrogé
    #     systeme_validation.lancer_signal()
    #     systeme_porte = TestSystemePorte()

    # # ALORS le système de validation lance un signal d'autorisation d'accès
    #     self.AssertEqual(False,systeme_porte.recevoir_signal())

    
       

if __name__ == '__main__':
    unittest.main()