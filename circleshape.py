import pygame


# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position: pygame.Vector2 = pygame.Vector2(x, y)
        self.velocity: pygame.Vector2 = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen: pygame.surface.Surface):
        # sub-classes must override
        pass

    def update(self, dt: float):
        # sub-classes must override
        pass

    def collision_check(self, circle):
        collision_distance = self.radius + circle.radius
        actual_distance = pygame.Vector2.distance_to(self.position, circle.position)
        if actual_distance <= collision_distance:
            return True
        else:
            return False
