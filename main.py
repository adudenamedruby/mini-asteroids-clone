import sys

import pygame

from asteroid import Asteroid
from astrofield import AsteroidField
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player
from shot import Shot


def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    dt = 0

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)
    Shot.containers = (shots, drawable, updateable)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(color="black")

        updateable.update(dt)

        for thing in drawable:
            thing.draw(screen)

        for asteroid in asteroids:
            if asteroid.is_colliding_with(player):
                print("Game Over!")
                sys.exit()

        for asteroid in asteroids:
            for shot in shots:
                if asteroid.is_colliding_with(shot):
                    asteroid.split()
                    shot.kill()

        pygame.display.flip()
        # framerate limiter
        dt = clock.tick(60)/1000
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()
