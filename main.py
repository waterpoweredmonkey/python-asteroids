# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame
from constants import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
from player import Player
from score import Score
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()


    Asteroid.containers = (updatables, drawables, asteroids)
    Shot.containers = (shots, updatables, drawables)
    AsteroidField.containers = (updatables)
    asteroid_field = AsteroidField()

    Player.containers = (updatables, drawables)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    Score.containers = (drawables)
    score = Score(16, 16, "READY!")

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        for updateable in updatables:
            updateable.update(dt)

        for asteroid in asteroids:
            if player.check_for_collision(asteroid):
                print("Game over!")
                sys.exit()
            for bullet in shots:
                if(bullet.check_for_collision(asteroid)):
                    score.add_score(asteroid.size_score())
                    asteroid.split()
                    bullet.kill()

        screen.fill("black")
        for drawable in drawables:
            drawable.draw(screen)
        pygame.display.flip()

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
