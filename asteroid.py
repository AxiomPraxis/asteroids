import pygame
from typing_extensions import override

from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius):
        super().__init__(x, y, radius)
        self.x = x
        self.y = y
        self.radius = radius

    @override
    def draw(self, screen):
        _ = pygame.draw.circle(surface=screen, center=self.position, color="white", radius=self.radius, width=2)

    @override
    def update(self, dt: float):
        self.position += self.velocity * dt
