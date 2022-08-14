import pygame


class Laser(pygame.sprite.Sprite):
    def __init__(self, pos, speed, max_y_constraint):
        super().__init__()
        self.image = pygame.Surface((4, 20))
        self.image.fill('orange')
        self.rect = self.image.get_rect(center=pos)
        self.speed = speed
        self.max_y_constraint = max_y_constraint

    def destroy(self):
        if self.rect.y <= -50 or self.rect.y >= self.max_y_constraint + 50:
            self.kill()

    def update(self):
        self.rect.y -= self.speed
        self.destroy()
