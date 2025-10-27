import pygame 
from constants import *
from player import Player
from shot import Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():

    pygame.init()

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    player = Player(x, y)
    astro_field = AsteroidField()

    clock = pygame.time.Clock()
    dt = 0
    
    while (True):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill((0, 0, 0))
        
        updatable.update(dt)

        for asteroid in asteroids:
            if (asteroid.detectcollision(player)):
                font = pygame.font.Font(None, 74)

                text = font.render("Game Over!", True, (255, 255, 255))

                screen.blit(text, (SCREEN_WIDTH / 2 - text.get_width() / 2,
                                SCREEN_HEIGHT / 2 - text.get_height() / 2))
                
                pygame.display.flip()
                
                pygame.time.wait(2000)
                return
            
        
        for asteroid in asteroids:
            for shot in shots:
                if (asteroid.detectcollision(shot)):
                    asteroid.split()
                    shot.kill()


        for thing in drawable:
            thing.draw(screen)

        dt = clock.tick(60) / 1000

        pygame.display.flip()


if __name__ == "__main__":
    main()
