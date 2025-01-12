import numpy as np

class MatCircle:
    def __init__(self, lifetime):
        self.radius = 3  # Радиус окружности
        self.lifetime = (0, lifetime)  # Время жизни тела
        self.cent_point_cord = (4, 4)  # Центр окружности (4, 4)
        self.color = 'blue'  # Цвет окружности

class CirclePoints(MatCircle):
    def __init__(self, num_points, lifetime):
        super().__init__(lifetime)  # Инициализация родительского класса MatCircle
        self.num_points = num_points  # Количество точек на окружности
        self.x_points = None  # Массив координат x
        self.y_points = None  # Массив координат y

    def generate_points(self):
        # Углы точек для полной окружности
        angles = np.linspace(0, 2 * np.pi, self.num_points)
        # Вычисляем координаты x и y с центром в (4, 4)
        self.x_points = self.radius * np.cos(angles) + self.cent_point_cord[0]
        self.y_points = self.radius * np.sin(angles) + self.cent_point_cord[1]

