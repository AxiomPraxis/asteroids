"""
Player module
"""

import pygame
from pygame.key import ScancodeWrapper
from pygame.math import Vector2
from typing_extensions import override

from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_SHOOT_SPEED, PLAYER_SPEED, PLAYER_TURN_SPEED, SHOT_RADIUS


class Player(CircleShape):

    def __init__(self, x, y):
        super().__init__(x, y, radius=PLAYER_RADIUS)
        self.rotation: int = 0

        # in the player class

    def triangle(self):
        forward: Vector2 = pygame.Vector2(0, 1).rotate(self.rotation)
        right: float = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    @override
    def draw(self, screen: pygame.surface.Surface):
        _ = pygame.draw.polygon(surface=screen, color="white", points=self.triangle(), width=2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self, dt):
        shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
        velocity = pygame.Vector2(0, 1).rotate(self.rotation)
        shot.velocity = velocity * PLAYER_SHOOT_SPEED
        

    @override
    def update(self, dt):
        keys: ScancodeWrapper = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-1.0 * dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot(dt=dt)

class Shot(CircleShape):
    def __init__(self, x: float, y: float, radius: int):
        super().__init__(x, y, radius)
        self.x = x
        self.y = y
        self.radius: int = SHOT_RADIUS
        self.rotation: int = 0
    
    @override
    def draw(self, screen):
        _ = pygame.draw.circle(surface=screen, center=self.position, color="white", radius=self.radius, width=2)

    @override
    def update(self, dt: float):
        self.position += self.velocity * dt
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt