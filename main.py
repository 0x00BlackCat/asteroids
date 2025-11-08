import pygame
import sys 
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot 
from constants import *
from logger import log_state, log_event
from player import *
import shot 

def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()


    Shot.containers = (shots, updatable, drawable)

    Player.containers = (updatable, drawable)  # type: ignore[attr-defined]

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0


    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt) 

        for asteroid in asteroids:
            if(asteroid.check_colision(player)):
                log_event("player_hit")
                print("Game Over!")
                sys.exit(1)

            for shot in shots:
                if(asteroid.check_colision(shot)):
                    log_event("asteroid_shot")
                    asteroid.split()
                    shot.kill()

        screen.fill("black")

        for s in drawable:
            s.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
