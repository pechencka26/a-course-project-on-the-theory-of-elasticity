import matplotlib.pyplot as plt
from methods.RungeKutta import RungeKutta
class Trajectory(RungeKutta):
    # Конструктор класса
    def __init__(self, x_coords, y_coords):
        # Инициализация объекта с координатами траектории
        self.x_coords = x_coords
        self.y_coords = y_coords

    # Метод для получения траектории в виде списка координат
    def get_trajectory(self):
        trajectory = []  # Список для хранения координат
        # Объединяем координаты X и Y в кортежи и добавляем в список
        for x, y in zip(self.x_coords, self.y_coords):
            trajectory.append((x, y))
        return trajectory

    # Метод для визуализации траектории с помощью графика
    def plot_trajectory(self, save_path=None):
        plt.plot(self.x_coords, self.y_coords, marker='o')
        plt.title("Траектория пути")
        plt.xlabel("X координаты")
        plt.ylabel("Y координаты")
        plt.grid()

        if save_path:  # Если указан путь, сохраняем график
            plt.savefig(save_path, format='jpeg', dpi=500)

        plt.show()