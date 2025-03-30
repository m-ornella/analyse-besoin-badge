import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from classes_test.test_lecteur import TestLecteurBadge
from src.systeme_validation import SystemeValidation
from classes_test.test_systeme_porte import TestSystemePorte

# 1.Présentation du badge au lecteur
# 2.Lecteur interroge le badge
# 3.Lecteur lance un signal d'accès ou de refus
class TestCases(unittest.TestCase):
    
    # 1) Test cas nominal : un badge valide, 1 porte, 1 lecteur
    def test_cas_nominal(self):
    # ETANT DONNE un badge valide présenté au lecteur
        lecteur_badge = TestLecteurBadge()
        lecteur_badge.simuler_detection_badge_valide()

    # ET une porte
        porte = TestSystemePorte(nbre_badges_requis=1)

    # QUAND le lecteur est interrogé
        SystemeValidation([porte], [lecteur_badge]).interroger_lecteur()

    # ALORS la porte reçoit un signal d'ouverture
        self.assertTrue(porte.signal)

    # 2) Aucun badge détecté
    def test_sans_detection(self):
        # ETANT DONNE un lecteur n'ayant pas détecté de badge
        lecteur = TestLecteurBadge()
    
        # ET une porte
        porte = TestSystemePorte(nbre_badges_requis=1)
    
        # QUAND le contrôleur interroge ce lecteur
        SystemeValidation([porte], [lecteur]).interroger_lecteur()
    
        # ALORS la porte ne reçoit pas de signal d'ouverture
        self.assertFalse(porte.signal)
 
    # 3) Badge détecté mais pas d’interrogation du système
    def test_sans_interrogation(self):
        # ETANT DONNE un lecteur ayant détecté un badge valide
        lecteur = TestLecteurBadge()
        lecteur.simuler_detection_badge_valide()
    
        # ET une porte
        porte = TestSystemePorte(nbre_badges_requis=1)
    
        # ET un contrôleur
        SystemeValidation(porte, lecteur)
    
        # ALORS la porte ne reçoit pas de signal d'ouverture
        self.assertFalse(porte.signal)

    # 4) Multiples portes avec un badge valide
    def test_multiples_portes_badge_valide(self):
        # ETANT DONNE un lecteur associé à plusieurs portes
        lecteur = TestLecteurBadge()
        porte1 = TestSystemePorte(nbre_badges_requis=1)
        porte2 = TestSystemePorte(nbre_badges_requis=1)  

        # QUAND un badge valide est présenté au lecteur
        lecteur.simuler_detection_badge_valide()
        SystemeValidation([porte1, porte2], [lecteur]).interroger_lecteur()

        # ALORS toutes les portes associées s'ouvrent
        self.assertTrue(porte1.signal)
        self.assertTrue(porte2.signal)

    # 5) Multiples portes avec un badge invalide
    def test_multiples_portes_badge_invalide(self):
        # ETANT DONNE un lecteur associé à un porte
        lecteur = TestLecteurBadge()
        porte1 = TestSystemePorte(nbre_badges_requis=1)
        porte2 = TestSystemePorte(nbre_badges_requis=1)  

        # QUAND un badge non valide est présenté au lecteur
        lecteur.simuler_detection_badge_invalide()
        SystemeValidation([porte1, porte2], [lecteur]).interroger_lecteur()

        # ALORS toutes les portes associées s'ouvrent
        self.assertFalse(porte1.signal)
        self.assertFalse(porte2.signal)

    # 6) Multiples lecteurs, badge valide
    def test_multiples_lecteurs_badge_valide(self):
        # ETANT DONNE plusieurs lecteurs associés à une porte
        lecteur1 = TestLecteurBadge()
        lecteur2 = TestLecteurBadge()
        porte1 = TestSystemePorte(nbre_badges_requis=1) 

        # QUAND un badge valide est présenté au lecteur
        lecteur1.simuler_detection_badge_valide()
        lecteur2.simuler_detection_badge_valide()
        SystemeValidation([porte1], [lecteur1, lecteur2]).interroger_lecteur()

        # ALORS toutes la porte associée s'ouvrent
        self.assertTrue(porte1.signal)

    # 7) Multiples lecteurs, badge invalide
    def test_multiples_lecteurs_badge_invalide(self):
        # ETANT DONNE plusieurs lecteurs associés à une porte
        lecteur1 = TestLecteurBadge()
        lecteur2 = TestLecteurBadge()
        porte1 = TestSystemePorte(nbre_badges_requis=1) 

        # QUAND un badge non valide est présenté au lecteur
        lecteur1.simuler_detection_badge_invalide()
        lecteur2.simuler_detection_badge_invalide()
        SystemeValidation([porte1], [lecteur1, lecteur2]).interroger_lecteur()

        # ALORS toutes la porte associée reste fermée
        self.assertFalse(porte1.signal)

    # 8) Multiples lecteurs, un badge valide et un invalide
    def test_multiples_lecteurs_un_badge_invalide_et_un_valide(self):
        # ETANT DONNE plusieurs lecteurs associés à une porte
        lecteur1 = TestLecteurBadge()
        lecteur2 = TestLecteurBadge()
        porte1 = TestSystemePorte(nbre_badges_requis=1) 

        # QUAND un badge valide est présenté au lecteur
        lecteur1.simuler_detection_badge_valide()
        lecteur2.simuler_detection_badge_invalide()
        SystemeValidation([porte1], [lecteur1, lecteur2]).interroger_lecteur()

        # ALORS toutes la porte associée s'ouvre
        self.assertTrue(porte1.signal)

    # 9) Un lecteur, un badge valide et un invalide
    def test_un_lecteur_un_badge_invalide_et_un_valide(self):
        # ETANT DONNE un lecteur associé à une porte
        lecteur = TestLecteurBadge()
        porte = TestSystemePorte(nbre_badges_requis=1) 

        # QUAND un badge valide et un badge invalide sont présentés au lecteur
        lecteur.simuler_detection_badge_valide()
        lecteur.simuler_detection_badge_invalide()
        SystemeValidation([porte], [lecteur]).interroger_lecteur()

        # ALORS la porte reste fermée
        self.assertFalse(porte.signal)

    # 10) Deux lecteurs, 2 badges valides requis, un seul badge valide présenté
    def test_deux_lecteurs_deux_badges_valides_requis_un_presente(self):
        # ETANT DONNE plusieurs lecteurs associés à une porte qui requiert 2 badges valides
        lecteur1 = TestLecteurBadge()
        lecteur2 = TestLecteurBadge()
        porte1 = TestSystemePorte(nbre_badges_requis=2) 

        # QUAND un seul badge valide est présenté à un seul lecteur
        lecteur1.simuler_detection_badge_valide()
        SystemeValidation([porte1], [lecteur1, lecteur2]).interroger_lecteur()

        # ALORS la porte reste fermée
        self.assertFalse(porte1.signal)

    # 11) Deux lecteurs, 2 badges valides requis, badges présentés : 1 valide + 1 invalide
    def test_deux_lecteurs_deux_badges_valides_requis_deux_presentes_un_valide(self):
        # ETANT DONNE plusieurs lecteurs associés à une porte qui requiert 2 badges valides
        lecteur1 = TestLecteurBadge()
        lecteur2 = TestLecteurBadge()
        porte1 = TestSystemePorte(nbre_badges_requis=2) 

        # QUAND deux badges sont présentés aux deux lecteurs : 1 valide + 1 invalide
        lecteur1.simuler_detection_badge_valide()
        lecteur2.simuler_detection_badge_invalide()
        SystemeValidation([porte1], [lecteur1, lecteur2]).interroger_lecteur()

        # ALORS la porte reste fermée
        self.assertFalse(porte1.signal)

    # 12) Deux lecteurs, 2 badges valides requis, deux badges valides
    def test_deux_lecteurs_deux_badges_requis_deux_valides(self):
        # ETANT DONNE plusieurs lecteurs associés à une porte qui requiert 2 badges valides
        lecteur1 = TestLecteurBadge()
        lecteur2 = TestLecteurBadge()
        porte1 = TestSystemePorte(nbre_badges_requis=2) 

        # QUAND deux badges valides sont présentés aux deux lecteurs
        lecteur1.simuler_detection_badge_valide()
        lecteur2.simuler_detection_badge_valide()
        SystemeValidation([porte1], [lecteur1, lecteur2]).interroger_lecteur()

        # ALORS la porte s'ouvre
        self.assertTrue(porte1.signal)

    # 13) Une porte mais aucun lecteur
    def test_une_porte_aucun_lecteur(self):
        # ETANT DONNE une porte
        porte = TestSystemePorte(nbre_badges_requis=1) 

        # QUAND aucun lecteur est associé
        SystemeValidation([porte], []).interroger_lecteur()

        # ALORS la porte reste fermée
        self.assertFalse(porte.signal)

    # 14) Deux détections successives de badge valide sur un même lecteur
    def test_deux_detection_de_badge_valides(self):
        # ETANT DONNE un lecteur associé à une porte
        lecteur = TestLecteurBadge()
        porte = TestSystemePorte(nbre_badges_requis=1) 

        # QUAND deux badges valides sont présentés au même lecteur
        lecteur.simuler_detection_badge_valide()
        lecteur.simuler_detection_badge_valide()

        # ALORS la porte s'ouvre
        SystemeValidation([porte], [lecteur]).interroger_lecteur()
        self.assertTrue(porte.signal)

    # 15) Même badge valide présenté plusieurs fois, mais porte requiert 2 badges
    def test_meme_badge_valide_plusieurs_fois_porte_2_requis(self):
        # ÉTANT DONNÉ une porte qui requiert 2 badges valides
        porte = TestSystemePorte(nbre_badges_requis=2)
        lecteur = TestLecteurBadge()

        # QUAND on simule plusieurs fois un *même* badge valide sur un même lecteur
        lecteur.simuler_detection_badge_valide()
        lecteur.simuler_detection_badge_valide()

        # ALORS la porte reste fermée si on considère qu'il faut 2 badges valides distincts
        SystemeValidation([porte], [lecteur]).interroger_lecteur()
        self.assertFalse(porte.signal)

    # 16) Vérifier si la porte se "réinitialise" après ouverture quand on ré-interroge
    def test_reinitialisation_de_la_porte_apres_ouverture(self):
        # ÉTANT DONNÉ une porte requérant 1 badge
        porte = TestSystemePorte(nbre_badges_requis=1)
        lecteur = TestLecteurBadge()

        # QUAND un badge valide est présenté => on interroge => la porte s'ouvre
        lecteur.simuler_detection_badge_valide()
        SystemeValidation([porte], [lecteur]).interroger_lecteur()
        self.assertTrue(porte.signal)

        # ET on relance une interrogation sans présenter de badge valide
        porte.signal = False
        lecteur.badge_detecte = None 
        SystemeValidation([porte], [lecteur]).interroger_lecteur()

        # ALORS la porte reste fermée
        self.assertFalse(porte.signal)

    # 17) L'ordre de présentation ne doit pas influer (2 badges requis)
    def test_inversion_des_lecteurs_dont_2_sont_valides(self):
        # ÉTANT DONNÉ deux lecteurs et une porte qui requiert 2 badges valides
        porte = TestSystemePorte(nbre_badges_requis=2)
        lecteur1 = TestLecteurBadge()
        lecteur2 = TestLecteurBadge()

        # QUAND on présente d'abord un badge valide au lecteur2, puis au lecteur1
        lecteur2.simuler_detection_badge_valide()
        lecteur1.simuler_detection_badge_valide()
        SystemeValidation([porte], [lecteur1, lecteur2]).interroger_lecteur()

        # ALORS la porte s'ouvre (l'ordre n'importe pas)
        self.assertTrue(porte.signal)

    # 18) Plusieurs portes, aucun lecteur
    def test_plusieurs_portes_aucun_lecteur(self):
        # ÉTANT DONNÉ plusieurs portes
        porte1 = TestSystemePorte(nbre_badges_requis=1)
        porte2 = TestSystemePorte(nbre_badges_requis=2)

        # QUAND on interroge sans aucun lecteur
        SystemeValidation([porte1, porte2], []).interroger_lecteur()

        # ALORS toutes les portes restent fermées
        self.assertFalse(porte1.signal)
        self.assertFalse(porte2.signal)

    # 19) Trois lecteurs, 2 badges requis, seulement 2 badges valides détectés
    def test_trois_lecteurs_deux_badges_requis_deux_valides(self):
        # ÉTANT DONNÉ une porte requérant 2 badges valides et 3 lecteurs
        porte = TestSystemePorte(nbre_badges_requis=2)
        lecteur1 = TestLecteurBadge()
        lecteur2 = TestLecteurBadge()
        lecteur3 = TestLecteurBadge()

        # QUAND deux lecteurs détectent un badge valide, le troisième rien
        lecteur1.simuler_detection_badge_valide()
        lecteur2.simuler_detection_badge_valide()
        # lecteur3 reste None
        SystemeValidation([porte], [lecteur1, lecteur2, lecteur3]).interroger_lecteur()

        # ALORS la porte s'ouvre
        self.assertTrue(porte.signal)

    # 20) Trois lecteurs, 1 badge requis, seulement 1 badge valide détecté
    def test_trois_lecteurs_un_badge_requis_un_valide(self):
        # ÉTANT DONNÉ une porte requérant 1 badge valide et 3 lecteurs
        porte = TestSystemePorte(nbre_badges_requis=1)
        lecteur1 = TestLecteurBadge()
        lecteur2 = TestLecteurBadge()
        lecteur3 = TestLecteurBadge()

        # QUAND seul lecteur2 détecte un badge valide
        lecteur2.simuler_detection_badge_valide()
        SystemeValidation([porte], [lecteur1, lecteur2, lecteur3]).interroger_lecteur()

        # ALORS la porte s'ouvre
        self.assertTrue(porte.signal)

    # 21) Deux lecteurs, 1 badge requis, un invalide et l'autre pas de détection
    def test_lecteur_invalide_et_lecteur_vide_door_1_badge(self):
        # ÉTANT DONNÉ deux lecteurs associés à une porte qui requiert 1 badge
        porte = TestSystemePorte(nbre_badges_requis=1)
        lecteur1 = TestLecteurBadge()
        lecteur2 = TestLecteurBadge()

        # QUAND lecteur1 détecte un badge invalide, lecteur2 n'a pas de badge
        lecteur1.simuler_detection_badge_invalide()
        # lecteur2 reste None

        SystemeValidation([porte], [lecteur1, lecteur2]).interroger_lecteur()

        # ALORS la porte reste fermée
        self.assertFalse(porte.signal)

    # 23) Porte nécessitant 0 badges (scénario extrême : la porte s'ouvre toujours)
    def test_porte_zero_badge_requis(self):
        # ÉTANT DONNÉ une porte n'ayant besoin d'aucun badge
        porte = TestSystemePorte(nbre_badges_requis=0)
        lecteur = TestLecteurBadge()

        # QUAND on interroge le système, même si aucun badge n'est valide
        SystemeValidation([porte], [lecteur]).interroger_lecteur()

        # ALORS la porte s'ouvre immédiatement (nbre_badges_requis=0)
        self.assertTrue(porte.signal)

    # 24) Porte nécessitant 1 badge, 2 lecteurs, le premier lecteur valide puis efface son badge avant interrogation
    def test_lecteur_valide_puis_efface_badge_avant_interrogation(self):
        # ÉTANT DONNÉ une porte (1 badge requis) et 2 lecteurs
        porte = TestSystemePorte(nbre_badges_requis=1)
        lecteur1 = TestLecteurBadge()
        lecteur2 = TestLecteurBadge()

        # QUAND le lecteur1 simule d'abord un badge valide, puis le "retire" (None) avant que le système n'interroge    
        lecteur1.simuler_detection_badge_valide()
        lecteur1.badge_detecte = None # "Effacement" du badge détecté (simule un changement d'état avant interrogation)
        # lecteur2 reste sans badge
        SystemeValidation([porte], [lecteur1, lecteur2]).interroger_lecteur()

        # ALORS la porte reste fermée
        self.assertFalse(porte.signal)

if __name__ == '__main__':
    unittest.main()