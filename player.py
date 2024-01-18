import pygame
from projectile import Projectile
import animation

# Crear una primera clase que va a representar a nuestro jugador
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
        # Infligir daño y verificar si el jugador aún tiene vida
        if self.health - amount > amount:
            self.health -= amount
        else:
            # Si el jugador no tiene más puntos de vida
            self.game.game_over()

    def update_animation(self):
        # Actualizar la animación
        self.animate()

    def update_health_bar(self, surface):
        # Definir un color para la barra de salud (verde claro)
        bar_color = (111, 210, 46)
        # Definir un color para el fondo de la barra de salud (gris oscuro)
        back_bar_color = (60, 63, 60)

        # Definir la posición y tamaño de la barra de salud
        bar_position = [self.rect.x + 50, self.rect.y + 20, self.health, 7]
        # Definir la posición y tamaño del fondo de la barra de salud
        back_bar_position = [self.rect.x + 50, self.rect.y + 20, self.max_health, 7]

        # Dibujar la barra de fondo y la barra de salud
        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)

    def launch_projectile(self):
        # Crear una nueva instancia de la clase Projectile
        #print("Lanzamiento de proyectil")
        self.all_projectiles.add(Projectile(self))
        # Iniciar la animación de lanzamiento
        self.start_animation()
        # Reproducir el sonido de lanzamiento
        self.game.sound_manager.play('tir')

    def move_right(self):
        # Mover al jugador a la derecha si no está en colisión con un monstruo
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity

    def move_left(self):
        # Mover al jugador a la izquierda
        self.rect.x -= self.velocity
