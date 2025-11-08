from circleshape import CircleShape
import pygame
import random

from constants import ASTEROID_MIN_RADIUS
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)


    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)


    def update(self,dt):
        self.position += self.velocity * dt

    def split(self):
        x,y = self.position
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        log_event("asteroid_split")
        angle = random.uniform(20, 50)

        v1 = self.velocity.rotate(angle)
        v2 = self.velocity.rotate(-angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        a1 = Asteroid(x, y, new_radius)
        a2 = Asteroid(x, y, new_radius)

        a1.velocity = v1 * 1.2
        a2.velocity = v2 * 1.2