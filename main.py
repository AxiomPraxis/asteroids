'''
Asteroids
'''
import sys
from typing import Any

import pygame
from pygame.sprite import Group
from pygame.surface import Surface
from pygame.time import Clock

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player



def main():
    '''
    Asteroids main function
    '''
    _ = pygame.init()
    updateable: Group[Any] = pygame.sprite.Group()
    drawable: Group[Any] = pygame.sprite.Group()
    asteroids: Group[Any] = pygame.sprite.Group()
    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = updateable
    screen: Surface = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
    clock: Clock = pygame.time.Clock()
    dt: float = 0.0
    player: Player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)
    asteroidfield: AsteroidField = AsteroidField()
    running = True
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        _ = screen.fill(color="black")
        dt= clock.tick(60) / 1000
        updateable.update(dt)
        for asteroid in asteroids:
            if asteroid.collision_check(player):
                print("Game over!")
                sys.exit(0)
        for item in drawable:
            item.draw(screen)
        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()
