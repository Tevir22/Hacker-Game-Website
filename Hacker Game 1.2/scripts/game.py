import pygame
from player import Player
from monster import Monster
from comet_event import CometFallEvent

# classe qui va representer le jeu
from sounds import SoundManager

class Game:

    def __init__(self):
        # definir si notre jeu a commencé ou non
        self.is_playing = False
        # generer le player
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        # generer l'evenement
        self.comet_event = CometFallEvent(self)
        # groupe de monstre
        self.all_monsters = pygame.sprite.Group()
        # gerer le son
        self.sound_manager = SoundManager()
        # mettre le score à 0
        self.font = pygame.font.Font("assets/my_custom_font.ttf", 60)
        self.score = 0
        self.pressed = {}

    def start(self):
        self.is_playing = True
        self.spawn_monster()
        self.spawn_monster()

    def game_over(self):
        # remettre le jeu à neuf, retirer les monstres et remttre le joueur à 100 pdv
        self.all_monsters = pygame.sprite.Group()
        self.comet_event.all_comets = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.comet_event.reset_persent()
        self.is_playing = False
        self.score = 0
        # jouer le son
        self.sound_manager.play('game_over')

    def update(self, screen):
        # afficher le score sur l'écran
        score_text = self.font.render(f"Score : {self.score}", 1, (193,227,234,255))
        screen.blit(score_text, (20, 20))

        # appliquer l'image du player
        screen.blit(self.player.image, self.player.rect)

        # actualiser la barre de vie du joueur
        self.player.update_health_bar(screen)

        # actualiser la barre d'evenement du jeu
        self.comet_event.update_bar(screen)

        # recuperer les projectiles du player
        for projectile in self.player.all_projectiles:
            projectile.move()

        # recuperer les monstres du jeu
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)

        # recuperer les cometes du jeu
        for comet in self.comet_event.all_comets:
            comet.fall()
            comet.move()

        # appliquer l'ensemble des images de mon groupe de projectiles
        self.player.all_projectiles.draw(screen)

        # appliquer l'ensemble des images du groupe de monstre
        self.all_monsters.draw(screen)

        # appliquer l'ensemble des images du groupe de cometes
        self.comet_event.all_comets.draw(screen)

        # verifier si le player souhaite aller à gauche ou à droite
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self):
        monster = Monster(self)
        self.all_monsters.add(monster)