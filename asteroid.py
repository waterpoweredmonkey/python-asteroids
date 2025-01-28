import pygame
from circleshape import CircleShape
from constants import *
from random import uniform

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def size_score(self):
        return self.radius / ASTEROID_MIN_RADIUS

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        random_angle = uniform(20, 50)

        new_velocity = self.velocity * 1.2
        velocities = [
            new_velocity.rotate(random_angle),
            new_velocity.rotate(-random_angle),
        ]
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        for velocity in velocities:
            asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid.velocity = velocity
        