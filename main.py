import pygame
import math
from game import Game


pygame.init()
# definir une clock
clock = pygame.time.Clock()
FPS = 80

# generer la fenetre de notre jeu
pygame.display.set_caption("All against Aliens")
screen = pygame.display.set_mode((1080, 720))

# importer et charger l'arrière plan de notre jeu
background = pygame.image.load('assets/bg.jpg')

# importer et charger bannière
banner = pygame.image.load('assets/banner.png')
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 4)

# importer ou charger notre bouton pour lancer la partie
play_button = pygame.image.load('assets/button.png')
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 3.33)
play_button_rect.y = math.ceil(screen.get_height() / 2)
# charger notre jeu
game = Game()


running = True
# boucle tant que cette condition est vrai
while running:

    # appliquer la fenetre du jeu
    screen.blit(background, (0, -200))

    # vérifier si notre jeu a commencé
    if game.is_playing:
        # déclencher les instructions de la partie
        game.update(screen)
    # verifier si notre jeu n'a pas commencé
    else:
        # ajouter mon écran de bienvenue
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)

    # mettre à jour l'écran
    pygame.display.flip()

    # si le joueur ferme cette fenetre
    for event in pygame.event.get():
        # que l'événement est fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")
        # detecter si un joueur lache une touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
            # Détecter si la touche espace est enclenchée pour lancer notre projectile
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # verification pour savoir si la souris est en collision avec le bouton
            if play_button_rect.collidepoint(event.pos):
                # mettre le jeu en mode lancé
                game.start()
                # jouer le son
                game.sound_manager.play('click')

    # fixer le nombre de fps sur ma clock
    clock.tick(FPS)