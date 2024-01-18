import pygame
from player import Player
from monster import Mummy, Alien
from comet_event import CometFallEvent
from sounds import SoundManager


class Game:
    def __init__(self, screen):
        self.screen = screen
        # Definir si nuestro juego ha comenzado
        self.is_playing = False
        # Generar nuestro jugador
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        # Generar el evento
        self.comet_event = CometFallEvent(self)
        # Grupo de monstruos
        self.all_monsters = pygame.sprite.Group()
        # Gestionar el sonido
        self.sound_manager = SoundManager()
        # Puntuación inicial
        self.font = pygame.font.Font("assets/my_custom_font.ttf", 25)
        self.score = 0
        # Teclas presionadas
        self.pressed = {}

    def start(self):
        self.is_playing = True
        self.spawn_monster(Mummy)
        self.spawn_monster(Mummy)
        self.spawn_monster(Alien)

    def add_score(self, points=10):
        self.score += points

    def game_over(self):
        # Reproducir el sonido de fin del juego
        self.sound_manager.play('game_over')

        # Cargar la imagen de 'Game Over'
        game_over_image = pygame.image.load('assets/bg/game-over1.png')
        game_over_image_rect = game_over_image.get_rect(
            center=(self.screen.get_width() / 2, self.screen.get_height() / 2))

        # Llenar la pantalla con negro
        self.screen.fill((0, 0, 0))

        # Poner la imagen de 'Game Over' en la pantalla
        self.screen.blit(game_over_image, game_over_image_rect)

        # Actualizar la pantalla para mostrar la imagen de 'Game Over'
        pygame.display.flip()

        # Pausar por unos segundos para mostrar la pantalla de 'Game Over'
        pygame.time.wait(3000)

        # Reiniciar el estado del juego
        self.is_playing = False
        self.all_monsters = pygame.sprite.Group()
        self.comet_event.all_comets = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.comet_event.reset_percent()
        self.score = 0

    def update(self, screen):
        # Mostrar la puntuación en la pantalla
        score_text = self.font.render(f"Score: {self.score}", True, (0, 255, 255))
        screen.blit(score_text, (20, 20))

        # Aplicar la imagen de nuestro jugador
        screen.blit(self.player.image, self.player.rect)

        # Actualizar la barra de salud del jugador
        self.player.update_health_bar(screen)

        # Actualizar la barra de evento de cometas
        self.comet_event.update_bar(screen)

        # Actualizar la animación del jugador
        self.player.update_animation()

        # Mover los proyectiles del jugador
        for projectile in self.player.all_projectiles:
            projectile.move()

        # Actualizar los monstruos
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)
            monster.update_animation()

        # Actualizar las cometas
        for comet in self.comet_event.all_comets:
            comet.fall()

        # Dibujar las cometas
        self.comet_event.all_comets.draw(screen)

        # Separar los Aliens de los otros monstruos
        all_aliens = [alien for alien in self.all_monsters if isinstance(alien, Alien)]
        all_other_monsters = [monster for monster in self.all_monsters if not isinstance(monster, Alien)]

        # Dibujar primero los Aliens
        for alien in all_aliens:
            screen.blit(alien.image, alien.rect)

        # Luego dibujar los otros monstruos para que estén en frente de los Aliens
        for monster in all_other_monsters:
            screen.blit(monster.image, monster.rect)

        # Dibujar los proyectiles
        self.player.all_projectiles.draw(screen)

        # Verificar si el jugador quiere moverse a la izquierda o derecha
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()




    def check_collision(self, sprite, group):
        # Comprobar colisiones
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self, monster_class_name):
        # Añadir un nuevo monstruo
        self.all_monsters.add(monster_class_name(self))
