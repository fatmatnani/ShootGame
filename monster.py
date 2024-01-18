import pygame
import random
import animation

# Crear una clase para gestionar el concepto de monstruo en nuestro juego
class Monster(animation.AnimateSprite):

    def __init__(self, game, name, size, offset=0):
        super().__init__(name, size)
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.3
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 540 - offset
        self.loot_amount = 10
        self.start_animation()

    def set_speed(self, speed):
        self.default_speed = speed
        self.velocity = random.randint(1, speed)

    def set_loot_amount(self, amount):
        self.loot_amount = amount

    def damage(self, amount):
        # Infligir daño
        self.health -= amount

        # Verificar si la salud ha llegado a 0
        if self.health <= 0:
            # Reaparecer como un nuevo monstruo
            self.rect.x = 1000 + random.randint(0, 300)
            self.velocity = random.randint(1, self.default_speed)
            self.health = self.max_health
            # Añadir puntuación
            self.game.add_score(self.loot_amount)

            # Si el evento de cometas está completamente cargado
            if self.game.comet_event.is_full_loaded():
                # Eliminar al monstruo del juego
                self.game.all_monsters.remove(self)

                # Intentar activar la lluvia de cometas
                self.game.comet_event.attempt_fall()

    def update_animation(self):
        self.animate(loop=True)

    def update_health_bar(self, surface):
        # Definir color de la barra de salud (verde claro)
        bar_color = (111, 210, 46)
        # Definir color de fondo de la barra de salud (gris oscuro)
        back_bar_color = (60, 63, 60)

        # Definir posición y tamaño de la barra de salud
        bar_position = [self.rect.x + 10, self.rect.y - 20, self.health, 5]
        # Definir posición y tamaño del fondo de la barra de salud
        back_bar_position = [self.rect.x + 10, self.rect.y - 20, self.max_health, 5]

        # Dibujar la barra de salud
        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)

    def forward(self):
        # Moverse solo si no hay colisión con el jugador
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        # Si hay colisión con el jugador
        else:
            # Infligir daño al jugador
            self.game.player.damage(self.attack)

# Definir clase para la momia
class Mummy(Monster):

    def __init__(self, game):
        super().__init__(game, "mummy", (130, 130))
        self.set_speed(3)
        self.set_loot_amount(20)

# Definir clase para el alien
class Alien(Monster):

    def __init__(self, game):
        super().__init__(game, "alien", (300, 300), 140)
        self.health = 250
        self.max_health = 250
        self.attack = 0.8
        self.set_speed(2)
        self.set_loot_amount(80)
