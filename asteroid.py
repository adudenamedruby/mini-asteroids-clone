import random

import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        return pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20, 50)
            positive_vector = self.velocity.rotate(angle)
            negative_vector = self.velocity.rotate(-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid_one = Asteroid(self.position[0], self.position[1], new_radius)
            asteroid_two = Asteroid(self.position[0], self.position[1], new_radius)
            asteroid_one.velocity = positive_vector * 1.2
            asteroid_two.velocity = negative_vector * 1.2
