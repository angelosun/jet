import pygame
from Params import Params
# Define a player object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'player'
# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()

    # Move the sprite based on user keypresses
    def update(self, pressed_keys):
        if pressed_keys[Params.K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[Params.K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[Params.K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[Params.K_RIGHT]:
            self.rect.move_ip(5, 0)        

        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > Params.SCREEN_WIDTH:
            self.rect.right = Params.SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= Params.SCREEN_HEIGHT:
            self.rect.bottom = Params.SCREEN_HEIGHT   