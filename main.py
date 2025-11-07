import pygame
from constants import *
from logger import log_state
from player import * 

def main():
    pygame.init()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)  # type: ignore[attr-defined]


    px = SCREEN_WIDTH / 2
    py = SCREEN_HEIGHT / 2

    player = Player(px, py)

    dt = 0

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        updatable.update(dt) 
        for s in drawable:
            s.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
