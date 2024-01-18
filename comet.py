import pygame
import random

# Clase para gestionar la cometa
class Comet(pygame.sprite.Sprite):
    def __init__(self, comet_event):
        super().__init__()
        # Definir la imagen asociada a esta cometa
        full_size_image = pygame.image.load('assets/comet.png')
        # Redimensionar la imagen al tamaño nuevo
        self.image = pygame.transform.scale(full_size_image, (128, 128))  # Redimensionar a 128x128 o al tamaño que se necesite
        self.rect = self.image.get_rect()
        self.velocity = random.randint(1, 3)
        self.rect.x = random.randint(20, 950)
        self.rect.y = -random.randint(0, 800)
        self.comet_event = comet_event

    def remove(self):
        # Eliminar la cometa del grupo
        self.comet_event.all_comets.remove(self)
        # Reproducir el sonido
        self.comet_event.game.sound_manager.play('meteorite')
        # Verificar si el número de cometas es 0
        if len(self.comet_event.all_comets) == 0:
            # Resetear la barra de cometas a 0
            self.comet_event.reset_percent()
            # Hacer aparecer de nuevo los monstruos
            self.comet_event.game.start()

    def fall(self):
        # Caer (mover la cometa hacia abajo)
        self.rect.y += self.velocity

        # No caer fuera de la pantalla (simular el suelo)
        if self.rect.y >= 600:
            # Eliminar la cometa si sale de la pantalla
            self.remove()

        # Verificar si la cometa impacta al jugador
        if self.comet_event.game.check_collision(self, self.comet_event.game.all_players):
            # Eliminar la cometa al impactar
            self.remove()
            # Infligir daño al jugador
            self.comet_event.game.player.damage(20)
