import numpy as np

class MaterialCircle:
    def __init__(self, radius, center):
        self.radius = radius
        self.center = center
        self.points = []  # Лист для сохранения точек окружности

    def generate_points(self, num_points):
        angles = np.linspace(0, np.pi*2, num_points)  # Углы для первой четверти
        for angle in angles:
            x = self.center[0] + self.radius * np.cos(angle)
            y = self.center[1] + self.radius * np.sin(angle)
            self.points.append((x, y))

    def get_points(self):
        return self.points
