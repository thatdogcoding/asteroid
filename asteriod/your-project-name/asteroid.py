import pygame
from logger import log_event
import random
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius == ASTEROID_MIN_RADIUS:
            return 
        else:
            log_event("asteroid_split")
            angle = random.uniform(20, 50)
            vector_1 = self.velocity.rotate(angle)
            vector_2 = self.velocity.rotate(-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            a_1 = Asteroid(self.position.x, self.position.y, new_radius)
            a_2 = Asteroid(self.position.x, self.position.y , new_radius)
            a_1.velocity = vector_1 * 1.2
            a_2.velocity = vector_2 * 1.2





