import pygame

# Clase para gestionar las animaciones
class AnimateSprite(pygame.sprite.Sprite):

    def __init__(self, sprite_name, size=(200, 200)):
        super().__init__()
        self.size = size
        self.image = pygame.image.load(f'assets/{sprite_name}.png')
        self.image = pygame.transform.scale(self.image, size)
        self.current_image = 0  # Comenzar la animación en la imagen 0
        self.images = animations.get(sprite_name)
        self.animation = False

    def start_animation(self):
        # Iniciar la animación
        self.animation = True

    def animate(self, loop=False):
        # Animar el sprite
        if self.animation:
            # Avanzar a la siguiente imagen
            self.current_image += 1

            # Verificar si se ha alcanzado el final de la animación
            if self.current_image >= len(self.images):
                # Reiniciar la animación en la imagen 0
                self.current_image = 0
                if not loop:
                    # Detener la animación si no está en modo bucle
                    self.animation = False

            # Cambiar la imagen actual por la siguiente
            self.image = self.images[self.current_image]
            self.image = pygame.transform.scale(self.image, self.size)

# Función para cargar las imágenes de una animación
def load_animation_images(sprite_name):
    # Cargar las 24 imágenes del sprite desde el directorio correspondiente
    images = []
    path = f"assets/{sprite_name}/{sprite_name}"

    # Iterar sobre cada imagen del directorio
    for num in range(1, 24):
        image_path = f"{path}{num}.png"
        images.append(pygame.image.load(image_path))

    # Devolver la lista de imágenes
    return images

# Diccionario que contendrá las imágenes cargadas de cada sprite
animations = {
    'mummy': load_animation_images('mummy'),
    'player': load_animation_images('player'),
    'alien': load_animation_images('alien'),
}
