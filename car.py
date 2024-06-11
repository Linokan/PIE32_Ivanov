from utils import PAS_CAR_LENGTH, TRUCK_CAR_LENGTH, SPEC_CAR_LENGTH, ACCIDENT_DURATION


class Car:
    def __init__(self, initial_speed, position, color=(0, 255, 0)):
        self.initial_speed = initial_speed
        self.speed = initial_speed
        self.position = position
        self.color = color
        self.state = 'moving'  # Состояния: moving (движется), braking (тормозит), accelerating (ускоряется), stopped (остановилась)
        self.accident_duration = ACCIDENT_DURATION # время после аварии, после которого машина продолжает движение
        self.accident_time = 0 # время после аварии, счетчик

    def update(self, delta_time, leading_car=None):
        if self.state == 'braking':
            # Применяем закон торможения
            self.braking_law(delta_time)
            # Если расстояние до ведущей машины больше безопасного, переходим в состояние "движение"
            if not leading_car or self.position + self.length * 4 < leading_car.position:
                self.state = 'moving'
        elif self.state == 'accelerating':
            # Увеличиваем скорость на определенную величину (ACCELERATE_RATE)
            self.speed = min(self.initial_speed, self.speed + ACCELERATE_RATE * delta_time)  # Пример закона ускорения
            if self.speed == self.initial_speed:
                self.state = 'moving'
        elif self.state == 'moving':
            if leading_car and self.position + self.length * 4 >= leading_car.position:  # Если расстояние до впереди идущей машины меньше 2 корпусов, начинаем тормозить
                self.state = 'braking'
        elif self.state == 'stopped':
            self.accident_time += delta_time
            if self.accident_time >= self.accident_duration:
                self.state = 'moving'
                road = self.get_road_instance()
                road.remove_car(self)  # Удаляем машину из объекта Road

        self.position += self.speed * delta_time


    # Торможение
    def braking_law(self, delta_time):
        # Максимальное ускорение при торможении
        max_braking_acceleration = 5  # км/ч^2
        # Минимальная целевая скорость (20% от начальной)
        target_speed = self.initial_speed * 0.2  # км/ч

        # Если скорость больше или равна целевой, тормозим с максимальным ускорением
        if self.speed >= target_speed:
            # Уменьшаем скорость на максимальное ускорение
            self.speed = max(0, self.speed - max_braking_acceleration * delta_time)


    # Проверка столкновения автомобилей
    def check_collision(self, other_car):
        if self.position + self.length >= other_car.position and self.position <= other_car.position + other_car.length:
            self.state = 'stopped'
            other_car.state = 'stopped'
            self.speed = 0
            other_car.speed = 0

class PassengerCar(Car):
    # Легковой автомобиль
    def __init__(self, initial_speed, position):
        super().__init__(initial_speed, position, (0, 0, 255))  # Синий цвет для легкового автомобиля
        self.type = 'passenger'
        self.length = PAS_CAR_LENGTH # Длина легковушки в метрах

class Truck(Car):
    # Грузовик
    def __init__(self, initial_speed, position):
        super().__init__(initial_speed, position, (255, 0, 0))  # Красный цвет для грузовика
        self.length = TRUCK_CAR_LENGTH  # Длина грузовика в метрах
        self.type = 'truck'

class SpecialCar(Car):
    # Специальная машина (пожарная и т.д.)
    def __init__(self, initial_speed, position):
        super().__init__(initial_speed, position, (0, 255, 0))  # Зеленый цвет для специального автомобиля
        self.length = SPEC_CAR_LENGTH  # Длина специального автомобиля в метрах
        self.type = 'special'
