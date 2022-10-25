import pygame
from comet import Comet

# créer une classe pour gérer cet evenement
class CometFallEvent:

    # lors du chargement -> créer un compteur
    def __init__(self, game):
        self.percent = 0
        self.percent_speed = 250 * 3
        self.game = game

        # definir un groupe de sprite pour stocker les cometes
        self.all_comets = pygame.sprite.Group()

    def add_percent(self):
        self.percent += self.percent_speed / 500

    def is_full_loaded(self):
        return self.percent >=100

    def reset_persent(self):
        self.percent = 0

    def meteor_fall(self):
        # apparaitre la boule de feu
        self.all_comets.add(Comet(self))

    def attempt_fall(self):
        # la jauge d'event est totalement chargée
        if self.is_full_loaded():
            print("Pluie de cometes !")
            self.meteor_fall()
            self.reset_persent()

    def update_bar(self, surface):

        # ajouter du pourcentage à la bar
        self.add_percent()

        # appel de la méthode pour essayer  de declencher la pluie de comete
        self.attempt_fall()

        # barre noire en arrière plan
        pygame.draw.rect(surface, (0, 0, 0), [
            0, # axe des x
            surface.get_height() - 20, # l'axe des y
            surface.get_width(), # longueur de la fenetre
            10 # épaisseur de la barre
        ])
        # barre rouge d'event
        pygame.draw.rect(surface, (127,61,83,255), [
            0,  # axe des x
            surface.get_height() - 20,  # l'axe des y
            (surface.get_width() / 100) * self.percent,  # longueur de la fenetre
            10  # épaisseur de la barre
        ])