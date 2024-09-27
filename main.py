# this allows us to use code from the open-source pygame library throughout this file
import pygame
import sys
from constants import *
from circleshape import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots,updatable, drawable)

    player1 = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT /2)
    asteroidfield1 = AsteroidField()

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, color="black")
        for update in updatable:
            update.update(dt)
        for asteroid in asteroids:
            if asteroid.collision_check(player1) == True:
                sys.exit("Game Over!")
            for shot in shots:
                if asteroid.collision_check(shot) == True:
                    asteroid.split()
                    shot.kill()
        for draw in drawable:
            draw.draw(screen)
        pygame.display.flip()
        
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()