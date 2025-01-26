# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
    init_result = pygame.init()
    print(f"pygame init results; num_pass:{init_result[0]}, num_fail:{init_result[1]}")
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill((0,0,0))
        pygame.display.flip()

if __name__ == "__main__":
    main()
