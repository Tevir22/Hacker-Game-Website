import pygame
import random

# creer une classe qui va gérer la notion de monstre sur le jeu
class Monster(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 1
        self.image = pygame.image.load('assets2/monster2-modified (1).png')
        self.image = pygame.transform.scale(self.image, (175, 175))
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 510
        self.velocity = random.randint(1, 2)

    def damage(self, amount):
        # infliger les dégats
        self.health -= amount

        # Verifier si son nouveau nombre de pdv et >= 0
        if self.health <= 0:
            # Reapparaitre comme un nouveau monstre
            self.rect.x = 1000 + random.randint(0, 300)
            self.velocity = random.randint(4, 10)
            self.health = self.max_health
            # ajouter le nombre de points
            self.game.score += 10

    def update_health_bar(self, surface):
        # dessiner la bar de vie
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 45, self.rect.y - 20, self.max_health, 5])
        pygame.draw.rect(surface, (193,227,234,255), [self.rect.x + 45, self.rect.y - 20, self.health, 5])

    def forward(self):
        # le deplacement ne se fait que s'il n'y a pas de collision avec un groupe de player
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        # si le monstre est en collision avedc le joueur
        else:
            # infliger des dégats (au joueur)
            self.game.player.damage(self.attack)