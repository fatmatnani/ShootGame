import pygame
from projectile import Projectile
import animation


# creer une premiere classe qui va representer notre joueur
class Player(animation.AnimateSprite):

    def __init__(self, game):
        super().__init__('player')
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 2
        self.all_projectiles = pygame.sprite.Group()

        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500

    def damage(self, amount):
        if self.health - amount > amount:
            self.health -= amount
        else:
            # si le joueur n'a plus de points de vie
            self.game.game_over()

    def update_animation(self):
        self.animate()
    def update_health_bar(self, surface):
        # definir une couleur pour notre jauge de vie (vert clair)
        bar_color = (111, 210, 46)
        # definoir une couleur pour l'arrière plan de la jauge(gris foncé)
        back_bar_color = (60, 63, 60)

        # definir la position de notre jauge de vie ainsi que de sa largeur
        bar_position = [self.rect.x + 50, self.rect.y + 20, self.health, 7]

        # definir la positionde l'arrière plan de la jauge de vie
        back_bar_position = [self.rect.x + 50, self.rect.y + 20, self.max_health, 7]

        # dessiner notre barre de vie
        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)

    def launch_projectile(self):
        # creer une nouvelle instance de la classe Projectile
        print("Launching projectile")
        self.all_projectiles.add(Projectile(self))
        # print("Number of projectiles:", len(self.all_projectiles))
        # démarrer l'animation du lancer
        self.start_animation()
        # démarrer le son du lancer
        self.game.sound_manager.play('tir')

    def move_right(self):
        # si le joueur n'est pas en collision avec un monstre
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity
