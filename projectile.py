import pygame


class Projectile(pygame.sprite.Sprite):

    def __init__(self, player):
        super().__init__()
        self.velocity = 3
        self.player = player
        self.image = pygame.image.load('assets/projectile.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 120
        self.rect.y = player.rect.y + 80
        self.origin_image = self.image
        self.angle = 0

    def rotate(self):
        # Rotar el proyectil
        self.angle += 8
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def remove(self):
        # Eliminar el proyectil del grupo
        self.player.all_projectiles.remove(self)

    def move(self):
        # Mover el proyectil
        self.rect.x += self.velocity
        self.rotate()

        # Verificar si el proyectil colisiona con algún monstruo
        for monster in self.player.game.check_collision(self, self.player.game.all_monsters):
            # Eliminar el proyectil
            self.remove()
            # Aplicar daño al monstruo
            monster.damage(self.player.attack)

        # Verificar si el proyectil ya no está en la pantalla
        if self.rect.x > 1080:
            # Eliminar el proyectil si está fuera de la pantalla
            self.remove()
