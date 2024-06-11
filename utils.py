import pygame

pygame.init()

# Размеры автомобиля для визуализации (в пикселях)
CAR_VISUAL_LENGTH = 30
CAR_VISUAL_WIDTH = 15

# Константы
PAS_CAR_LENGTH = 5  # Длина легкого автомобиля
TRUCK_CAR_LENGTH = 10 # Длина грузовика
SPEC_CAR_LENGTH = 7 # Длина спец. автомобиля
MIN_SPEED = 50  # Минимальная начальная скорость (км/ч)
MAX_SPEED = 100  # Максимальная начальная скорость (км/ч)
MIN_INTERVAL = 3  # Минимальный интервал появления автомобилей (сек)
MAX_INTERVAL = 5  # Максимальный интервал появления автомобилей (сек)
BRAKE_RATE = 5  # Скорость торможения (км/ч^2)
ACCELERATE_RATE = 2  # Скорость ускорения (км/ч^2)
TARGET_SPEED = 20  # Целевая скорость при торможении (км/ч)
ACCIDENT_DURATION = 3 # Длительность остановки после аварии

# Установка размеров окна
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
ROAD_HEIGHT = 100  # Высота однополосной дороги в пикселях
ROAD_COLOR = (50, 50, 50)  # Серый цвет для дороги
LINE_COLOR = (255, 255, 255)  # Белый цвет для разметки

# Определение размера и цвета текста
TEXT_SIZE = 20
TEXT_COLOR = (255, 255, 255)

# Загрузка шрифтов
font = pygame.font.SysFont(None, TEXT_SIZE)

# Создание изображений букв для каждого типа машины
letter_L = font.render('Л', True, TEXT_COLOR)
letter_G = font.render('Г', True, TEXT_COLOR)
letter_S = font.render('С', True, TEXT_COLOR)

# Конвертация км/ч в м/с
def kmh_to_ms(speed_kmh):
    return speed_kmh * 1000 / 3600
