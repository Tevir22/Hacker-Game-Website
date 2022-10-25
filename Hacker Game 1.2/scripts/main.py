import pygame
import math
from game import Game

pygame.init()

# definir une clock
clock = pygame.time.Clock()
FPS = 300

# generer la fenetre du jeu
pygame.display.set_caption("HACKER GAME by Blue Bear")
screen = pygame.display.set_mode((1080, 720))

# importer et charger l'arriere plan du jeu
background = pygame.image.load('assets2/background2.png')

# importer le bannière
banner = pygame.image.load('assets2/banner2 (2).png')
banner = pygame.transform.scale(banner, (500, 575))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 4)
banner_rect.y = math.ceil(screen.get_height() / 200)

# importer le bouton pour lancer la partie
play_button = pygame.image.load('assets2/banner2 (2).png')
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 3.33)
play_button_rect.y = math.ceil(screen.get_height() / 1.9)

# charger le jeu
game = Game()
running = True

# boucle tant que cette condition est vraie
while running:

    # appliquer l'arriere plan du jeu
    screen.blit(background, (0, 0))

    # verifier si le jeu a commencé ou non
    if game.is_playing:
        # déclencher les instructions de la partie
        game.update(screen)
    # verifier si notre jeu n'a pas commencé
    else:
        # ajouter mon écran de bienvenue
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)

    # mettre à jour l'ecran
    pygame.display.flip()

    # si le player ferme cette fenetre
    for event in pygame.event.get():
        # que l'evenement est fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")
        # detecter si un player lache une touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            # detecter si la touche espace est enclenchée pour lancer le projectile
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # verification pour savoir si la souris est en collision avec le bouton jouer
            if play_button_rect.collidepoint(event.pos):
                # mettre le jeu en mode "lancé"
                game.start()
                # jouer le son
                game.sound_manager.play('click')

    # fixer le nombre de fps sur la clock
    clock.tick(FPS)