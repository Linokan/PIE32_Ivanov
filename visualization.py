import pygame
from utils import SCREEN_HEIGHT, SCREEN_WIDTH, ROAD_HEIGHT, ROAD_COLOR, LINE_COLOR, letter_S, letter_G, letter_L
from car import PassengerCar, Truck, SpecialCar

# Инициализация Pygame
pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


def draw_road():
    road_rect = pygame.Rect(0, (SCREEN_HEIGHT - ROAD_HEIGHT) / 2, SCREEN_WIDTH, ROAD_HEIGHT)
    pygame.draw.rect(screen, ROAD_COLOR, road_rect)

    # Рисуем центральную разметку
    line_width = 5
    for x in range(0, SCREEN_WIDTH, 40):
        pygame.draw.line(screen, LINE_COLOR,
                         (x, (SCREEN_HEIGHT + line_width) / 2),
                         (x + 20, (SCREEN_HEIGHT + line_width) / 2), line_width)


def draw_car(car):
    x = car.position * SCREEN_WIDTH / 1000  # Конвертация позиции из метров в пиксели
    y = (SCREEN_HEIGHT - ROAD_HEIGHT) / 2 + (ROAD_HEIGHT - car.length * 3) / 2  # Центрируем машины на дороге
    car_rect = pygame.Rect(x, y, car.length * 6, car.length * 3)

    # Определение цвета машины в зависимости от ее состояния
    if car.state == 'braking':
        color = (0, 0, 255)  # Синий цвет при торможении
    elif car.state == 'accelerating':
        color = (255, 0, 0)  # Красный цвет при ускорении
    elif car.state == 'stopped':
        color = (0, 0, 0)  # Черный цвет при аварии
    else:
        color = (0, 255, 0)  # Зеленый цвет при обычном движении

    # Рисуем машину с контуром
    pygame.draw.rect(screen, color, car_rect.move(x - car.position * SCREEN_WIDTH / 1000, 0))
    pygame.draw.rect(screen, (0, 0, 0), car_rect.inflate(2, 2).move(x - car.position * SCREEN_WIDTH / 1000, 0), 1)

    # Отрисовка буквы в центре машины
    if isinstance(car, PassengerCar):
        screen.blit(letter_L, (car_rect.centerx - letter_L.get_width() / 2, car_rect.centery - letter_L.get_height() / 2))
    elif isinstance(car, Truck):
        screen.blit(letter_G, (car_rect.centerx - letter_G.get_width() / 2, car_rect.centery - letter_G.get_height() / 2))
    elif isinstance(car, SpecialCar):
        screen.blit(letter_S, (car_rect.centerx - letter_S.get_width() / 2, car_rect.centery - letter_S.get_height() / 2))


def update_screen(road):
    screen.fill((255, 255, 255))  # Белый фон
    draw_road()  # Рисуем дорогу
    for car in road.cars:
        draw_car(car)
    pygame.display.flip()
