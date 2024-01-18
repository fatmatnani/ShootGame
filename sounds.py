import pygame

# Clase para gestionar los sonidos del juego
class SoundManager:

    def __init__(self):
        # Diccionario con los sonidos
        self.sounds = {
            'click': pygame.mixer.Sound('assets/sounds/click.ogg'),
            'game_over': pygame.mixer.Sound('assets/sounds/game_over.ogg'),
            'meteorite': pygame.mixer.Sound('assets/sounds/meteorite.ogg'),
            'tir': pygame.mixer.Sound('assets/sounds/tir.ogg'),
        }

    def play(self, name):
        # Reproducir un sonido basado en su nombre
        self.sounds[name].play()
