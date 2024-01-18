import pygame
import asyncio
import math
from game import Game

pygame.init()

# Definir un reloj
clock = pygame.time.Clock()
FPS = 80

# Definir las constantes de ancho y alto de pantalla
SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 720

# Generar la ventana de nuestro juego
pygame.display.set_caption("All against Aliens")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Importar y cargar el fondo de nuestro juego
background = pygame.image.load('assets/bg/bg3.png')
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Importar y cargar la bandera
banner = pygame.image.load('assets/banner.png')
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 4)

# Importar y cargar nuestro botón para iniciar el juego
play_button = pygame.image.load('assets/button.png')
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 3.33)
play_button_rect.y = math.ceil(screen.get_height() / 2)

# Cargar nuestro juego
game = Game(screen)



async def main():
    running = True
    # Bucle mientras esta condición sea verdadera
    while running:

        # Aplicar la ventana del juego
        screen.blit(background, (0, 10))

        # Verificar si nuestro juego ha comenzado
        if game.is_playing:
            # Activar las instrucciones de la partida
            game.update(screen)
        else:
            # Añadir nuestra pantalla de bienvenida
            screen.blit(play_button, play_button_rect)
            screen.blit(banner, banner_rect)

        # Actualizar la pantalla
        pygame.display.flip()

        # Si el jugador cierra esta ventana
        for event in pygame.event.get():
            # Si el evento es cerrar la ventana
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                #print("Cierre del juego")
            # Detectar si un jugador suelta una tecla
            elif event.type == pygame.KEYDOWN:
                game.pressed[event.key] = True
                # Detectar si la tecla espaciadora está presionada para lanzar nuestro proyectil
                if event.key == pygame.K_SPACE:
                    game.player.launch_projectile()

            elif event.type == pygame.KEYUP:
                game.pressed[event.key] = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Verificar para saber si el ratón está en colisión con el botón
                if play_button_rect.collidepoint(event.pos):
                    # Poner el juego en modo de inicio
                    game.start()
                    # Reproducir el sonido
                    game.sound_manager.play('click')

        # Establecer el número de fps en nuestro reloj
        clock.tick(FPS)
        await asyncio.sleep(0)

asyncio.run(main())        
