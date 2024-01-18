import pygame
from comet import Comet

# Clase para manejar eventos de caída de cometas a intervalos regulares
class CometFallEvent:
    def __init__(self, game):
        self.percent = 0
        self.percent_speed = 10
        self.game = game
        self.fall_mode = False

        # Definir un grupo de sprites para almacenar nuestras cometas
        self.all_comets = pygame.sprite.Group()

    def add_percent(self):
        self.percent += self.percent_speed / 100

    def is_full_loaded(self):
        # Verificar si la barra de evento está completamente cargada
        return self.percent >= 100

    def reset_percent(self):
        # Reiniciar la barra de evento
        self.percent = 0

    def meteor_fall(self):
        # Bucle para lanzar varias cometas
        for _ in range(1, 10):
            self.all_comets.add(Comet(self))

    def attempt_fall(self):
        # Intentar la caída de meteoritos si el evento está completamente cargado y no hay monstruos
        if self.is_full_loaded() and len(self.game.all_monsters) == 0:
            #print("cometas")  # Lluvia de cometas
            self.meteor_fall()
            self.fall_mode = True  # Activar el evento

    def update_bar(self, surface):
        # Añadir porcentaje a la barra
        self.add_percent()

        # Barra negra de fondo
        pygame.draw.rect(surface, (0, 0, 0), [
            0,  # Eje X
            surface.get_height() - 20,  # Eje Y
            surface.get_width(),  # Longitud de la ventana
            10  # Grosor de la barra
        ])
        # Barra roja de la barra de eventos
        pygame.draw.rect(surface, (187, 11, 11), [
            0,  # Eje X
            surface.get_height() - 20,  # Eje Y
            (surface.get_width() / 100) * self.percent,  # Longitud de la ventana
            10  # Grosor de la barra
        ])
