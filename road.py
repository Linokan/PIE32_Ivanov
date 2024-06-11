import numpy as np
from car import PassengerCar, Truck, SpecialCar
from utils import MIN_INTERVAL, MAX_INTERVAL, kmh_to_ms, MIN_SPEED, MAX_SPEED

class Road:
    def __init__(self, length):
        self.length = length
        self.cars = []
        self.time_since_last_car = 0
        self.next_car_time = np.random.uniform(MIN_INTERVAL, MAX_INTERVAL)
        self.delayed_car = None
        self.delay_time = 5  # Время задержки в секундах

    def add_car(self, car):
        if not self.cars or self.cars[-1].position >= car.length * 4:  # 4 корпуса для безопасного старта
            self.cars.append(car)

    def update(self, delta_time):
        self.time_since_last_car += delta_time
        if self.time_since_last_car >= self.next_car_time: # Проверка интервала
            car_type = np.random.choice(['passenger', 'truck', 'special']) # Выбор генерации рандомного типа автомобиля
            initial_speed = np.random.uniform(kmh_to_ms(MIN_SPEED), kmh_to_ms(MAX_SPEED)) # Генерация скорости

            if car_type == 'passenger':
                new_car = PassengerCar(initial_speed, 0)
            elif car_type == 'truck':
                new_car = Truck(initial_speed, 0)
            elif car_type == 'special':
                new_car = SpecialCar(initial_speed, 0)

            self.add_car(new_car)
            self.time_since_last_car = 0
            self.next_car_time = np.random.uniform(MIN_INTERVAL, MAX_INTERVAL)

        for i, car in enumerate(self.cars):
            leading_car = self.cars[i-1] if i > 0 else None
            car.update(delta_time, leading_car)
            for other_car in self.cars:
                if car != other_car:
                    car.check_collision(other_car)

        # Обрабатываем искусственную задержку одного автомобиля
        if self.delayed_car:
            self.delay_time -= delta_time
            if self.delay_time <= 0:
                self.delayed_car.state = 'accelerating'
                self.delayed_car = None

    def delay_random_car(self):
        if not self.delayed_car and self.cars:
            self.delayed_car = np.random.choice(self.cars)
            self.delayed_car.state = 'braking'
            self.delay_time = 5

    def remove_car(self, car):
        if car in self.cars:
            self.cars.remove(car)