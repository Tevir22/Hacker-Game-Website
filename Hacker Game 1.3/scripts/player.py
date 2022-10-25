import pygame
from projectile import Projectile

# creer une premiere classe qui va representer le player
class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 20
        self.velocity = 6
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load('assets2/player2.png')
        self.image = pygame.transform.scale(self.image, (175, 175))
        self.rect = self.image.get_rect()
        self.rect.x = 2
        self.rect.y = 500

    def damage(self, amound):
        if self.health - amound > amound:
            self.health -= amound
        else:
            # si le joueur n'a plus de pdv
            self.game.game_over()

    def update_health_bar(self, surface):
        # dessiner la bar de vie
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 35, self.rect.y - 25, self.max_health, 7])
        pygame.draw.rect(surface, (193,227,234,255), [self.rect.x + 35, self.rect.y - 25, self.health, 7])

    def launch_projectile(self):
        # creer une nouvelle instance de la classe Projectile
        self.all_projectiles.add(Projectile(self))
        # jouer le son
        self.game.sound_manager.play('tir')

    def move_right(self):
        # si le player n'est pas en collision avec une entité monstre
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity