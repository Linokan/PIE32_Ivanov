import pygame
from road import Road
from visualization import update_screen

def main():
    clock = pygame.time.Clock()
    road = Road(length=1000)  # Длина дороги в метрах

    running = True
    while running:
        delta_time = clock.get_time() / 1000.0  # Время между кадрами в секундах

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    road.delay_random_car()

        road.update(delta_time)
        update_screen(road)

        clock.tick(60)  # Ограничение до 60 кадров в секунду

    pygame.quit()

if __name__ == "__main__":
    main()
