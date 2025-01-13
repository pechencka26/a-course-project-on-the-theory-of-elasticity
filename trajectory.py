import matplotlib.pyplot as plt
from methods.RungeKutta import RungeKutta
class Trajectory(RungeKutta):
    # Конструктор класса
    def __init__(self, x_coords, y_coords):
        # Инициализация объекта с координатами траектории
        self.x_coords = x_coords  # Сохраняем координаты по оси X
        self.y_coords = y_coords  # Сохраняем координаты по оси Y

    # Метод для получения траектории в виде списка координат
    def get_trajectory(self):
        trajectory = []  # Список для хранения координат
        # Объединяем координаты X и Y в кортежи и добавляем в список
        for x, y in zip(self.x_coords, self.y_coords):
            trajectory.append((x, y))  # Добавляем точку в траекторию
        return trajectory  # Возвращаем список траектории

    # Метод для вывода траектории в консоль
    def print_trajectory(self):
        # Для каждого пункта траектории выводим координаты в консоль
        for point in self.get_trajectory():
            print(f"Координата: {point}")  # Печатаем координаты текущей точки

    # Метод для визуализации траектории с помощью графика
    def plot_trajectory(self):
        # Строим график, используя координаты X и Y
        plt.plot(self.x_coords, self.y_coords, marker='o')  # Отображаем точки на графике
        # Заголовок графика
        plt.title("Траектория пути")
        plt.xlabel("X координаты")
        plt.ylabel("Y координаты")
        plt.grid()
        plt.show()
